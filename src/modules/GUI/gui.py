# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPlainTextEdit, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(843, 755)
        Dialog.setStyleSheet(u"\n"
"     * {\n"
"       font-family: \"Arial\";  /* Use Arial as the global font */\n"
"       font-size: 12pt;       /* Set a default font size */\n"
"       color: black;          /* Set font color to black */\n"
"     }\n"
"   ")
        self.menuBar = QWidget(Dialog)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 841, 81))
        self.menuBar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.searchButton = QPushButton(self.menuBar)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setEnabled(True)
        self.searchButton.setGeometry(QRect(400, 0, 112, 71))
        self.searchButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 14pt;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color: rgb(56, 177, 224);\n"
"	font: 700 16pt;\n"
"}")
        self.searchButton.setCheckable(True)
        self.searchButton.setChecked(True)
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
"	font: 700 14pt;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color: rgb(56, 177, 224);\n"
"	font: 700 16pt;\n"
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
"	font: 700 14pt;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color: rgb(56, 177, 224);\n"
"	font: 700 16pt;\n"
"}")
        self.uploadButton.setCheckable(True)
        self.uploadButton.setAutoExclusive(True)
        self.title = QLabel(self.menuBar)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 101, 51))
        self.title.setStyleSheet(u"font: 9pt;\n"
"font: 20pt;")
        self.selectTabIndicator = QWidget(self.menuBar)
        self.selectTabIndicator.setObjectName(u"selectTabIndicator")
        self.selectTabIndicator.setGeometry(QRect(0, 69, 841, 20))
        self.selectTabIndicator.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(56, 177, 224);\n"
"	border: none; \n"
"}")
        self.resultsButton = QPushButton(self.menuBar)
        self.resultsButton.setObjectName(u"resultsButton")
        self.resultsButton.setGeometry(QRect(730, 0, 111, 71))
        self.resultsButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 14pt;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color: rgb(56, 177, 224);\n"
"	font: 700 16pt;\n"
"}")
        self.resultsButton.setCheckable(True)
        self.resultsButton.setAutoExclusive(True)
        self.keysButton = QPushButton(self.menuBar)
        self.keysButton.setObjectName(u"keysButton")
        self.keysButton.setGeometry(QRect(290, 0, 111, 71))
        self.keysButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 14pt;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color: rgb(56, 177, 224);\n"
"	font: 700 16pt;\n"
"}")
        self.keysButton.setCheckable(True)
        self.keysButton.setChecked(False)
        self.keysButton.setAutoExclusive(True)
        self.searchButton.raise_()
        self.setAIButton.raise_()
        self.uploadButton.raise_()
        self.title.raise_()
        self.resultsButton.raise_()
        self.selectTabIndicator.raise_()
        self.keysButton.raise_()
        self.myQStackedWidget = QStackedWidget(Dialog)
        self.myQStackedWidget.setObjectName(u"myQStackedWidget")
        self.myQStackedWidget.setGeometry(QRect(60, 110, 711, 591))
        self.myQStackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.keysPage = QWidget()
        self.keysPage.setObjectName(u"keysPage")
        self.keysList = QWidget(self.keysPage)
        self.keysList.setObjectName(u"keysList")
        self.keysList.setGeometry(QRect(20, 30, 671, 491))
        self.keysList.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 20px;\n"
"}")
        self.keysListTag = QLabel(self.keysList)
        self.keysListTag.setObjectName(u"keysListTag")
        self.keysListTag.setGeometry(QRect(30, 10, 111, 16))
        self.keysListTag.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt\n"
"	\n"
"}")
        self.elsevierKeyEntry = QLineEdit(self.keysList)
        self.elsevierKeyEntry.setObjectName(u"elsevierKeyEntry")
        self.elsevierKeyEntry.setGeometry(QRect(170, 40, 481, 41))
        self.elsevierKeyEntry.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"}\n"
"")
        self.elsevierKeyLabel = QLabel(self.keysList)
        self.elsevierKeyLabel.setObjectName(u"elsevierKeyLabel")
        self.elsevierKeyLabel.setGeometry(QRect(40, 54, 121, 16))
        self.elsevierKeyLabel.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt\n"
"	\n"
"}")
        self.gptKeyLabel = QLabel(self.keysList)
        self.gptKeyLabel.setObjectName(u"gptKeyLabel")
        self.gptKeyLabel.setGeometry(QRect(40, 104, 121, 16))
        self.gptKeyLabel.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt\n"
"	\n"
"}")
        self.gptKeyEntry = QLineEdit(self.keysList)
        self.gptKeyEntry.setObjectName(u"gptKeyEntry")
        self.gptKeyEntry.setGeometry(QRect(170, 90, 481, 41))
        self.gptKeyEntry.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"}\n"
"")
        self.llama8bKeyEntry = QLineEdit(self.keysList)
        self.llama8bKeyEntry.setObjectName(u"llama8bKeyEntry")
        self.llama8bKeyEntry.setGeometry(QRect(170, 140, 481, 41))
        self.llama8bKeyEntry.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"}\n"
"")
        self.llama8bKeyLabel = QLabel(self.keysList)
        self.llama8bKeyLabel.setObjectName(u"llama8bKeyLabel")
        self.llama8bKeyLabel.setGeometry(QRect(40, 150, 121, 16))
        self.llama8bKeyLabel.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt\n"
