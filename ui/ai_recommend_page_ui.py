# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ai_recommend_page.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(980, 720)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(32)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_left = QWidget(Form)
        self.widget_left.setObjectName(u"widget_left")
        self.widget_left.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_left.sizePolicy().hasHeightForWidth())
        self.widget_left.setSizePolicy(sizePolicy)
        self.widget_left.setMaximumSize(QSize(400, 700))
        self.widget_left.setStyleSheet(u"background-color:white;\n"
"border-radius: 12px")
        self.verticalLayout = QVBoxLayout(self.widget_left)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, 40)
        self.label = QLabel(self.widget_left)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight: 700; font-size: 16px; color: red; padding-bottom: 6px;")

        self.verticalLayout.addWidget(self.label)

        self.groupBox = QGroupBox(self.widget_left)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_2.addWidget(self.radioButton_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget_left)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_5.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_5.addWidget(self.radioButton_4)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_7 = QGroupBox(self.widget_left)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.comboBox = QComboBox(self.groupBox_7)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setStyleSheet(u" border: 1px solid #dcdcdc;border-radius: 12px;")

        self.verticalLayout_6.addWidget(self.comboBox)


        self.verticalLayout.addWidget(self.groupBox_7)

        self.groupBox_3 = QGroupBox(self.widget_left)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_5 = QCheckBox(self.groupBox_3)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_3.addWidget(self.checkBox_5)

        self.checkBox_4 = QCheckBox(self.groupBox_3)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_3.addWidget(self.checkBox_4)

        self.checkBox_3 = QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_3.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.pushButton_2 = QPushButton(self.widget_left)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.widget_left)

        self.widget_right = QWidget(Form)
        self.widget_right.setObjectName(u"widget_right")
        self.verticalLayout_4 = QVBoxLayout(self.widget_right)
        self.verticalLayout_4.setSpacing(16)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget_right)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setStyleSheet(u"font-weight: 700; font-size: 16px; color: red; padding-bottom: 6px;")

        self.verticalLayout_4.addWidget(self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.widget_right)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 110))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.groupBox_4 = QGroupBox(self.widget_right)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 180))
        self.groupBox_4.setMaximumSize(QSize(16777215, 150))
        self.groupBox_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 40, 351, 121))

        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.widget_right)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 200))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_8.addWidget(self.label_9)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.widget_right)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.horizontalSlider_2 = QSlider(self.groupBox_6)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_5.addWidget(self.horizontalSlider_2)

        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_9.addWidget(self.label_10)


        self.verticalLayout_4.addWidget(self.groupBox_6)

        self.pushButton = QPushButton(self.widget_right)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.widget_right)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        Form.setStyleSheet(QCoreApplication.translate("Form", u"background-color: #f5f5f5; font-family: \"Segoe UI\", sans-serif;", None))
        self.label.setText(QCoreApplication.translate("Form", u"1. CONFIGURATION (Input)", None))
        self.groupBox.setStyleSheet(QCoreApplication.translate("Form", u"QGroupBox { background-color: white; border: 1px solid #e0e0e0; border-radius: 10px; margin-top: 12px; padding: 12px 14px 12px 14px; font-weight: 600; color: #2e2e2e; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 6px; }", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.groupBox_2.setStyleSheet(QCoreApplication.translate("Form", u"QGroupBox { background-color: white; border: 1px solid #e0e0e0; border-radius: 10px; margin-top: 12px; padding: 12px 14px 12px 14px; font-weight: 600; color: #2e2e2e; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 6px; }", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.groupBox_7.setStyleSheet(QCoreApplication.translate("Form", u"QGroupBox { background-color: white; border: 1px solid #e0e0e0; border-radius: 10px; margin-top: 12px; padding: 12px 14px 12px 14px; font-weight: 600; color: #2e2e2e; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 6px; }", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.groupBox_3.setStyleSheet(QCoreApplication.translate("Form", u"QGroupBox { background-color: white; border: 1px solid #e0e0e0; border-radius: 10px; margin-top: 12px; padding: 12px 14px 12px 14px; font-weight: 600; color: #2e2e2e; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 6px; }", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.pushButton_2.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton { background-color: #d32f2f; color: white; border: none; border-radius: 12px; padding: 10px 20px; font-weight: 600; } QPushButton:hover { background-color: #bf2626; }", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\U0001f680 Generate Recommendation", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.frame_2.setStyleSheet(QCoreApplication.translate("Form", u"QFrame { background-color: #d32f2f; border-radius: 14px; color: white; }", None))
        self.groupBox_4.setStyleSheet(QCoreApplication.translate("Form", u"QGroupBox { background-color: white; border: 1px solid #e0e0e0; border-radius: 12px; margin-top: 12px; padding: 14px; font-weight: 600; color: #2e2e2e; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 6px; }", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.label_6.setStyleSheet(QCoreApplication.translate("Form", u"font-size: 14px; color: #4a4a4a; line-height: 22px; padding-top: 4px;", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.groupBox_5.setStyleSheet(QCoreApplication.translate("Form", u"QGroupBox { background-color: white; border: 1px solid #e0e0e0; border-radius: 12px; margin-top: 12px; padding: 14px; font-weight: 600; color: #2e2e2e; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 6px; }", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\u26a0\ufe0f ", None))
        self.label_7.setStyleSheet(QCoreApplication.translate("Form", u"font-size: 14px; color: #2a2a2a; line-height: 20px;", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setStyleSheet(QCoreApplication.translate("Form", u"font-size: 14px; color: #2a2a2a; line-height: 20px;", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_9.setStyleSheet(QCoreApplication.translate("Form", u"font-size: 14px; color: #2a2a2a; line-height: 20px;", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.groupBox_6.setStyleSheet(QCoreApplication.translate("Form", u"QGroupBox { background-color: white; border: 1px solid #e0e0e0; border-radius: 12px; margin-top: 12px; padding: 14px; font-weight: 600; color: #2e2e2e; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 6px; }", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Low", None))
        self.horizontalSlider_2.setStyleSheet(QCoreApplication.translate("Form", u"QSlider::groove:horizontal { height: 6px; background: #e0e0e0; border-radius: 3px; } QSlider::handle:horizontal { width: 14px; height: 14px; border-radius: 7px; background: #d32f2f; margin: -4px 0; }", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"High", None))
        self.label_10.setStyleSheet(QCoreApplication.translate("Form", u"font-size: 14px; color: #414141; padding-top: 4px;", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton { background-color: #d32f2f; color: white; border: none; border-radius: 12px; padding: 10px 26px; font-weight: 600; } QPushButton:hover { background-color: #bf2626; }", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Export Test Case (.xlsx)", None))
    # retranslateUi

