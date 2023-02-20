import json
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score
from ui_mainwindow import Ui_MainWindow
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import parser
import csv
import multiprocessing as ml
from Stemmer import Stemmer
import os
import re
import pickle

count_gpu = 20
main_path = 'data'
tegs = ['авто', 'культура', 'спорт', 'юмор', 'образование', 'бизнес', 'путешествие']


def text_cleaner(text):
    text = text.lower()  # приведение в lowercase
    stemmer = Stemmer('russian')
    text = ' '.join(stemmer.stemWords(text.split()))
    text = re.sub(r'\b\d+\b', ' digit ', text)  # замена цифр
    return text


def get_data_str():
    return open('data.csv', 'r').read()


def add_data(tag, url):
    open('data.csv', 'a').write(f'\n{tag},{url}')


def set_data(path):
    open('data.csv', 'w').write(open(path, 'r').read())


def get_data():
    return list(csv.reader(open('data.csv', 'r')))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_pars.clicked.connect(self.parsing)
        self.ui.data_plane_text_2.setPlainText(get_data_str())
        self.ui.add.clicked.connect(self.add)

        if 'data' not in os.listdir():
            os.mkdir('data')

        self.x = []
        self.y = []
        self.tegs_lens = {}
        for teg in tegs:
            if teg not in os.listdir('data/'):
                os.mkdir(f'data/{teg}')
            self.tegs_lens[teg] = 0
            for file in os.listdir(f'{main_path}/{teg}'):
                texts = list(map(lambda x: x.lower().strip(), open(f'{main_path}/{teg}/{file}', 'r', encoding='utf8').readlines()))
                self.tegs_lens[teg] += len(texts)
                self.x.append('\n'.join(texts))
                self.y.append(teg)

        self.cvs = {
            'TfidfVectorizer': TfidfVectorizer(),
            'CountVectorizer': CountVectorizer()
        }
        self.models = {
            'LinearDiscriminantAnalysis': LinearDiscriminantAnalysis(),
            'LogisticRegression'        : LogisticRegression(solver='sag', multi_class='ovr'),
            'DecisionTreeClassifier'    : DecisionTreeClassifier()
        }
        self.ui.start.clicked.connect(self.get_clas)
        self.ui.train.clicked.connect(self.train)

        self.ui.pushButton_get_file.clicked.connect(self.download)

        self.ui.plainTextEdit_3.setPlainText(json.dumps(self.tegs_lens, ensure_ascii=False, indent=4))

    def download(self):
        fileName, _ = QFileDialog.getOpenFileName(self,
                                               ("Data csv"), os.getcwd(), ("Image Files (*.csv *.txt)"))
        print(fileName)
        set_data(fileName)
        self.redata()

    def get_clas(self):
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('cv.pkl', 'rb') as f:
            cv = pickle.load(f)

        text = text_cleaner(self.ui.lineEdit.text()).lower()
        data = parser.get_data_from_url_js(text)
        data = list(map(lambda x: x.lower().strip(), data))
        predict = model.predict(cv.transform(['\n'.join(data)]).toarray())
        print(predict)

        self.print_plane(self.ui.out_start, f'{self.ui.lineEdit.text()} -> {predict}')
        self.print_plane(self.ui.out_start, f'----------------------------------------------------')

    def train(self):
        try:
            print(self.ui.ch_cv.currentText())
            cv = self.cvs.get(str(self.ui.ch_cv.currentText()))
            model = self.models.get(str(self.ui.ch_model.currentText()))
            # model = LogisticRegression(solver='sag', multi_class='ovr')

            X_train, X_test, y_train, y_test = train_test_split(cv.fit_transform(self.x), self.y, test_size=0.1, random_state=41, shuffle=True)

            model.fit(X_train, y_train)

            count_success = 0
            predicted = model.predict(X_test)
            for n, i in enumerate(predicted):
                count_success += i == y_test[n]

            print(f'my score: {count_success / len(y_test):.4f}')
            print(f'accuracy_score: {accuracy_score(predicted, y_test)}')
            print(f'precision_score: {precision_score(predicted, y_test, average=None)}')
            print(f'recall_score: {recall_score(predicted, y_test, average=None)}')

            self.print_plane(self.ui.consol_train, f'my score: {count_success / len(y_test):.4f}')
            self.print_plane(self.ui.consol_train, f'accuracy_score: {accuracy_score(predicted, y_test)}')
            self.print_plane(self.ui.consol_train, f'precision_score: {precision_score(predicted, y_test, average=None)}')
            self.print_plane(self.ui.consol_train, f'recall_score: {recall_score(predicted, y_test, average=None)}')
            self.print_plane(self.ui.consol_train, f'-------------------------------------------------------------')

            with open('model.pkl', 'wb') as f:
                pickle.dump(model, f)
            with open('cv.pkl', 'wb') as f:
                pickle.dump(cv, f)
        except Exception as e:
            self.print_plane(self.ui.consol_train, f'error: {e}')
            self.print_plane(self.ui.consol_train, f'-------------------------------------------------------------')

    def add(self):
        link = self.ui.link_inp.text()
        tag = self.ui.get_class.currentText()
        self.print_plane(self.ui.data_plane_text_1, f'add {tag} ; {link}')
        add_data(tag, link)
        self.redata()

    def redata(self):
        self.ui.data_plane_text_2.setPlainText(get_data_str())
        for teg in tegs:
            self.tegs_lens[teg] = 0
            for file in os.listdir(f'{main_path}/{teg}'):
                texts = list(map(lambda x: x.lower().strip(), open(f'{main_path}/{teg}/{file}', 'r', encoding='utf8').readlines()))
                self.tegs_lens[teg] += len(texts)
                self.x.append('\n'.join(texts))
                self.y.append(teg)
        self.ui.plainTextEdit_3.setPlainText(json.dumps(self.tegs_lens, ensure_ascii=False, indent=4))

    def print_plane(self, widj, text):
        widj.setPlainText(widj.toPlainText() + text + '\n')

    def parsing(self):
        self.print_plane(self.ui.data_plane_text_1, 'start parsing...')
        print('start parsing...')
        with ml.Pool(count_gpu) as p:
            p.map(parser.get_data_from_url_soft, get_data())
        self.print_plane(self.ui.data_plane_text_1, 'finished parsing...')
        print('finished parsing...')

        self.redata()


if __name__ == "__main__":
    # print(get_data())
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())