"	\n"
"}")
        self.myQStackedWidget.addWidget(self.keysPage)
        self.searchPage = QWidget()
        self.searchPage.setObjectName(u"searchPage")
        self.setFiltersPage = QWidget(self.searchPage)
        self.setFiltersPage.setObjectName(u"setFiltersPage")
        self.setFiltersPage.setEnabled(True)
        self.setFiltersPage.setGeometry(QRect(50, 110, 611, 421))
        self.setFiltersPage.setStyleSheet(u"QWidget{\n"
"	border-radius: 20px;   \n"
"	\n"
"	background-color: rgb(218, 218, 218);\n"
"}")
        self.authorLabel = QLabel(self.setFiltersPage)
        self.authorLabel.setObjectName(u"authorLabel")
        self.authorLabel.setGeometry(QRect(60, 40, 61, 16))
        self.authorLabel.setStyleSheet(u"font: 700 12pt;")
        self.publishYearLabel = QLabel(self.setFiltersPage)
        self.publishYearLabel.setObjectName(u"publishYearLabel")
        self.publishYearLabel.setGeometry(QRect(410, 40, 101, 16))
        self.publishYearLabel.setStyleSheet(u"font: 700 12pt;")
        self.settingLabel = QLabel(self.setFiltersPage)
        self.settingLabel.setObjectName(u"settingLabel")
        self.settingLabel.setGeometry(QRect(60, 190, 61, 21))
        self.settingLabel.setStyleSheet(u"font: 700 12pt;")
        self.keyWordsLabel = QLabel(self.setFiltersPage)
        self.keyWordsLabel.setObjectName(u"keyWordsLabel")
        self.keyWordsLabel.setGeometry(QRect(60, 110, 81, 21))
        self.keyWordsLabel.setStyleSheet(u"font: 700 12pt;")
        self.authorName = QLineEdit(self.setFiltersPage)
        self.authorName.setObjectName(u"authorName")
        self.authorName.setGeometry(QRect(50, 60, 301, 41))
        self.authorName.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"	border-radius: 20px;  \n"
"}\n"
"")
        self.publishYearFrom = QDateEdit(self.setFiltersPage)
        self.publishYearFrom.setObjectName(u"publishYearFrom")
        self.publishYearFrom.setGeometry(QRect(460, 70, 110, 22))
        self.publishYearFrom.setStyleSheet(u"QDateEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.publishYearFrom.setDateTime(QDateTime(QDate(2013, 12, 26), QTime(0, 0, 0)))
        self.publishYearFrom.setDate(QDate(2013, 12, 31))
        self.keyWords = QLineEdit(self.setFiltersPage)
        self.keyWords.setObjectName(u"keyWords")
        self.keyWords.setGeometry(QRect(50, 140, 301, 41))
        self.keyWords.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"	border-radius: 20px;  \n"
"}\n"
"")
        self.setting = QLineEdit(self.setFiltersPage)
        self.setting.setObjectName(u"setting")
        self.setting.setGeometry(QRect(50, 220, 301, 41))
        self.setting.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"	border-radius: 20px;  \n"
"}\n"
"")
        self.setFiltersCloseButton = QPushButton(self.setFiltersPage)
        self.setFiltersCloseButton.setObjectName(u"setFiltersCloseButton")
        self.setFiltersCloseButton.setGeometry(QRect(550, 360, 41, 41))
        self.setFiltersCloseButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 10pt;\n"
"	border: none;\n"
"}\n"
"\n"
"/*\n"
"QPushButton:Hover{\n"
"	background-color: rgb(56, 177, 224);\n"
"}\n"
"*/")
        self.setFiltersCloseButton.setCheckable(True)
        self.setFiltersCloseButton.setChecked(False)
        self.setFiltersCloseButton.setAutoRepeat(False)
        self.setFiltersCloseButton.setAutoExclusive(True)
        self.publishYearFromLabel = QLabel(self.setFiltersPage)
        self.publishYearFromLabel.setObjectName(u"publishYearFromLabel")
        self.publishYearFromLabel.setGeometry(QRect(410, 71, 41, 20))
        self.publishYearFromLabel.setStyleSheet(u"font: 700 12pt;")
        self.publishYearTo = QDateEdit(self.setFiltersPage)
        self.publishYearTo.setObjectName(u"publishYearTo")
        self.publishYearTo.setGeometry(QRect(460, 109, 110, 22))
        self.publishYearTo.setStyleSheet(u"QDateEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.publishYearTo.setDateTime(QDateTime(QDate(2023, 12, 26), QTime(0, 0, 0)))
        self.publishYearTo.setDate(QDate(2023, 12, 31))
        self.publishYearToLabel = QLabel(self.setFiltersPage)
        self.publishYearToLabel.setObjectName(u"publishYearToLabel")
        self.publishYearToLabel.setGeometry(QRect(410, 110, 41, 20))
        self.publishYearToLabel.setStyleSheet(u"font: 700 12pt;")
        self.comboBox = QComboBox(self.setFiltersPage)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(410, 180, 151, 22))
        self.comboBox.setStyleSheet(u"background-color: rgb(184, 184, 184);")
        self.comboBox.setEditable(False)
        self.uploadJournal_2 = QWidget(self.searchPage)
        self.uploadJournal_2.setObjectName(u"uploadJournal_2")
        self.uploadJournal_2.setGeometry(QRect(20, 20, 671, 101))
        self.uploadJournal_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 20px;\n"
"}")
        self.searchJournalsLabel = QLabel(self.uploadJournal_2)
        self.searchJournalsLabel.setObjectName(u"searchJournalsLabel")
        self.searchJournalsLabel.setGeometry(QRect(20, 10, 201, 20))
        self.searchJournalsLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt\n"
"	\n"
"}")
        self.elsevierQuery = QLineEdit(self.uploadJournal_2)
        self.elsevierQuery.setObjectName(u"elsevierQuery")
        self.elsevierQuery.setGeometry(QRect(20, 40, 301, 41))
        self.elsevierQuery.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"}\n"
"")
        self.downloadElsevierJournals = QPushButton(self.uploadJournal_2)
        self.downloadElsevierJournals.setObjectName(u"downloadElsevierJournals")
        self.downloadElsevierJournals.setGeometry(QRect(550, 40, 101, 41))
        self.downloadElsevierJournals.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	\n"
