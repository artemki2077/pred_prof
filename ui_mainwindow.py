# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QHBoxLayout,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setAutoFillBackground(False)
        self.train_tab = QWidget()
        self.train_tab.setObjectName(u"train_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.train_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ch_model = QComboBox(self.train_tab)
        self.ch_model.addItem("")
        self.ch_model.addItem("")
        self.ch_model.addItem("")
        self.ch_model.setObjectName(u"ch_model")

        self.verticalLayout_2.addWidget(self.ch_model)

        self.ch_cv = QComboBox(self.train_tab)
        self.ch_cv.addItem("")
        self.ch_cv.addItem("")
        self.ch_cv.setObjectName(u"ch_cv")

        self.verticalLayout_2.addWidget(self.ch_cv)

        self.train = QPushButton(self.train_tab)
        self.train.setObjectName(u"train")

        self.verticalLayout_2.addWidget(self.train)

        self.consol_train = QPlainTextEdit(self.train_tab)
        self.consol_train.setObjectName(u"consol_train")
        self.consol_train.setEnabled(True)
        self.consol_train.setMouseTracking(False)
        self.consol_train.setTabletTracking(False)
        self.consol_train.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.consol_train.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.consol_train.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.consol_train.setTabChangesFocus(False)
        self.consol_train.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.consol_train.setReadOnly(True)
        self.consol_train.setOverwriteMode(False)
        self.consol_train.setBackgroundVisible(False)
        self.consol_train.setCenterOnScroll(False)

        self.verticalLayout_2.addWidget(self.consol_train)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.plainTextEdit_3 = QPlainTextEdit(self.train_tab)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.plainTextEdit_3)

        self.tabWidget.addTab(self.train_tab, "")
        self.classer_tab = QWidget()
        self.classer_tab.setObjectName(u"classer_tab")
        self.horizontalLayout = QHBoxLayout(self.classer_tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.out_start = QPlainTextEdit(self.classer_tab)
        self.out_start.setObjectName(u"out_start")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_start.sizePolicy().hasHeightForWidth())
        self.out_start.setSizePolicy(sizePolicy)
        self.out_start.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.out_start.setReadOnly(True)

        self.horizontalLayout.addWidget(self.out_start)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lineEdit = QLineEdit(self.classer_tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit)

        self.start = QPushButton(self.classer_tab)
        self.start.setObjectName(u"start")

        self.verticalLayout.addWidget(self.start)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.classer_tab, "")
        self.data_tab = QWidget()
        self.data_tab.setObjectName(u"data_tab")
        self.horizontalLayout_5 = QHBoxLayout(self.data_tab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.link_inp = QLineEdit(self.data_tab)
        self.link_inp.setObjectName(u"link_inp")

        self.horizontalLayout_7.addWidget(self.link_inp)

        self.get_class = QComboBox(self.data_tab)
        self.get_class.addItem("")
        self.get_class.addItem("")
        self.get_class.addItem("")
        self.get_class.addItem("")
        self.get_class.addItem("")
        self.get_class.addItem("")
        self.get_class.addItem("")
        self.get_class.setObjectName(u"get_class")

        self.horizontalLayout_7.addWidget(self.get_class)

        self.add = QPushButton(self.data_tab)
        self.add.setObjectName(u"add")

        self.horizontalLayout_7.addWidget(self.add)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.pushButton_pars = QPushButton(self.data_tab)
        self.pushButton_pars.setObjectName(u"pushButton_pars")

        self.verticalLayout_4.addWidget(self.pushButton_pars)

        self.pushButton_get_file = QPushButton(self.data_tab)
        self.pushButton_get_file.setObjectName(u"pushButton_get_file")

        self.verticalLayout_4.addWidget(self.pushButton_get_file)

        self.data_plane_text_1 = QPlainTextEdit(self.data_tab)
        self.data_plane_text_1.setObjectName(u"data_plane_text_1")
        self.data_plane_text_1.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.data_plane_text_1)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.data_plane_text_2 = QPlainTextEdit(self.data_tab)
        self.data_plane_text_2.setObjectName(u"data_plane_text_2")
        self.data_plane_text_2.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.data_plane_text_2)

        self.tabWidget.addTab(self.data_tab, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0441\u0441\u0435\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0430\u0439\u0442\u043e\u0432", None))
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.ch_model.setItemText(0, QCoreApplication.translate("MainWindow", u"LogisticRegression", None))
        self.ch_model.setItemText(1, QCoreApplication.translate("MainWindow", u"DecisionTreeClassifier", None))
        self.ch_model.setItemText(2, QCoreApplication.translate("MainWindow", u"LinearDiscriminantAnalysis", None))

        self.ch_cv.setItemText(0, QCoreApplication.translate("MainWindow", u"CountVectorizer", None))
        self.ch_cv.setItemText(1, QCoreApplication.translate("MainWindow", u"TfidfVectorizer", None))

        self.train.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0431\u0443\u0447\u0438\u0442\u044c", None))
        self.consol_train.setPlainText("")
        self.consol_train.setPlaceholderText("")
        self.plainTextEdit_3.setPlainText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.train_tab), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0430\u0439\u0442", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043b\u0430\u0441\u0441\u0435\u0444\u0438\u0446\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u0430\u0439\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.classer_tab), QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0441\u0441\u0435\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.link_inp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0441\u0441\u044b\u043b\u043a\u0430", None))
        self.get_class.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0430\u0432\u0442\u043e", None))
        self.get_class.setItemText(1, QCoreApplication.translate("MainWindow", u"\u043a\u0443\u043b\u044c\u0442\u0443\u0440\u0430", None))
        self.get_class.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0441\u043f\u043e\u0440\u0442", None))
        self.get_class.setItemText(3, QCoreApplication.translate("MainWindow", u"\u044e\u043c\u043e\u0440", None))
        self.get_class.setItemText(4, QCoreApplication.translate("MainWindow", u"\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.get_class.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0431\u0438\u0437\u043d\u0435\u0441", None))
        self.get_class.setItemText(6, QCoreApplication.translate("MainWindow", u"\u043f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0438\u0435", None))

        self.add.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_pars.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0430\u0440\u0441\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButton_get_file.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_tab), QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

