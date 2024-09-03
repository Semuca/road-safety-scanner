# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)

from PySide6.QtWidgets import (QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QStackedWidget,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(841, 707)
        self.menuBar = QWidget(Dialog)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 841, 81))
        self.menuBar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.searchButton = QPushButton(self.menuBar)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(730, 0, 111, 71))
        self.searchButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color: rgb(56, 177, 224);\n"
"	font: 700 16pt \"Segoe UI\";\n"
"}")
        self.searchButton.setCheckable(True)
        self.searchButton.setAutoExclusive(True)
        self.setAIButton = QPushButton(self.menuBar)
        self.setAIButton.setObjectName(u"setAIButton")
        self.setAIButton.setGeometry(QRect(510, 0, 111, 71))
        self.setAIButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color: rgb(56, 177, 224);\n"
"	font: 700 16pt \"Segoe UI\";\n"
"}")
        self.setAIButton.setCheckable(True)
        self.setAIButton.setChecked(False)
        self.setAIButton.setAutoExclusive(True)
        self.uploadButton = QPushButton(self.menuBar)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setGeometry(QRect(620, 0, 111, 71))
        self.uploadButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color: rgb(56, 177, 224);\n"
"	font: 700 16pt \"Segoe UI\";\n"
"}")
        self.uploadButton.setCheckable(True)
        self.uploadButton.setAutoExclusive(True)
        self.title = QLabel(self.menuBar)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(350, 10, 101, 51))
        self.title.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";\n"
"font: 20pt \"Segoe UI\";")
        self.selectTabIndicator = QWidget(self.menuBar)
        self.selectTabIndicator.setObjectName(u"selectTabIndicator")
        self.selectTabIndicator.setGeometry(QRect(0, 69, 841, 20))
        self.selectTabIndicator.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(56, 177, 224);\n"
"	border: none; \n"
"}")
        self.myQStackedWidget = QStackedWidget(Dialog)
        self.myQStackedWidget.setObjectName(u"myQStackedWidget")
        self.myQStackedWidget.setGeometry(QRect(60, 110, 711, 531))
        self.myQStackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.setAIPage = QWidget()
        self.setAIPage.setObjectName(u"setAIPage")
        self.label = QLabel(self.setAIPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 121, 41))
        self.label.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.pushButton_5 = QPushButton(self.setAIPage)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(490, 140, 181, 161))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(56, 178, 224);\n"
"	font: 700 11pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	border: 4px solid rgb(56, 178, 224);\n"
"}")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)
        self.pushButton_6 = QPushButton(self.setAIPage)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(40, 140, 181, 161))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(56, 178, 224);\n"
"	font: 700 11pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	border: 4px solid rgb(56, 178, 224);\n"
"}\n"
"\n"
"")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)
        self.pushButton_7 = QPushButton(self.setAIPage)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(260, 140, 181, 161))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(56, 178, 224);\n"
"	font: 700 11pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	border: 4px solid rgb(56, 178, 224);\n"
"}")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)
        self.pushButton_9 = QPushButton(self.setAIPage)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(40, 340, 181, 161))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(56, 178, 224);\n"
"	font: 700 11pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	border: 4px solid rgb(56, 178, 224);\n"
"}")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)
        self.myQStackedWidget.addWidget(self.setAIPage)
        self.searchPage = QWidget()
        self.searchPage.setObjectName(u"searchPage")
        self.uploadJournal_2 = QWidget(self.searchPage)
        self.uploadJournal_2.setObjectName(u"uploadJournal_2")
        self.uploadJournal_2.setGeometry(QRect(20, 20, 671, 101))
        self.uploadJournal_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 20px;\n"
"}")
        self.label_12 = QLabel(self.uploadJournal_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 10, 201, 20))
        self.label_12.setStyleSheet(u"QLabel{\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt \"Segoe UI\"\n"
"	\n"
"}")
        self.lineEdit = QLineEdit(self.uploadJournal_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 40, 511, 41))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt \"Segoe UI\";\n"
"	padding-left: 10px;\n"
"}\n"
"")
        self.pushButton = QPushButton(self.uploadJournal_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 40, 101, 41))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	\n"
"	font: 8pt \"Segoe UI\";\n"
"	background-color: rgb(211, 211, 211);\n"
"}")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.results = QWidget(self.searchPage)
        self.results.setObjectName(u"results")
        self.results.setGeometry(QRect(20, 140, 671, 371))
        self.results.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 20px;\n"
"}")
        self.label_13 = QLabel(self.results)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 10, 111, 16))
        self.label_13.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt \"Segoe UI\"\n"
"	\n"
"}")
        self.myQStackedWidget.addWidget(self.searchPage)
        self.uploadJournalPage = QWidget()
        self.uploadJournalPage.setObjectName(u"uploadJournalPage")
        self.uploadJournal = QWidget(self.uploadJournalPage)
        self.uploadJournal.setObjectName(u"uploadJournal")
        self.uploadJournal.setGeometry(QRect(20, 20, 671, 101))
        self.uploadJournal.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 20px;\n"
"}")
        self.label_2 = QLabel(self.uploadJournal)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 10, 201, 20))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt \"Segoe UI\"\n"
"	\n"
"}")
        self.uploadedList = QWidget(self.uploadJournalPage)
        self.uploadedList.setObjectName(u"uploadedList")
        self.uploadedList.setGeometry(QRect(20, 140, 671, 371))
        self.uploadedList.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 20px;\n"
"}")
        self.label_3 = QLabel(self.uploadedList)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 10, 111, 16))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt \"Segoe UI\"\n"
"	\n"
"}")
        self.layoutWidget = QWidget(self.uploadedList)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 50, 621, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt \"Segoe UI\"\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt \"Segoe UI\"\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt \"Segoe UI\"\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.label_7)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt \"Segoe UI\"\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.label_4)

        self.myQStackedWidget.addWidget(self.uploadJournalPage)

        self.retranslateUi(Dialog)

        self.myQStackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.searchButton.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.setAIButton.setText(QCoreApplication.translate("Dialog", u"Set AI", None))
        self.uploadButton.setText(QCoreApplication.translate("Dialog", u"Upload", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Drive AI", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select your AI:", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Llama 3.1B", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Chat GPT", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Meta AI", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Llama 8B", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Search Journals", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Search for a journal...", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Download", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Results", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Upload your journals here", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Uploaded List:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Author", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Title", None))
    # retranslateUi