"	font: 700 10pt;\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	\n"
"	font: 8pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"}")
        self.downloadElsevierJournals.setCheckable(False)
        self.downloadElsevierJournals.setChecked(False)
        self.downloadElsevierJournals.setAutoRepeat(False)
        self.downloadElsevierJournals.setAutoExclusive(False)
        self.searchElsevierJournals = QPushButton(self.uploadJournal_2)
        self.searchElsevierJournals.setObjectName(u"searchElsevierJournals")
        self.searchElsevierJournals.setGeometry(QRect(330, 40, 101, 41))
        self.searchElsevierJournals.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	\n"
"	font: 700 10pt;\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	\n"
"	font: 8pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"}")
        self.searchElsevierJournals.setCheckable(False)
        self.searchElsevierJournals.setChecked(False)
        self.searchElsevierJournals.setAutoRepeat(False)
        self.searchElsevierJournals.setAutoExclusive(False)
        self.setFiltersButton = QPushButton(self.uploadJournal_2)
        self.setFiltersButton.setObjectName(u"setFiltersButton")
        self.setFiltersButton.setGeometry(QRect(440, 40, 101, 41))
        self.setFiltersButton.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	\n"
"	font: 700 10pt;\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"")
        self.setFiltersButton.setCheckable(True)
        self.setFiltersButton.setChecked(False)
        self.setFiltersButton.setAutoRepeat(False)
        self.setFiltersButton.setAutoExclusive(False)
        self.results = QWidget(self.searchPage)
        self.results.setObjectName(u"results")
        self.results.setGeometry(QRect(20, 140, 671, 371))
        self.results.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 20px;\n"
"}")
        self.resultsLabel = QLabel(self.results)
        self.resultsLabel.setObjectName(u"resultsLabel")
        self.resultsLabel.setGeometry(QRect(30, 10, 111, 16))
        self.resultsLabel.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt\n"
"	\n"
"}")
        self.searchListTableWidget = QTableWidget(self.results)
        if (self.searchListTableWidget.columnCount() < 4):
            self.searchListTableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.searchListTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.searchListTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.searchListTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.searchListTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.searchListTableWidget.setObjectName(u"searchListTableWidget")
        self.searchListTableWidget.setGeometry(QRect(30, 50, 621, 301))
        self.searchListTableWidget.setStyleSheet(u"QHeaderView::section {\n"
"	color: rgb(113, 113, 113);\n"
"}\n"
"font: 700 12pt")
        self.myQStackedWidget.addWidget(self.searchPage)
        self.uploadJournal_2.raise_()
        self.results.raise_()
        self.setFiltersPage.raise_()
        self.setAIPage = QWidget()
        self.setAIPage.setObjectName(u"setAIPage")
        self.label = QLabel(self.setAIPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 121, 41))
        self.label.setStyleSheet(u"font: 700 11pt;")
        self.pushButton_ChatGpt = QPushButton(self.setAIPage)
        self.pushButton_ChatGpt.setObjectName(u"pushButton_ChatGpt")
        self.pushButton_ChatGpt.setGeometry(QRect(40, 140, 181, 161))
        self.pushButton_ChatGpt.setStyleSheet(u"QPushButton {\n"
"    border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(56, 178, 224);\n"
"	font: 700 11pt;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color: rgb(204, 255, 255);\n"
"	border: 4px solid rgb(56, 178, 224);\n"
"}")
        self.pushButton_ChatGpt.setCheckable(True)
        self.pushButton_ChatGpt.setAutoExclusive(True)
        self.pushButton_Llama8b = QPushButton(self.setAIPage)
        self.pushButton_Llama8b.setObjectName(u"pushButton_Llama8b")
        self.pushButton_Llama8b.setGeometry(QRect(260, 140, 181, 161))
        self.pushButton_Llama8b.setStyleSheet(u"QPushButton {\n"
"    border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(56, 178, 224);\n"
"	font: 700 11pt;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color: rgb(204, 255, 255);\n"
"	border: 4px solid rgb(56, 178, 224);\n"
"}")
        self.pushButton_Llama8b.setCheckable(True)
        self.pushButton_Llama8b.setAutoExclusive(True)
        self.pushButton_Llama405b = QPushButton(self.setAIPage)
        self.pushButton_Llama405b.setObjectName(u"pushButton_Llama405b")
        self.pushButton_Llama405b.setGeometry(QRect(490, 140, 181, 161))
        self.pushButton_Llama405b.setStyleSheet(u"QPushButton {\n"
"    border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(56, 178, 224);\n"
"	font: 700 11pt;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color: rgb(204, 255, 255);\n"
"	border: 4px solid rgb(56, 178, 224);\n"
"}")
        self.pushButton_Llama405b.setCheckable(True)
        self.pushButton_Llama405b.setAutoExclusive(True)
        self.pushButton_ClaudeSonnet = QPushButton(self.setAIPage)
        self.pushButton_ClaudeSonnet.setObjectName(u"pushButton_ClaudeSonnet")
        self.pushButton_ClaudeSonnet.setGeometry(QRect(40, 340, 181, 161))
        self.pushButton_ClaudeSonnet.setStyleSheet(u"QPushButton {\n"
"    border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(56, 178, 224);\n"
"	font: 700 11pt;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	background-color: rgb(204, 255, 255);\n"
"	border: 4px solid rgb(56, 178, 224);\n"
"}")
        self.pushButton_ClaudeSonnet.setCheckable(True)
        self.pushButton_ClaudeSonnet.setAutoExclusive(True)
        self.myQStackedWidget.addWidget(self.setAIPage)
        self.uploadJournalPage = QWidget()
        self.uploadJournalPage.setObjectName(u"uploadJournalPage")
        self.uploadJournal = QWidget(self.uploadJournalPage)
        self.uploadJournal.setObjectName(u"uploadJournal")
        self.uploadJournal.setGeometry(QRect(20, 20, 671, 101))
        self.uploadJournal.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 20px;\n"
