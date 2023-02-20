import json
import os
import parser
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from pprint import pprint
from Stemmer import Stemmer
from sklearn.metrics import accuracy_score, recall_score, precision_score

from sklearn.model_selection import train_test_split
import re

main_path = 'data'
tegs = ['авто', 'культура', 'спорт', 'юмор', 'образование', 'бизнес', 'путешествие']


def text_cleaner(text):
    text = text.lower()  # приведение в lowercase
    stemmer = Stemmer('russian')
    text = ' '.join(stemmer.stemWords(text.split()))
    text = re.sub(r'\b\d+\b', ' digit ', text)  # замена цифр
    return text


def load_spec_words():
    data = []
    json_data = json.load(open('data.json', 'r', encoding='utf8'))
    for tag in json_data:
        for i in json_data[tag][:50]:
            res = i.split(' ')
            if len(res) >= 2:
                print(f'{len(res)} -> {res}')
            data.extend(list(map(lambda x: text_cleaner(x), res)))
    return list(set(data))


x = []
y = []
tegs_lens = {}
for teg in tegs:
    tegs_lens[teg] = 0
    for file in os.listdir(f'{main_path}/{teg}'):
        texts = list(map(lambda x: x.lower().strip(), open(f'{main_path}/{teg}/{file}', 'r', encoding='utf8').readlines()))
        tegs_lens[teg] += len(texts)
        x.append('\n'.join(texts))
        y.append(teg)



pprint(tegs_lens)
cv = CountVectorizer()
# cv = TfidfVectorizer()
model = LogisticRegression(solver='sag', multi_class='ovr')
# cv.fit(x)

X_train, X_test, y_train, y_test = train_test_split(cv.fit_transform(x), y, test_size=0.1, random_state=41, shuffle=True)
model.fit(X_train, y_train)

count_success = 0
predicted = model.predict(X_test)
for n, i in enumerate(predicted):
    count_success += i == y_test[n]

print(f'my score: {count_success / len(y_test):.4f}')
print(f'accuracy_score: {accuracy_score(predicted, y_test)}')
print(f'precision_score: {precision_score(predicted, y_test, average=None)}')
print(f'recall_score: {recall_score(predicted, y_test, average=None)}')
while 1:
    text = text_cleaner(input()).lower()
    data = parser.get_data_from_url_js(text)
    data = list(map(lambda x: x.lower().strip(), data))
    print(model.predict(cv.transform(['\n'.join(data)]).toarray()))