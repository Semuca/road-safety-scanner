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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(861, 730)
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
        self.title.setGeometry(QRect(220, 10, 101, 51))
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
        self.searchButton.raise_()
        self.setAIButton.raise_()
        self.uploadButton.raise_()
        self.title.raise_()
        self.resultsButton.raise_()
        self.selectTabIndicator.raise_()
        self.myQStackedWidget = QStackedWidget(Dialog)
        self.myQStackedWidget.setObjectName(u"myQStackedWidget")
        self.myQStackedWidget.setGeometry(QRect(60, 110, 711, 591))
        self.myQStackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.searchPage = QWidget()
        self.searchPage.setObjectName(u"searchPage")
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
        self.elsevierQuery.setGeometry(QRect(20, 40, 411, 41))
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
        self.searchElsevierJournals.setGeometry(QRect(440, 40, 101, 41))
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
        self.searchListTableWidget.setGeometry(QRect(20, 30, 621, 301))
        self.searchListTableWidget.setStyleSheet(u"QHeaderView::section {\n"
"	color: rgb(113, 113, 113);\n"
"}\n"
"font: 700 12pt")
        self.myQStackedWidget.addWidget(self.searchPage)
        self.setAIPage = QWidget()
        self.setAIPage.setObjectName(u"setAIPage")
        self.label = QLabel(self.setAIPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 121, 41))
        self.label.setStyleSheet(u"font: 700 11pt;")
        self.pushButton_5 = QPushButton(self.setAIPage)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(490, 140, 181, 161))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(56, 178, 224);\n"
"	font: 700 11pt;\n"
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
"	font: 700 11pt;\n"
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
"	font: 700 11pt;\n"
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
"	font: 700 11pt;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"	border: 4px solid rgb(56, 178, 224);\n"
"}")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)
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
        self.pushButton_Llama70b = QPushButton(self.setAIPage)
        self.pushButton_Llama70b.setObjectName(u"pushButton_Llama70b")
        self.pushButton_Llama70b.setGeometry(QRect(260, 140, 181, 161))
        self.pushButton_Llama70b.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_Llama70b.setCheckable(True)
        self.pushButton_Llama70b.setAutoExclusive(True)
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
        self.searchResultsBar = QLineEdit(self.setFiltersOption)
        self.searchResultsBar.setObjectName(u"searchResultsBar")
        self.searchResultsBar.setGeometry(QRect(20, 40, 511, 41))
        self.searchResultsBar.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"	padding-left: 10px;\n"
"}\n"
"")
        self.setFiltersButton = QPushButton(self.setFiltersOption)
        self.setFiltersButton.setObjectName(u"setFiltersButton")
        self.setFiltersButton.setGeometry(QRect(550, 40, 101, 41))
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
        self.setFiltersPage = QWidget(self.resultsPage)
        self.setFiltersPage.setObjectName(u"setFiltersPage")
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
        self.publishDateLabel = QLabel(self.setFiltersPage)
        self.publishDateLabel.setObjectName(u"publishDateLabel")
        self.publishDateLabel.setGeometry(QRect(410, 40, 101, 16))
        self.publishDateLabel.setStyleSheet(u"font: 700 12pt;")
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
        self.publishDate = QDateEdit(self.setFiltersPage)
        self.publishDate.setObjectName(u"publishDate")
        self.publishDate.setGeometry(QRect(410, 70, 110, 22))
        self.publishDate.setStyleSheet(u"QDateEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
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
        self.processJournalsButton = QPushButton(self.setFiltersPage)
        self.processJournalsButton.setObjectName(u"processJournalsButton")
        self.processJournalsButton.setGeometry(QRect(480, 360, 111, 41))
        self.processJournalsButton.setStyleSheet(u"QWidget{\n"
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
"QPushButton:Checked{\n"
"	background-color: rgb(56, 177, 224);\n"
"}")
        self.processJournalsButton.setCheckable(True)
        self.processJournalsButton.setChecked(False)
        self.processJournalsButton.setAutoRepeat(False)
        self.processJournalsButton.setAutoExclusive(True)
        self.setFiltersCloseButton = QPushButton(self.setFiltersPage)
        self.setFiltersCloseButton.setObjectName(u"setFiltersCloseButton")
        self.setFiltersCloseButton.setGeometry(QRect(20, 360, 41, 41))
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
        self.myQStackedWidget.addWidget(self.resultsPage)
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

        self.retranslateUi(Dialog)

        self.myQStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.searchButton.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.setAIButton.setText(QCoreApplication.translate("Dialog", u"Set AI", None))
        self.uploadButton.setText(QCoreApplication.translate("Dialog", u"Upload", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Drive AI", None))
        self.resultsButton.setText(QCoreApplication.translate("Dialog", u"Results", None))
        self.searchJournalsLabel.setText(QCoreApplication.translate("Dialog", u"Search Journals", None))
        self.elsevierQuery.setPlaceholderText(QCoreApplication.translate("Dialog", u"Search for a journal...", None))
        self.downloadElsevierJournals.setText(QCoreApplication.translate("Dialog", u"Download", None))
        self.searchElsevierJournals.setText(QCoreApplication.translate("Dialog", u"Search", None))
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
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Llama 3.1B", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Chat GPT", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Meta AI", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Llama 8B", None))
        self.pushButton_ChatGpt.setText(QCoreApplication.translate("Dialog", u"GPT-4o mini", None))
        self.pushButton_Llama70b.setText(QCoreApplication.translate("Dialog", u"Llama 3.1-70B", None))
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
        self.searchResultsTag.setText(QCoreApplication.translate("Dialog", u"Enter your Natural Language Query", None))
        self.searchResultsBar.setPlaceholderText(QCoreApplication.translate("Dialog", u"Find me journals relevant to...", None))
        self.setFiltersButton.setText(QCoreApplication.translate("Dialog", u"Set Filters", None))
        self.resultsListTag.setText(QCoreApplication.translate("Dialog", u"Results", None))
        self.authorLabel.setText(QCoreApplication.translate("Dialog", u"Author:", None))
        self.publishDateLabel.setText(QCoreApplication.translate("Dialog", u"Publish Date", None))
        self.settingLabel.setText(QCoreApplication.translate("Dialog", u"Setting", None))
        self.keyWordsLabel.setText(QCoreApplication.translate("Dialog", u"Key Words", None))
        self.authorName.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Author's Name...", None))
        self.keyWords.setText("")
        self.keyWords.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter key words separated by \",\"", None))
        self.setting.setText("")
        self.setting.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter a country", None))
        self.processJournalsButton.setText(QCoreApplication.translate("Dialog", u"Process Journals", None))
        self.setFiltersCloseButton.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.backButton.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.nextButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