"}")
        self.uploadJournalLabel = QLabel(self.uploadJournal)
        self.uploadJournalLabel.setObjectName(u"uploadJournalLabel")
        self.uploadJournalLabel.setGeometry(QRect(250, 10, 201, 20))
        self.uploadJournalLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt\n"
"	\n"
"}")
        self.uploadJournalButton = QPushButton(self.uploadJournal)
        self.uploadJournalButton.setObjectName(u"uploadJournalButton")
        self.uploadJournalButton.setGeometry(QRect(280, 40, 101, 41))
        self.uploadJournalButton.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	\n"
"	font: 700 10pt;\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"")
        self.uploadedList = QWidget(self.uploadJournalPage)
        self.uploadedList.setObjectName(u"uploadedList")
        self.uploadedList.setGeometry(QRect(20, 140, 671, 371))
        self.uploadedList.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 20px;\n"
"}")
        self.uploadedListLabel = QLabel(self.uploadedList)
        self.uploadedListLabel.setObjectName(u"uploadedListLabel")
        self.uploadedListLabel.setGeometry(QRect(30, 10, 111, 16))
        self.uploadedListLabel.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt\n"
"	\n"
"}")
        self.journalListTableWidget = QTableWidget(self.uploadedList)
        if (self.journalListTableWidget.columnCount() < 4):
            self.journalListTableWidget.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.journalListTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.journalListTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.journalListTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.journalListTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.journalListTableWidget.setObjectName(u"journalListTableWidget")
        self.journalListTableWidget.setGeometry(QRect(30, 50, 621, 301))
        self.journalListTableWidget.setStyleSheet(u"QHeaderView::section {\n"
"	color: rgb(113, 113, 113);\n"
"}\n"
"font: 700 12pt")
        self.myQStackedWidget.addWidget(self.uploadJournalPage)
        self.resultsPage = QWidget()
        self.resultsPage.setObjectName(u"resultsPage")
        self.addColumnPage = QWidget(self.resultsPage)
        self.addColumnPage.setObjectName(u"addColumnPage")
        self.addColumnPage.setEnabled(True)
        self.addColumnPage.setGeometry(QRect(50, 110, 611, 421))
        self.addColumnPage.setStyleSheet(u"QWidget{\n"
"	border-radius: 20px;   \n"
"	\n"
"	background-color: rgb(218, 218, 218);\n"
"}")
        self.addColumnCancelButton = QPushButton(self.addColumnPage)
        self.addColumnCancelButton.setObjectName(u"addColumnCancelButton")
        self.addColumnCancelButton.setGeometry(QRect(120, 360, 91, 41))
        self.addColumnCancelButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 10pt;\n"
"	border: none;\n"
"}\n"
"\n"
"/*\n"
"QPushButton:Hover{\n"
"	background-color: rgb(56, 177, 224);\n"
"}\n"
"*/")
        self.addColumnCancelButton.setCheckable(True)
        self.addColumnCancelButton.setChecked(False)
        self.addColumnCancelButton.setAutoRepeat(False)
        self.addColumnCancelButton.setAutoExclusive(True)
        self.addColumnApplyButton = QPushButton(self.addColumnPage)
        self.addColumnApplyButton.setObjectName(u"addColumnApplyButton")
        self.addColumnApplyButton.setGeometry(QRect(20, 360, 91, 41))
        self.addColumnApplyButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 10pt;\n"
"	border: none;\n"
"}\n"
"\n"
"/*\n"
"QPushButton:Hover{\n"
"	background-color: rgb(56, 177, 224);\n"
"}\n"
"*/")
        self.addColumnApplyButton.setCheckable(True)
        self.addColumnApplyButton.setChecked(False)
        self.addColumnApplyButton.setAutoRepeat(False)
        self.addColumnApplyButton.setAutoExclusive(True)
        self.addColumnLabel = QLabel(self.addColumnPage)
        self.addColumnLabel.setObjectName(u"addColumnLabel")
        self.addColumnLabel.setGeometry(QRect(30, 20, 111, 16))
        self.addColumnLabel.setStyleSheet(u"font: 700 12pt;")
        self.addColumnQueryText = QPlainTextEdit(self.addColumnPage)
        self.addColumnQueryText.setObjectName(u"addColumnQueryText")
        self.addColumnQueryText.setGeometry(QRect(50, 160, 511, 181))
        self.addColumnQueryText.viewport().setProperty("cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.addColumnQueryText.setMouseTracking(True)
        self.addColumnQueryText.setStyleSheet(u"QPlainTextEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"	border-radius: 20px;  \n"
"}\n"
"")
        self.addColumnHeaderLabel = QLabel(self.addColumnPage)
        self.addColumnHeaderLabel.setObjectName(u"addColumnHeaderLabel")
        self.addColumnHeaderLabel.setGeometry(QRect(40, 50, 111, 16))
        self.addColumnHeaderLabel.setStyleSheet(u"font: 700 12pt;")
        self.addColumnHeaderEntry = QLineEdit(self.addColumnPage)
        self.addColumnHeaderEntry.setObjectName(u"addColumnHeaderEntry")
        self.addColumnHeaderEntry.setGeometry(QRect(50, 80, 511, 41))
        self.addColumnHeaderEntry.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"}\n"
"")
        self.addColumnQueryLabel = QLabel(self.addColumnPage)
        self.addColumnQueryLabel.setObjectName(u"addColumnQueryLabel")
        self.addColumnQueryLabel.setGeometry(QRect(40, 130, 111, 16))
        self.addColumnQueryLabel.setStyleSheet(u"font: 700 12pt;")
        self.editColumnPage = QWidget(self.resultsPage)
        self.editColumnPage.setObjectName(u"editColumnPage")
        self.editColumnPage.setEnabled(True)
        self.editColumnPage.setGeometry(QRect(50, 110, 611, 421))
        self.editColumnPage.setStyleSheet(u"QWidget{\n"
"	border-radius: 20px;   \n"
"	\n"
"	background-color: rgb(218, 218, 218);\n"
"}")
        self.editColumnLabel = QLabel(self.editColumnPage)
        self.editColumnLabel.setObjectName(u"editColumnLabel")
        self.editColumnLabel.setGeometry(QRect(30, 20, 111, 16))
        self.editColumnLabel.setStyleSheet(u"font: 700 12pt;")
        self.editColumnCancelButton = QPushButton(self.editColumnPage)
        self.editColumnCancelButton.setObjectName(u"editColumnCancelButton")
        self.editColumnCancelButton.setGeometry(QRect(120, 360, 91, 41))
        self.editColumnCancelButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 10pt;\n"
