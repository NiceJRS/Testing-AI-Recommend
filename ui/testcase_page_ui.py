# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testcase_page.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_TestcasePage(object):
    def setupUi(self, TestcasePage):
        if not TestcasePage.objectName():
            TestcasePage.setObjectName(u"TestcasePage")
        TestcasePage.resize(980, 720)
        self.verticalLayout = QVBoxLayout(TestcasePage)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, 20, -1)
        self.horizontalLayoutHeader = QHBoxLayout()
        self.horizontalLayoutHeader.setSpacing(16)
        self.horizontalLayoutHeader.setObjectName(u"horizontalLayoutHeader")
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setSpacing(6)
        self.titleLayout.setObjectName(u"titleLayout")
        self.labelTitle = QLabel(TestcasePage)
        self.labelTitle.setObjectName(u"labelTitle")

        self.titleLayout.addWidget(self.labelTitle)


        self.horizontalLayoutHeader.addLayout(self.titleLayout)

        self.headerSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutHeader.addItem(self.headerSpacer)

        self.actionsLayout = QHBoxLayout()
        self.actionsLayout.setSpacing(12)
        self.actionsLayout.setObjectName(u"actionsLayout")
        self.btnImport = QPushButton(TestcasePage)
        self.btnImport.setObjectName(u"btnImport")
        self.btnImport.setMinimumSize(QSize(140, 44))

        self.actionsLayout.addWidget(self.btnImport)


        self.horizontalLayoutHeader.addLayout(self.actionsLayout)


        self.verticalLayout.addLayout(self.horizontalLayoutHeader)

        self.verticalLayoutTable = QVBoxLayout()
        self.verticalLayoutTable.setObjectName(u"verticalLayoutTable")
        self.tableTestCases = QTableWidget(TestcasePage)
        if (self.tableTestCases.columnCount() < 8):
            self.tableTestCases.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableTestCases.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableTestCases.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableTestCases.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableTestCases.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableTestCases.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableTestCases.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableTestCases.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableTestCases.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tableTestCases.rowCount() < 3):
            self.tableTestCases.setRowCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableTestCases.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableTestCases.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableTestCases.setItem(2, 0, __qtablewidgetitem10)
        self.tableTestCases.setObjectName(u"tableTestCases")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableTestCases.sizePolicy().hasHeightForWidth())
        self.tableTestCases.setSizePolicy(sizePolicy)
        self.tableTestCases.setAlternatingRowColors(True)
        self.tableTestCases.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableTestCases.setRowCount(3)
        self.tableTestCases.setColumnCount(8)
        self.tableTestCases.horizontalHeader().setVisible(True)
        self.tableTestCases.verticalHeader().setVisible(False)

        self.verticalLayoutTable.addWidget(self.tableTestCases)


        self.verticalLayout.addLayout(self.verticalLayoutTable)


        self.retranslateUi(TestcasePage)

        QMetaObject.connectSlotsByName(TestcasePage)
    # setupUi

    def retranslateUi(self, TestcasePage):
        TestcasePage.setStyleSheet(QCoreApplication.translate("TestcasePage", u"background-color: #f5f5f5;", None))
        self.labelTitle.setStyleSheet(QCoreApplication.translate("TestcasePage", u"font-size: 28px; font-weight: 600; color: #222222;", None))
        self.labelTitle.setText(QCoreApplication.translate("TestcasePage", u"Test Case List", None))
        self.btnImport.setStyleSheet(QCoreApplication.translate("TestcasePage", u"QPushButton { background-color: #d32f2f; color: white; border: none; border-radius: 10px; font-weight: 600; padding: 10px 22px; }", None))
        self.btnImport.setText(QCoreApplication.translate("TestcasePage", u"Import Test Case", None))
        ___qtablewidgetitem = self.tableTestCases.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TestcasePage", u"No", None));
        ___qtablewidgetitem1 = self.tableTestCases.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TestcasePage", u"Service", None));
        ___qtablewidgetitem2 = self.tableTestCases.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TestcasePage", u"Number of Scenarios", None));
        ___qtablewidgetitem3 = self.tableTestCases.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TestcasePage", u"Priority", None));
        ___qtablewidgetitem4 = self.tableTestCases.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TestcasePage", u"Security", None));
        ___qtablewidgetitem5 = self.tableTestCases.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TestcasePage", u"Mobile", None));
        ___qtablewidgetitem6 = self.tableTestCases.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TestcasePage", u"Web Console", None));
        ___qtablewidgetitem7 = self.tableTestCases.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TestcasePage", u"Country", None));

        __sortingEnabled = self.tableTestCases.isSortingEnabled()
        self.tableTestCases.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tableTestCases.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("TestcasePage", u"2026-01-10", None));
        ___qtablewidgetitem9 = self.tableTestCases.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("TestcasePage", u"2026-01-12", None));
        ___qtablewidgetitem10 = self.tableTestCases.item(2, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("TestcasePage", u"2026-01-14", None));
        self.tableTestCases.setSortingEnabled(__sortingEnabled)

        self.tableTestCases.setStyleSheet(QCoreApplication.translate("TestcasePage", u"QTableWidget { background-color: white; border-radius: 12px; border: none; font-size: 14px; } QHeaderView::section { background-color: #2e2e2e; color: white; padding: 6px; border: none; font-weight: 600; }", None))
    # retranslateUi