"	border: none;\n"
"}\n"
"\n"
"/*\n"
"QPushButton:Hover{\n"
"	background-color: rgb(56, 177, 224);\n"
"}\n"
"*/")
        self.editColumnCancelButton.setCheckable(True)
        self.editColumnCancelButton.setChecked(False)
        self.editColumnCancelButton.setAutoRepeat(False)
        self.editColumnCancelButton.setAutoExclusive(True)
        self.editColumnQueryText = QPlainTextEdit(self.editColumnPage)
        self.editColumnQueryText.setObjectName(u"editColumnQueryText")
        self.editColumnQueryText.setGeometry(QRect(50, 160, 511, 181))
        self.editColumnQueryText.viewport().setProperty("cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.editColumnQueryText.setMouseTracking(True)
        self.editColumnQueryText.setStyleSheet(u"QPlainTextEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"	border-radius: 20px;  \n"
"}\n"
"")
        self.editColumnApplyButton = QPushButton(self.editColumnPage)
        self.editColumnApplyButton.setObjectName(u"editColumnApplyButton")
        self.editColumnApplyButton.setGeometry(QRect(20, 360, 91, 41))
        self.editColumnApplyButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 10pt;\n"
"	border: none;\n"
"}\n"
"\n"
"/*\n"
"QPushButton:Hover{\n"
"	background-color: rgb(56, 177, 224);\n"
"}\n"
"*/")
        self.editColumnApplyButton.setCheckable(True)
        self.editColumnApplyButton.setChecked(False)
        self.editColumnApplyButton.setAutoRepeat(False)
        self.editColumnApplyButton.setAutoExclusive(True)
        self.deleteColumnButton = QPushButton(self.editColumnPage)
        self.deleteColumnButton.setObjectName(u"deleteColumnButton")
        self.deleteColumnButton.setGeometry(QRect(500, 360, 91, 41))
        self.deleteColumnButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 10pt;\n"
"	border: none;\n"
"}\n"
"\n"
"/*\n"
"QPushButton:Hover{\n"
"	background-color: rgb(56, 177, 224);\n"
"}\n"
"*/")
        self.deleteColumnButton.setCheckable(True)
        self.deleteColumnButton.setChecked(False)
        self.deleteColumnButton.setAutoRepeat(False)
        self.deleteColumnButton.setAutoExclusive(True)
        self.editColumnHeaderEntry = QLineEdit(self.editColumnPage)
        self.editColumnHeaderEntry.setObjectName(u"editColumnHeaderEntry")
        self.editColumnHeaderEntry.setGeometry(QRect(50, 80, 511, 41))
        self.editColumnHeaderEntry.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"}\n"
"")
        self.editColumnHeaderLabel = QLabel(self.editColumnPage)
        self.editColumnHeaderLabel.setObjectName(u"editColumnHeaderLabel")
        self.editColumnHeaderLabel.setGeometry(QRect(40, 50, 111, 16))
        self.editColumnHeaderLabel.setStyleSheet(u"font: 700 12pt;")
        self.editColumnQueryLabel = QLabel(self.editColumnPage)
        self.editColumnQueryLabel.setObjectName(u"editColumnQueryLabel")
        self.editColumnQueryLabel.setGeometry(QRect(40, 130, 111, 16))
        self.editColumnQueryLabel.setStyleSheet(u"font: 700 12pt;")
        self.setFiltersOption = QWidget(self.resultsPage)
        self.setFiltersOption.setObjectName(u"setFiltersOption")
        self.setFiltersOption.setGeometry(QRect(20, 20, 671, 101))
        self.setFiltersOption.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 20px;\n"
"}")
        self.searchResultsTag = QLabel(self.setFiltersOption)
        self.searchResultsTag.setObjectName(u"searchResultsTag")
        self.searchResultsTag.setGeometry(QRect(20, 10, 211, 20))
        self.searchResultsTag.setStyleSheet(u"QLabel{\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt\n"
"	\n"
"}")
        self.processJournalsButton = QPushButton(self.setFiltersOption)
        self.processJournalsButton.setObjectName(u"processJournalsButton")
        self.processJournalsButton.setGeometry(QRect(440, 40, 101, 41))
        self.processJournalsButton.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	\n"
"	font: 700 10pt;\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	\n"
"	font: 8pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"}")
        self.processJournalsButton.setCheckable(False)
        self.processJournalsButton.setChecked(False)
        self.processJournalsButton.setAutoRepeat(False)
        self.processJournalsButton.setAutoExclusive(False)
        self.addColumnButton = QPushButton(self.setFiltersOption)
        self.addColumnButton.setObjectName(u"addColumnButton")
        self.addColumnButton.setGeometry(QRect(180, 40, 101, 41))
        self.addColumnButton.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	\n"
"	font: 700 10pt;\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	\n"
"	font: 8pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"}")
        self.addColumnButton.setCheckable(False)
        self.addColumnButton.setChecked(False)
        self.addColumnButton.setAutoRepeat(False)
        self.addColumnButton.setAutoExclusive(False)
        self.exportResultsButton = QPushButton(self.setFiltersOption)
        self.exportResultsButton.setObjectName(u"exportResultsButton")
        self.exportResultsButton.setGeometry(QRect(400, 40, 101, 41))
        self.exportResultsButton.setStyleSheet(u"QPushButton{\n"
"            color:white;\n"
"            font: 700 10pt;\n"
"            background-color: rgb(8, 144, 196);\n"
"       }\n"
"\n"
"       QPushButton:Checked{\n"
"            font: 8pt;\n"
"            background-color: rgb(211, 211, 211);\n"
"       }")
        self.exportResultsButton.setCheckable(False)
        self.exportResultsButton.setChecked(False)
        self.exportResultsButton.setAutoRepeat(False)
        self.exportResultsButton.setAutoExclusive(False)
        self.resultsList = QWidget(self.resultsPage)
        self.resultsList.setObjectName(u"resultsList")
        self.resultsList.setGeometry(QRect(20, 140, 671, 371))
        self.resultsList.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 20px;\n"
"}")
        self.resultsListTag = QLabel(self.resultsList)
        self.resultsListTag.setObjectName(u"resultsListTag")
        self.resultsListTag.setGeometry(QRect(30, 10, 111, 16))
        self.resultsListTag.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(113, 113, 113);\n"
"	\n"
"	font: 700 12pt\n"
"	\n"
"}")
        self.resultsListTableWidget = QTableWidget(self.resultsList)
        if (self.resultsListTableWidget.columnCount() < 1):
            self.resultsListTableWidget.setColumnCount(1)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.resultsListTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        self.resultsListTableWidget.setObjectName(u"resultsListTableWidget")
        self.resultsListTableWidget.setGeometry(QRect(30, 50, 621, 301))
        self.resultsListTableWidget.setStyleSheet(u"QHeaderView::section {\n"
"	color: rgb(113, 113, 113);\n"
"}\n"
"font: 700 12pt")
        self.myQStackedWidget.addWidget(self.resultsPage)
        self.setFiltersOption.raise_()
        self.resultsList.raise_()
        self.addColumnPage.raise_()
        self.editColumnPage.raise_()
        self.backButton = QPushButton(Dialog)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setEnabled(True)
        self.backButton.setGeometry(QRect(70, 650, 100, 40))
        self.backButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(56, 178, 224);\n"
"}\n"
"/*\n"
"QPushButton:Hover{\n"
"	background-color: rgb(204, 255, 255);\n"
"	border: 3px solid rgb(56, 178, 224);\n"
"}\n"
"*/")
        self.nextButton = QPushButton(Dialog)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(660, 650, 100, 40))
        self.nextButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(56, 178, 224);\n"
"}\n"
"/*\n"
"QPushButton:Hover{\n"
"	background-color: rgb(204, 255, 255);\n"
"	border: 3px solid rgb(56, 178, 224);\n"
"}\n"
"*/")
        self.editSetPage = QWidget(Dialog)
        self.editSetPage.setObjectName(u"editSetPage")
        self.editSetPage.setEnabled(True)
        self.editSetPage.setGeometry(QRect(120, 230, 591, 401))
        self.editSetPage.setStyleSheet(u"QWidget{\n"
"	border-radius: 20px;   \n"
"	\n"
"	\n"
"	background-color: rgb(161, 161, 161);\n"
"}")
        self.editYourSetTitle = QLabel(self.editSetPage)
        self.editYourSetTitle.setObjectName(u"editYourSetTitle")
        self.editYourSetTitle.setGeometry(QRect(220, 10, 181, 41))
        self.editYourSetTitle.setStyleSheet(u"font: 700 16pt;")
        self.editSubsetText = QLineEdit(self.editSetPage)
        self.editSubsetText.setObjectName(u"editSubsetText")
        self.editSubsetText.setGeometry(QRect(50, 100, 301, 31))
        self.editSubsetText.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"	border-radius: 12px;  \n"
"}\n"
"")
        self.editSubsetText.setReadOnly(False)
        self.editSubsetSaveButton = QPushButton(self.editSetPage)
        self.editSubsetSaveButton.setObjectName(u"editSubsetSaveButton")
        self.editSubsetSaveButton.setGeometry(QRect(520, 340, 41, 41))
        self.editSubsetSaveButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 10pt;\n"
"	border: none;\n"
"}\n"
"\n"
"/*\n"
"QPushButton:Hover{\n"
"	background-color: rgb(56, 177, 224);\n"
"}\n"
"*/")
        self.editSubsetSaveButton.setCheckable(True)
        self.editSubsetSaveButton.setChecked(False)
        self.editSubsetSaveButton.setAutoRepeat(False)
        self.editSubsetSaveButton.setAutoExclusive(True)
        self.editSubsetList = QListWidget(self.editSetPage)
        self.editSubsetList.setObjectName(u"editSubsetList")
        self.editSubsetList.setGeometry(QRect(50, 140, 431, 181))
        self.editSubsetList.setStyleSheet(u"QListWidget {\n"
"	\n"
"	\n"
"	font: 9pt \"Arial\";\n"
"    background-color: rgb(225, 225, 225);\n"
"    border-radius: 12px; \n"
"}\n"
"\n"
"\n"
"")
        self.editTitle = QLineEdit(self.editSetPage)
        self.editTitle.setObjectName(u"editTitle")
        self.editTitle.setGeometry(QRect(50, 60, 121, 31))
        self.editTitle.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"	border-radius: 12px;  \n"
"}\n"
"")
        self.setsPage = QWidget(Dialog)
        self.setsPage.setObjectName(u"setsPage")
        self.setsPage.setEnabled(True)
        self.setsPage.setGeometry(QRect(110, 220, 611, 421))
        self.setsPage.setStyleSheet(u"QWidget{\n"
"	border-radius: 20px;   \n"
"	\n"
"	background-color: rgb(218, 218, 218);\n"
"}")
        self.editYourSetsTitle = QLabel(self.setsPage)
        self.editYourSetsTitle.setObjectName(u"editYourSetsTitle")
        self.editYourSetsTitle.setGeometry(QRect(200, 20, 191, 41))
        self.editYourSetsTitle.setStyleSheet(u"font: 700 16pt;")
        self.saveSets = QPushButton(self.setsPage)
        self.saveSets.setObjectName(u"saveSets")
        self.saveSets.setGeometry(QRect(550, 360, 41, 41))
        self.saveSets.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 10pt;\n"
"	border: none;\n"
"}\n"
"\n"
"/*\n"
"QPushButton:Hover{\n"
"	background-color: rgb(56, 177, 224);\n"
"}\n"
"*/")
        self.saveSets.setCheckable(True)
        self.saveSets.setChecked(False)
        self.saveSets.setAutoRepeat(False)
        self.saveSets.setAutoExclusive(True)
        self.allJournalSets = QListWidget(self.setsPage)
        self.allJournalSets.setObjectName(u"allJournalSets")
        self.allJournalSets.setGeometry(QRect(60, 100, 501, 221))
        self.allJournalSets.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.addJournalButton = QPushButton(self.setsPage)
        self.addJournalButton.setObjectName(u"addJournalButton")
        self.addJournalButton.setGeometry(QRect(70, 330, 111, 24))
        self.addJournalButton.setStyleSheet(u"QPushButton{\n"
"	color:black;\n"
"	\n"
"	font: 700 10pt;\n"
"	background-color: rgb(161, 161, 161);\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	\n"
"	font: 8pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"}")
        self.addJournalButton.setCheckable(True)
        self.addNewSetWidget = QWidget(Dialog)
        self.addNewSetWidget.setObjectName(u"addNewSetWidget")
        self.addNewSetWidget.setEnabled(True)
        self.addNewSetWidget.setGeometry(QRect(120, 230, 591, 401))
        self.addNewSetWidget.setStyleSheet(u"QWidget{\n"
"	border-radius: 20px;   \n"
"	\n"
"	\n"
"	background-color: rgb(161, 161, 161);\n"
"}")
        self.addNewSetTitle = QLabel(self.addNewSetWidget)
        self.addNewSetTitle.setObjectName(u"addNewSetTitle")
        self.addNewSetTitle.setGeometry(QRect(220, 10, 181, 41))
        self.addNewSetTitle.setStyleSheet(u"font: 700 16pt;")
        self.newSubsetText = QLineEdit(self.addNewSetWidget)
        self.newSubsetText.setObjectName(u"newSubsetText")
        self.newSubsetText.setGeometry(QRect(50, 100, 301, 31))
        self.newSubsetText.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"	border-radius: 12px;  \n"
"}\n"
"")
        self.addSetOKButton = QPushButton(self.addNewSetWidget)
        self.addSetOKButton.setObjectName(u"addSetOKButton")
        self.addSetOKButton.setGeometry(QRect(520, 340, 41, 41))
        self.addSetOKButton.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(8, 144, 196);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 700 10pt;\n"
"	border: none;\n"
"}\n"
"\n"
"/*\n"
"QPushButton:Hover{\n"
"	background-color: rgb(56, 177, 224);\n"
"}\n"
"*/")
        self.addSetOKButton.setCheckable(True)
        self.addSetOKButton.setChecked(False)
        self.addSetOKButton.setAutoRepeat(False)
        self.addSetOKButton.setAutoExclusive(True)
        self.subsetList = QListWidget(self.addNewSetWidget)
        self.subsetList.setObjectName(u"subsetList")
        self.subsetList.setGeometry(QRect(50, 140, 431, 181))
        self.subsetList.setStyleSheet(u"QListWidget {\n"
"	\n"
"	\n"
"	font: 9pt \"Arial\";\n"
"    background-color: rgb(225, 225, 225);\n"
"    border-radius: 12px; \n"
"}\n"
"\n"
"\n"
"")
        self.newSetTitle = QLineEdit(self.addNewSetWidget)
        self.newSetTitle.setObjectName(u"newSetTitle")
        self.newSetTitle.setGeometry(QRect(50, 60, 121, 31))
        self.newSetTitle.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"	border-radius: 12px;  \n"
"}\n"
"")
        self.menuBar.raise_()
        self.myQStackedWidget.raise_()
        self.backButton.raise_()
        self.nextButton.raise_()
        self.setsPage.raise_()
        self.addNewSetWidget.raise_()
        self.editSetPage.raise_()

        self.retranslateUi(Dialog)

        self.myQStackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.searchButton.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.setAIButton.setText(QCoreApplication.translate("Dialog", u"Set AI", None))
        self.uploadButton.setText(QCoreApplication.translate("Dialog", u"Upload", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Drive AI", None))
        self.resultsButton.setText(QCoreApplication.translate("Dialog", u"Results", None))
        self.keysButton.setText(QCoreApplication.translate("Dialog", u"Keys", None))
        self.keysListTag.setText(QCoreApplication.translate("Dialog", u"Keys", None))
        self.elsevierKeyEntry.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter key here...", None))
        self.elsevierKeyLabel.setText(QCoreApplication.translate("Dialog", u"ELSEVIER_API_KEY", None))
        self.gptKeyLabel.setText(QCoreApplication.translate("Dialog", u"GPT_API_KEY", None))
        self.gptKeyEntry.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter key here...", None))
        self.llama8bKeyEntry.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter key here...", None))
        self.llama8bKeyLabel.setText(QCoreApplication.translate("Dialog", u"LLAMA8B_API_KEY", None))
        self.authorLabel.setText(QCoreApplication.translate("Dialog", u"Author:", None))
        self.publishYearLabel.setText(QCoreApplication.translate("Dialog", u"Publish Year:", None))
        self.settingLabel.setText(QCoreApplication.translate("Dialog", u"Setting", None))
        self.keyWordsLabel.setText(QCoreApplication.translate("Dialog", u"Key Words", None))
        self.authorName.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Author's Name...", None))
        self.publishYearFrom.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy", None))
        self.keyWords.setText("")
        self.keyWords.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter key words separated by \",\"", None))
        self.setting.setText("")
        self.setting.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter a country", None))
        self.setFiltersCloseButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.publishYearFromLabel.setText(QCoreApplication.translate("Dialog", u"From", None))
        self.publishYearTo.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy", None))
        self.publishYearToLabel.setText(QCoreApplication.translate("Dialog", u"To", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select Your Set", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Set 1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Add a new Set", None))

        self.searchJournalsLabel.setText(QCoreApplication.translate("Dialog", u"Search Journals", None))
        self.elsevierQuery.setPlaceholderText(QCoreApplication.translate("Dialog", u"Search for a journal...", None))
        self.downloadElsevierJournals.setText(QCoreApplication.translate("Dialog", u"Download", None))
        self.searchElsevierJournals.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.setFiltersButton.setText(QCoreApplication.translate("Dialog", u"Set Filters", None))
        self.resultsLabel.setText(QCoreApplication.translate("Dialog", u"Results", None))
        ___qtablewidgetitem = self.searchListTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"AUTHOR", None));
        ___qtablewidgetitem1 = self.searchListTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"TITLE", None));
        ___qtablewidgetitem2 = self.searchListTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"TYPE", None));
        ___qtablewidgetitem3 = self.searchListTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"DATE", None));
        self.label.setText(QCoreApplication.translate("Dialog", u"Select your AI:", None))
        self.pushButton_ChatGpt.setText(QCoreApplication.translate("Dialog", u"GPT-4o mini", None))
        self.pushButton_Llama8b.setText(QCoreApplication.translate("Dialog", u"Llama 3.1-8B", None))
        self.pushButton_Llama405b.setText(QCoreApplication.translate("Dialog", u"Llama 3.1-405B", None))
        self.pushButton_ClaudeSonnet.setText(QCoreApplication.translate("Dialog", u"Claude 3.5 Sonnet", None))
        self.uploadJournalLabel.setText(QCoreApplication.translate("Dialog", u"Upload your journals here", None))
        self.uploadJournalButton.setText(QCoreApplication.translate("Dialog", u"Upload", None))
        self.uploadedListLabel.setText(QCoreApplication.translate("Dialog", u"Uploaded List:", None))
        ___qtablewidgetitem4 = self.journalListTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"AUTHOR", None));
        ___qtablewidgetitem5 = self.journalListTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"TITLE", None));
        ___qtablewidgetitem6 = self.journalListTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"TYPE", None));
        ___qtablewidgetitem7 = self.journalListTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"DATE", None));
        self.addColumnCancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.addColumnApplyButton.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.addColumnLabel.setText(QCoreApplication.translate("Dialog", u"Add query column", None))
        self.addColumnQueryText.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter prompt here...", None))
        self.addColumnHeaderLabel.setText(QCoreApplication.translate("Dialog", u"Header", None))
        self.addColumnHeaderEntry.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter key here...", None))
        self.addColumnQueryLabel.setText(QCoreApplication.translate("Dialog", u"Query", None))
        self.editColumnLabel.setText(QCoreApplication.translate("Dialog", u"Edit query column", None))
        self.editColumnCancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.editColumnQueryText.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter prompt here...", None))
        self.editColumnApplyButton.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.deleteColumnButton.setText(QCoreApplication.translate("Dialog", u"Delete column", None))
        self.editColumnHeaderEntry.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter key here...", None))
        self.editColumnHeaderLabel.setText(QCoreApplication.translate("Dialog", u"Header", None))
        self.editColumnQueryLabel.setText(QCoreApplication.translate("Dialog", u"Query", None))
        self.searchResultsTag.setText(QCoreApplication.translate("Dialog", u"Process articles", None))
        self.processJournalsButton.setText(QCoreApplication.translate("Dialog", u"Process", None))
        self.addColumnButton.setText(QCoreApplication.translate("Dialog", u"Add column", None))
        self.exportResultsButton.setText(QCoreApplication.translate("Dialog", u"Download", None))
        self.resultsListTag.setText(QCoreApplication.translate("Dialog", u"Results", None))
        ___qtablewidgetitem8 = self.resultsListTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"PUBLICATION", None));
        self.backButton.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.nextButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
        self.editYourSetTitle.setText(QCoreApplication.translate("Dialog", u"Edit your Set", None))
        self.editSubsetText.setText("")
        self.editSubsetText.setPlaceholderText(QCoreApplication.translate("Dialog", u"Add a new subset", None))
        self.editSubsetSaveButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.editTitle.setText("")
        self.editTitle.setPlaceholderText(QCoreApplication.translate("Dialog", u"Set Name", None))
        self.editYourSetsTitle.setText(QCoreApplication.translate("Dialog", u"Your Current Sets", None))
        self.saveSets.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.addJournalButton.setText(QCoreApplication.translate("Dialog", u"Add a New Set", None))
        self.addNewSetTitle.setText(QCoreApplication.translate("Dialog", u"Add a New Set", None))
        self.newSubsetText.setText("")
        self.newSubsetText.setPlaceholderText(QCoreApplication.translate("Dialog", u"Add a new subset", None))
        self.addSetOKButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.newSetTitle.setText("")
        self.newSetTitle.setPlaceholderText(QCoreApplication.translate("Dialog", u"Set Name", None))
    # retranslateUi

