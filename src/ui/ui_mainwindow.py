# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'python_app.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(877, 674)
        self.actionAllCameras = QAction(MainWindow)
        self.actionAllCameras.setObjectName(u"actionAllCameras")
        self.actionAddCamera = QAction(MainWindow)
        self.actionAddCamera.setObjectName(u"actionAddCamera")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cameraList = QWidget()
        self.cameraList.setObjectName(u"cameraList")
        self.horizontalLayout_3 = QHBoxLayout(self.cameraList)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cameraListHorizontalWidget = QWidget(self.cameraList)
        self.cameraListHorizontalWidget.setObjectName(u"cameraListHorizontalWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.cameraListHorizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftSide = QWidget(self.cameraListHorizontalWidget)
        self.leftSide.setObjectName(u"leftSide")
        self.gridLayout_5 = QGridLayout(self.leftSide)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.searchButton = QPushButton(self.leftSide)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMaximumSize(QSize(500, 250))
        self.searchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.searchButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #2d89ef;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1b5fbf;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #144a99;\n"
"}")

        self.gridLayout_5.addWidget(self.searchButton, 1, 1, 1, 1)

        self.searchEdit = QLineEdit(self.leftSide)
        self.searchEdit.setObjectName(u"searchEdit")

        self.gridLayout_5.addWidget(self.searchEdit, 1, 0, 1, 1)

        self.searchLabel = QLabel(self.leftSide)
        self.searchLabel.setObjectName(u"searchLabel")

        self.gridLayout_5.addWidget(self.searchLabel, 0, 0, 1, 1)

        self.cameraTable = QTableWidget(self.leftSide)
        self.cameraTable.setObjectName(u"cameraTable")
        self.cameraTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cameraTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cameraTable.setRowCount(0)
        self.cameraTable.setColumnCount(0)

        self.gridLayout_5.addWidget(self.cameraTable, 2, 0, 1, 2)


        self.horizontalLayout_2.addWidget(self.leftSide)

        self.rightSide = QWidget(self.cameraListHorizontalWidget)
        self.rightSide.setObjectName(u"rightSide")
        self.gridLayout_6 = QGridLayout(self.rightSide)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.cameraDeleteButton = QPushButton(self.rightSide)
        self.cameraDeleteButton.setObjectName(u"cameraDeleteButton")
        self.cameraDeleteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cameraDeleteButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #c0392b;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e74c3c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #922b21;\n"
"}")

        self.gridLayout_6.addWidget(self.cameraDeleteButton, 19, 0, 1, 2)

        self.tabWidget = QTabWidget(self.rightSide)
        self.tabWidget.setObjectName(u"tabWidget")
        self.identificationTab = QWidget()
        self.identificationTab.setObjectName(u"identificationTab")
        self.horizontalLayout_5 = QHBoxLayout(self.identificationTab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.identificationGridLayout = QGridLayout()
        self.identificationGridLayout.setObjectName(u"identificationGridLayout")
        self.cameraTypeLabel = QLabel(self.identificationTab)
        self.cameraTypeLabel.setObjectName(u"cameraTypeLabel")
        self.cameraTypeLabel.setFrameShape(QFrame.Box)
        self.cameraTypeLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.identificationGridLayout.addWidget(self.cameraTypeLabel, 1, 1, 1, 1)

        self.cameraLocationLabel = QLabel(self.identificationTab)
        self.cameraLocationLabel.setObjectName(u"cameraLocationLabel")
        self.cameraLocationLabel.setFrameShape(QFrame.Box)
        self.cameraLocationLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.identificationGridLayout.addWidget(self.cameraLocationLabel, 1, 0, 1, 1)

        self.cameraPurposeLabel = QLabel(self.identificationTab)
        self.cameraPurposeLabel.setObjectName(u"cameraPurposeLabel")
        self.cameraPurposeLabel.setFrameShape(QFrame.Box)
        self.cameraPurposeLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.identificationGridLayout.addWidget(self.cameraPurposeLabel, 2, 0, 1, 1)

        self.cameraFunctioLabel = QLabel(self.identificationTab)
        self.cameraFunctioLabel.setObjectName(u"cameraFunctioLabel")
        self.cameraFunctioLabel.setFrameShape(QFrame.Box)
        self.cameraFunctioLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.identificationGridLayout.addWidget(self.cameraFunctioLabel, 2, 1, 1, 1)

        self.cameraCoverageLabel = QLabel(self.identificationTab)
        self.cameraCoverageLabel.setObjectName(u"cameraCoverageLabel")
        self.cameraCoverageLabel.setFrameShape(QFrame.Box)
        self.cameraCoverageLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.identificationGridLayout.addWidget(self.cameraCoverageLabel, 4, 0, 1, 2)


        self.horizontalLayout_5.addLayout(self.identificationGridLayout)

        self.tabWidget.addTab(self.identificationTab, "")
        self.infrastructerTab = QWidget()
        self.infrastructerTab.setObjectName(u"infrastructerTab")
        self.verticalLayout_2 = QVBoxLayout(self.infrastructerTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.infrastructureGridLayout = QGridLayout()
        self.infrastructureGridLayout.setObjectName(u"infrastructureGridLayout")
        self.cameraModelLabel = QLabel(self.infrastructerTab)
        self.cameraModelLabel.setObjectName(u"cameraModelLabel")
        self.cameraModelLabel.setFrameShape(QFrame.Box)
        self.cameraModelLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.infrastructureGridLayout.addWidget(self.cameraModelLabel, 2, 0, 1, 1)

        self.cameraServerLabel = QLabel(self.infrastructerTab)
        self.cameraServerLabel.setObjectName(u"cameraServerLabel")
        self.cameraServerLabel.setFrameShape(QFrame.Box)
        self.cameraServerLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.infrastructureGridLayout.addWidget(self.cameraServerLabel, 1, 0, 1, 1)

        self.cameraIPaddressLabel = QLabel(self.infrastructerTab)
        self.cameraIPaddressLabel.setObjectName(u"cameraIPaddressLabel")
        self.cameraIPaddressLabel.setFrameShape(QFrame.Box)
        self.cameraIPaddressLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.infrastructureGridLayout.addWidget(self.cameraIPaddressLabel, 0, 0, 1, 2)

        self.cameraRackLabel = QLabel(self.infrastructerTab)
        self.cameraRackLabel.setObjectName(u"cameraRackLabel")
        self.cameraRackLabel.setFrameShape(QFrame.Box)
        self.cameraRackLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.infrastructureGridLayout.addWidget(self.cameraRackLabel, 1, 1, 1, 1)

        self.cameraRetentionLabel = QLabel(self.infrastructerTab)
        self.cameraRetentionLabel.setObjectName(u"cameraRetentionLabel")
        self.cameraRetentionLabel.setFrameShape(QFrame.Box)
        self.cameraRetentionLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.infrastructureGridLayout.addWidget(self.cameraRetentionLabel, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.infrastructureGridLayout)

        self.tabWidget.addTab(self.infrastructerTab, "")
        self.statusTab = QWidget()
        self.statusTab.setObjectName(u"statusTab")
        self.verticalLayout_6 = QVBoxLayout(self.statusTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.statusGridLayout = QGridLayout()
        self.statusGridLayout.setObjectName(u"statusGridLayout")
        self.cameraStartDateLabel = QLabel(self.statusTab)
        self.cameraStartDateLabel.setObjectName(u"cameraStartDateLabel")
        self.cameraStartDateLabel.setFrameShape(QFrame.Box)
        self.cameraStartDateLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.statusGridLayout.addWidget(self.cameraStartDateLabel, 1, 0, 1, 1)

        self.cameraEndDateLabel = QLabel(self.statusTab)
        self.cameraEndDateLabel.setObjectName(u"cameraEndDateLabel")
        self.cameraEndDateLabel.setFrameShape(QFrame.Box)
        self.cameraEndDateLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.statusGridLayout.addWidget(self.cameraEndDateLabel, 1, 1, 1, 1)

        self.cameraStatusLabel = QLabel(self.statusTab)
        self.cameraStatusLabel.setObjectName(u"cameraStatusLabel")
        self.cameraStatusLabel.setFrameShape(QFrame.Box)
        self.cameraStatusLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.statusGridLayout.addWidget(self.cameraStatusLabel, 0, 0, 1, 2)


        self.verticalLayout_6.addLayout(self.statusGridLayout)

        self.tabWidget.addTab(self.statusTab, "")
        self.imageTab = QWidget()
        self.imageTab.setObjectName(u"imageTab")
        self.horizontalLayout_6 = QHBoxLayout(self.imageTab)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.imageVerticalLayout = QVBoxLayout()
        self.imageVerticalLayout.setObjectName(u"imageVerticalLayout")
        self.cameraImageLabel = QLabel(self.imageTab)
        self.cameraImageLabel.setObjectName(u"cameraImageLabel")
        self.cameraImageLabel.setFrameShape(QFrame.Box)
        self.cameraImageLabel.setAlignment(Qt.AlignCenter)

        self.imageVerticalLayout.addWidget(self.cameraImageLabel)


        self.horizontalLayout_6.addLayout(self.imageVerticalLayout)

        self.tabWidget.addTab(self.imageTab, "")
        self.actionTab = QWidget()
        self.actionTab.setObjectName(u"actionTab")
        self.verticalLayout_3 = QVBoxLayout(self.actionTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.actionGridLayout = QGridLayout()
        self.actionGridLayout.setObjectName(u"actionGridLayout")
        self.cameraNoteLabel = QLabel(self.actionTab)
        self.cameraNoteLabel.setObjectName(u"cameraNoteLabel")
        self.cameraNoteLabel.setFrameShape(QFrame.Box)
        self.cameraNoteLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.actionGridLayout.addWidget(self.cameraNoteLabel, 0, 0, 1, 1)

        self.cameraActionLabel = QLabel(self.actionTab)
        self.cameraActionLabel.setObjectName(u"cameraActionLabel")
        self.cameraActionLabel.setFrameShape(QFrame.Box)
        self.cameraActionLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.actionGridLayout.addWidget(self.cameraActionLabel, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.actionGridLayout)

        self.tabWidget.addTab(self.actionTab, "")

        self.gridLayout_6.addWidget(self.tabWidget, 3, 0, 1, 2)

        self.cameraEditButton = QPushButton(self.rightSide)
        self.cameraEditButton.setObjectName(u"cameraEditButton")
        self.cameraEditButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cameraEditButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #27ae60;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e8449;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #145a32;\n"
"}")

        self.gridLayout_6.addWidget(self.cameraEditButton, 9, 1, 1, 1)

        self.cameraControllButton = QPushButton(self.rightSide)
        self.cameraControllButton.setObjectName(u"cameraControllButton")
        self.cameraControllButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cameraControllButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #27ae60;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e8449;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #145a32;\n"
"}")

        self.gridLayout_6.addWidget(self.cameraControllButton, 9, 0, 1, 1)

        self.cameraIDLabel = QLabel(self.rightSide)
        self.cameraIDLabel.setObjectName(u"cameraIDLabel")

        self.gridLayout_6.addWidget(self.cameraIDLabel, 1, 0, 1, 1)

        self.cameraCodeLabel = QLabel(self.rightSide)
        self.cameraCodeLabel.setObjectName(u"cameraCodeLabel")
        self.cameraCodeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.cameraCodeLabel, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 18, 0, 1, 2)


        self.horizontalLayout_2.addWidget(self.rightSide)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 6)

        self.horizontalLayout_3.addWidget(self.cameraListHorizontalWidget)

        self.stackedWidget.addWidget(self.cameraList)
        self.addCamera = QWidget()
        self.addCamera.setObjectName(u"addCamera")
        self.addCamera.setEnabled(True)
        self.verticalLayout_4 = QVBoxLayout(self.addCamera)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.addCameraVerticalLayout = QVBoxLayout()
        self.addCameraVerticalLayout.setObjectName(u"addCameraVerticalLayout")
        self.addCameraLabel = QLabel(self.addCamera)
        self.addCameraLabel.setObjectName(u"addCameraLabel")
        self.addCameraLabel.setAlignment(Qt.AlignCenter)

        self.addCameraVerticalLayout.addWidget(self.addCameraLabel)

        self.scrollArea = QScrollArea(self.addCamera)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 823, 1288))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.addCameraFormLayout = QFormLayout()
        self.addCameraFormLayout.setObjectName(u"addCameraFormLayout")
        self.addCameraCodeLabel = QLabel(self.scrollAreaWidgetContents)
        self.addCameraCodeLabel.setObjectName(u"addCameraCodeLabel")

        self.addCameraFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.addCameraCodeLabel)

        self.addCameraCodeLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.addCameraCodeLineEdit.setObjectName(u"addCameraCodeLineEdit")

        self.addCameraFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.addCameraCodeLineEdit)

        self.networkGroupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.networkGroupBox.setObjectName(u"networkGroupBox")
        self.formLayout_2 = QFormLayout(self.networkGroupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.addCameraIPAddressLabel = QLabel(self.networkGroupBox)
        self.addCameraIPAddressLabel.setObjectName(u"addCameraIPAddressLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.addCameraIPAddressLabel)

        self.addCameraIPAddressLineEdit = QLineEdit(self.networkGroupBox)
        self.addCameraIPAddressLineEdit.setObjectName(u"addCameraIPAddressLineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.addCameraIPAddressLineEdit)

        self.addCameraServerLabel = QLabel(self.networkGroupBox)
        self.addCameraServerLabel.setObjectName(u"addCameraServerLabel")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.addCameraServerLabel)

        self.addCameraServerLineEdit = QLineEdit(self.networkGroupBox)
        self.addCameraServerLineEdit.setObjectName(u"addCameraServerLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.addCameraServerLineEdit)

        self.addCameraRackLabel = QLabel(self.networkGroupBox)
        self.addCameraRackLabel.setObjectName(u"addCameraRackLabel")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.addCameraRackLabel)

        self.addCameraRackLineEdit = QLineEdit(self.networkGroupBox)
        self.addCameraRackLineEdit.setObjectName(u"addCameraRackLineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.addCameraRackLineEdit)


        self.addCameraFormLayout.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.networkGroupBox)

        self.locationGroupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.locationGroupBox.setObjectName(u"locationGroupBox")
        self.formLayout_3 = QFormLayout(self.locationGroupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.addCameraLocationLabel = QLabel(self.locationGroupBox)
        self.addCameraLocationLabel.setObjectName(u"addCameraLocationLabel")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.addCameraLocationLabel)

        self.addCameraLocationLineEdit = QLineEdit(self.locationGroupBox)
        self.addCameraLocationLineEdit.setObjectName(u"addCameraLocationLineEdit")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.addCameraLocationLineEdit)

        self.addCameraCoverageLabel = QLabel(self.locationGroupBox)
        self.addCameraCoverageLabel.setObjectName(u"addCameraCoverageLabel")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.addCameraCoverageLabel)

        self.addCameraCoverageLineEdit = QLineEdit(self.locationGroupBox)
        self.addCameraCoverageLineEdit.setObjectName(u"addCameraCoverageLineEdit")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.addCameraCoverageLineEdit)


        self.addCameraFormLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.locationGroupBox)

        self.addCameraActionGroupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.addCameraActionGroupBox.setObjectName(u"addCameraActionGroupBox")
        self.formLayout_5 = QFormLayout(self.addCameraActionGroupBox)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.addCameraNoteLabel = QLabel(self.addCameraActionGroupBox)
        self.addCameraNoteLabel.setObjectName(u"addCameraNoteLabel")
        self.addCameraNoteLabel.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.addCameraNoteLabel)

        self.addCameraActionLabel = QLabel(self.addCameraActionGroupBox)
        self.addCameraActionLabel.setObjectName(u"addCameraActionLabel")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.addCameraActionLabel)

        self.addCameraNoteEdit = QTextEdit(self.addCameraActionGroupBox)
        self.addCameraNoteEdit.setObjectName(u"addCameraNoteEdit")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.addCameraNoteEdit)

        self.addCameraActionTextEdit = QTextEdit(self.addCameraActionGroupBox)
        self.addCameraActionTextEdit.setObjectName(u"addCameraActionTextEdit")

        self.formLayout_5.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.addCameraActionTextEdit)


        self.addCameraFormLayout.setWidget(14, QFormLayout.ItemRole.SpanningRole, self.addCameraActionGroupBox)

        self.addCameraButton = QPushButton(self.scrollAreaWidgetContents)
        self.addCameraButton.setObjectName(u"addCameraButton")
        self.addCameraButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addCameraButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #27ae60;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e8449;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #145a32;\n"
"}")

        self.addCameraFormLayout.setWidget(16, QFormLayout.ItemRole.SpanningRole, self.addCameraButton)

        self.typeGroupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.typeGroupBox.setObjectName(u"typeGroupBox")
        self.formLayout_6 = QFormLayout(self.typeGroupBox)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.addCameraTypeLabel = QLabel(self.typeGroupBox)
        self.addCameraTypeLabel.setObjectName(u"addCameraTypeLabel")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.addCameraTypeLabel)

        self.addCameraTypeLineEdit = QLineEdit(self.typeGroupBox)
        self.addCameraTypeLineEdit.setObjectName(u"addCameraTypeLineEdit")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.addCameraTypeLineEdit)

        self.addCameraFunctionLineEdit = QLineEdit(self.typeGroupBox)
        self.addCameraFunctionLineEdit.setObjectName(u"addCameraFunctionLineEdit")

        self.formLayout_6.setWidget(2, QFormLayout.ItemRole.FieldRole, self.addCameraFunctionLineEdit)

        self.addCameraPurposeLineEdit = QLineEdit(self.typeGroupBox)
        self.addCameraPurposeLineEdit.setObjectName(u"addCameraPurposeLineEdit")

        self.formLayout_6.setWidget(4, QFormLayout.ItemRole.FieldRole, self.addCameraPurposeLineEdit)

        self.addCameraFunctionLabel = QLabel(self.typeGroupBox)
        self.addCameraFunctionLabel.setObjectName(u"addCameraFunctionLabel")

        self.formLayout_6.setWidget(2, QFormLayout.ItemRole.LabelRole, self.addCameraFunctionLabel)

        self.addCameraPuropseLabel = QLabel(self.typeGroupBox)
        self.addCameraPuropseLabel.setObjectName(u"addCameraPuropseLabel")

        self.formLayout_6.setWidget(4, QFormLayout.ItemRole.LabelRole, self.addCameraPuropseLabel)


        self.addCameraFormLayout.setWidget(6, QFormLayout.ItemRole.SpanningRole, self.typeGroupBox)

        self.technicalGroupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.technicalGroupBox.setObjectName(u"technicalGroupBox")
        self.formLayout_7 = QFormLayout(self.technicalGroupBox)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.addCameraModelLabel = QLabel(self.technicalGroupBox)
        self.addCameraModelLabel.setObjectName(u"addCameraModelLabel")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.addCameraModelLabel)

        self.addCameraModelLineEdit = QLineEdit(self.technicalGroupBox)
        self.addCameraModelLineEdit.setObjectName(u"addCameraModelLineEdit")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.addCameraModelLineEdit)

        self.addCameraRetentionLineEdit = QLineEdit(self.technicalGroupBox)
        self.addCameraRetentionLineEdit.setObjectName(u"addCameraRetentionLineEdit")

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.FieldRole, self.addCameraRetentionLineEdit)

        self.addCameraRetentionLabel = QLabel(self.technicalGroupBox)
        self.addCameraRetentionLabel.setObjectName(u"addCameraRetentionLabel")

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.LabelRole, self.addCameraRetentionLabel)


        self.addCameraFormLayout.setWidget(8, QFormLayout.ItemRole.SpanningRole, self.technicalGroupBox)

        self.healthStatusGroupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.healthStatusGroupBox.setObjectName(u"healthStatusGroupBox")
        self.gridLayout_8 = QGridLayout(self.healthStatusGroupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.addCameraStartDateEdit = QDateTimeEdit(self.healthStatusGroupBox)
        self.addCameraStartDateEdit.setObjectName(u"addCameraStartDateEdit")
        self.addCameraStartDateEdit.setCalendarPopup(True)

        self.gridLayout_8.addWidget(self.addCameraStartDateEdit, 1, 1, 1, 1, Qt.AlignRight)

        self.addCameraStartDateLabel = QLabel(self.healthStatusGroupBox)
        self.addCameraStartDateLabel.setObjectName(u"addCameraStartDateLabel")

        self.gridLayout_8.addWidget(self.addCameraStartDateLabel, 1, 0, 1, 1)

        self.addCameraEndDateLabel = QLabel(self.healthStatusGroupBox)
        self.addCameraEndDateLabel.setObjectName(u"addCameraEndDateLabel")

        self.gridLayout_8.addWidget(self.addCameraEndDateLabel, 1, 2, 1, 1, Qt.AlignRight)

        self.addCameraEndDateEdit = QDateTimeEdit(self.healthStatusGroupBox)
        self.addCameraEndDateEdit.setObjectName(u"addCameraEndDateEdit")
        self.addCameraEndDateEdit.setEnabled(True)
        self.addCameraEndDateEdit.setCalendarPopup(True)

        self.gridLayout_8.addWidget(self.addCameraEndDateEdit, 1, 3, 1, 1)

        self.statusGroupBox = QGroupBox(self.healthStatusGroupBox)
        self.statusGroupBox.setObjectName(u"statusGroupBox")
        self.horizontalLayout_4 = QHBoxLayout(self.statusGroupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.addCameraActiveRadioButton = QRadioButton(self.statusGroupBox)
        self.addCameraActiveRadioButton.setObjectName(u"addCameraActiveRadioButton")

        self.horizontalLayout_4.addWidget(self.addCameraActiveRadioButton)

        self.addCameraInactiveButton = QRadioButton(self.statusGroupBox)
        self.addCameraInactiveButton.setObjectName(u"addCameraInactiveButton")

        self.horizontalLayout_4.addWidget(self.addCameraInactiveButton)

        self.addCameraDismantleRadioButton = QRadioButton(self.statusGroupBox)
        self.addCameraDismantleRadioButton.setObjectName(u"addCameraDismantleRadioButton")
        self.addCameraDismantleRadioButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.addCameraDismantleRadioButton)


        self.gridLayout_8.addWidget(self.statusGroupBox, 3, 0, 1, 4)


        self.addCameraFormLayout.setWidget(10, QFormLayout.ItemRole.SpanningRole, self.healthStatusGroupBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.addCameraFormLayout.setItem(1, QFormLayout.ItemRole.FieldRole, self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.addCameraFormLayout.setItem(3, QFormLayout.ItemRole.SpanningRole, self.horizontalSpacer_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.addCameraFormLayout.setItem(5, QFormLayout.ItemRole.SpanningRole, self.horizontalSpacer_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.addCameraFormLayout.setItem(7, QFormLayout.ItemRole.SpanningRole, self.horizontalSpacer_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.addCameraFormLayout.setItem(9, QFormLayout.ItemRole.SpanningRole, self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.addCameraFormLayout.setItem(11, QFormLayout.ItemRole.SpanningRole, self.horizontalSpacer_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.addCameraFormLayout.setItem(13, QFormLayout.ItemRole.SpanningRole, self.horizontalSpacer_7)

        self.imageGroupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.imageGroupBox.setObjectName(u"imageGroupBox")
        self.gridLayout_10 = QGridLayout(self.imageGroupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.addCameraImageLabel = QLabel(self.imageGroupBox)
        self.addCameraImageLabel.setObjectName(u"addCameraImageLabel")

        self.gridLayout_10.addWidget(self.addCameraImageLabel, 0, 0, 1, 1)

        self.addCameraImageLineEdit = QLineEdit(self.imageGroupBox)
        self.addCameraImageLineEdit.setObjectName(u"addCameraImageLineEdit")
        self.addCameraImageLineEdit.setReadOnly(True)

        self.gridLayout_10.addWidget(self.addCameraImageLineEdit, 0, 1, 1, 1)

        self.addCameraImageUploadButton = QPushButton(self.imageGroupBox)
        self.addCameraImageUploadButton.setObjectName(u"addCameraImageUploadButton")

        self.gridLayout_10.addWidget(self.addCameraImageUploadButton, 0, 2, 1, 1)

        self.addCameraPreviewImageLabel = QLabel(self.imageGroupBox)
        self.addCameraPreviewImageLabel.setObjectName(u"addCameraPreviewImageLabel")
        self.addCameraPreviewImageLabel.setFrameShape(QFrame.Box)
        self.addCameraPreviewImageLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.addCameraPreviewImageLabel, 0, 3, 1, 1)


        self.addCameraFormLayout.setWidget(12, QFormLayout.ItemRole.SpanningRole, self.imageGroupBox)


        self.verticalLayout_9.addLayout(self.addCameraFormLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.addCameraVerticalLayout.addWidget(self.scrollArea)


        self.verticalLayout_4.addLayout(self.addCameraVerticalLayout)

        self.stackedWidget.addWidget(self.addCamera)
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.verticalLayout_5 = QVBoxLayout(self.about)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.abotVerticalLayout = QVBoxLayout()
        self.abotVerticalLayout.setSpacing(0)
        self.abotVerticalLayout.setObjectName(u"abotVerticalLayout")
        self.aboutLabel = QLabel(self.about)
        self.aboutLabel.setObjectName(u"aboutLabel")
        self.aboutLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.abotVerticalLayout.addWidget(self.aboutLabel)

        self.aboutTextBrowser = QTextBrowser(self.about)
        self.aboutTextBrowser.setObjectName(u"aboutTextBrowser")
        self.aboutTextBrowser.setOverwriteMode(False)

        self.abotVerticalLayout.addWidget(self.aboutTextBrowser)


        self.verticalLayout_5.addLayout(self.abotVerticalLayout)

        self.stackedWidget.addWidget(self.about)

        self.verticalLayout_8.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 877, 24))
        self.mainMenu = QMenu(self.menubar)
        self.mainMenu.setObjectName(u"mainMenu")
        self.mainMenu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.mainMenu.menuAction())
        self.mainMenu.addAction(self.actionAllCameras)
        self.mainMenu.addAction(self.actionAddCamera)
        self.mainMenu.addSeparator()
        self.mainMenu.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pregledac kamera", None))
        self.actionAllCameras.setText(QCoreApplication.translate("MainWindow", u"Sve Kamere", None))
        self.actionAddCamera.setText(QCoreApplication.translate("MainWindow", u"Dodaj Kameru", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"O Aplikaciji", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Pretraga", None))
        self.searchLabel.setText(QCoreApplication.translate("MainWindow", u"Pretraga", None))
        self.cameraDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Brisanje Kamere", None))
        self.cameraTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Tip:", None))
        self.cameraLocationLabel.setText(QCoreApplication.translate("MainWindow", u"Lokacija:", None))
        self.cameraPurposeLabel.setText(QCoreApplication.translate("MainWindow", u"Svrha:", None))
        self.cameraFunctioLabel.setText(QCoreApplication.translate("MainWindow", u"Namena:", None))
        self.cameraCoverageLabel.setText(QCoreApplication.translate("MainWindow", u"Pokrivenost:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.identificationTab), QCoreApplication.translate("MainWindow", u"Informacije", None))
        self.cameraModelLabel.setText(QCoreApplication.translate("MainWindow", u"Rezolucija/Model:", None))
        self.cameraServerLabel.setText(QCoreApplication.translate("MainWindow", u"Server:", None))
        self.cameraIPaddressLabel.setText(QCoreApplication.translate("MainWindow", u"IP Adresa:", None))
        self.cameraRackLabel.setText(QCoreApplication.translate("MainWindow", u"Rek:", None))
        self.cameraRetentionLabel.setText(QCoreApplication.translate("MainWindow", u"Retencija:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infrastructerTab), QCoreApplication.translate("MainWindow", u"Infrastruktura", None))
        self.cameraStartDateLabel.setText(QCoreApplication.translate("MainWindow", u"Pocetak:", None))
        self.cameraEndDateLabel.setText(QCoreApplication.translate("MainWindow", u"Kraj:", None))
        self.cameraStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statusTab), QCoreApplication.translate("MainWindow", u"Status", None))
        self.cameraImageLabel.setText(QCoreApplication.translate("MainWindow", u"Slika", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageTab), QCoreApplication.translate("MainWindow", u"Slika", None))
        self.cameraNoteLabel.setText(QCoreApplication.translate("MainWindow", u"Napomena:", None))
        self.cameraActionLabel.setText(QCoreApplication.translate("MainWindow", u"Akcije:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.actionTab), QCoreApplication.translate("MainWindow", u"Akcije", None))
        self.cameraEditButton.setText(QCoreApplication.translate("MainWindow", u"Izmena", None))
        self.cameraControllButton.setText(QCoreApplication.translate("MainWindow", u"Upravljanje", None))
        self.cameraIDLabel.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.cameraCodeLabel.setText(QCoreApplication.translate("MainWindow", u"Kod:", None))
        self.addCameraLabel.setText(QCoreApplication.translate("MainWindow", u"Dodavanje Kamere", None))
        self.addCameraCodeLabel.setText(QCoreApplication.translate("MainWindow", u"Kod", None))
        self.networkGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"1. Mreza i Infrastruktura", None))
        self.addCameraIPAddressLabel.setText(QCoreApplication.translate("MainWindow", u"IP Adresa", None))
        self.addCameraServerLabel.setText(QCoreApplication.translate("MainWindow", u"Server", None))
        self.addCameraRackLabel.setText(QCoreApplication.translate("MainWindow", u"Rek", None))
        self.locationGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"2. Lokacija i Pokrivanje", None))
        self.addCameraLocationLabel.setText(QCoreApplication.translate("MainWindow", u"Lokacija", None))
        self.addCameraCoverageLabel.setText(QCoreApplication.translate("MainWindow", u"Pokrivenost", None))
        self.addCameraActionGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"7. Akcije", None))
#if QT_CONFIG(tooltip)
        self.addCameraNoteLabel.setToolTip(QCoreApplication.translate("MainWindow", u"Nije Obavezno Polje", None))
#endif // QT_CONFIG(tooltip)
        self.addCameraNoteLabel.setText(QCoreApplication.translate("MainWindow", u"Napomena", None))
        self.addCameraActionLabel.setText(QCoreApplication.translate("MainWindow", u"Akcija", None))
        self.addCameraButton.setText(QCoreApplication.translate("MainWindow", u"Dodajte Kameru", None))
        self.typeGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"3. Tip i Namena", None))
        self.addCameraTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Tip", None))
        self.addCameraFunctionLabel.setText(QCoreApplication.translate("MainWindow", u"Namena", None))
        self.addCameraPuropseLabel.setText(QCoreApplication.translate("MainWindow", u"Svrha", None))
        self.technicalGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"4. Tehnicki Podaci", None))
        self.addCameraModelLabel.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.addCameraRetentionLabel.setText(QCoreApplication.translate("MainWindow", u"Retencija", None))
        self.healthStatusGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"5. Status", None))
        self.addCameraStartDateLabel.setText(QCoreApplication.translate("MainWindow", u"Postavljena", None))
        self.addCameraEndDateLabel.setText(QCoreApplication.translate("MainWindow", u"Skinuta", None))
        self.statusGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        self.addCameraActiveRadioButton.setText(QCoreApplication.translate("MainWindow", u"Aktivna", None))
        self.addCameraInactiveButton.setText(QCoreApplication.translate("MainWindow", u"Neaktivna", None))
        self.addCameraDismantleRadioButton.setText(QCoreApplication.translate("MainWindow", u"Skinuta", None))
        self.imageGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"6. Slika", None))
        self.addCameraImageLabel.setText(QCoreApplication.translate("MainWindow", u"Izaberite Sliku", None))
        self.addCameraImageUploadButton.setText(QCoreApplication.translate("MainWindow", u"Izaberi Sliku", None))
        self.addCameraPreviewImageLabel.setText(QCoreApplication.translate("MainWindow", u"Prikaz Slike", None))
        self.aboutLabel.setText(QCoreApplication.translate("MainWindow", u"O Aplikaciji", None))
        self.aboutTextBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">Aplikacija za upravljanje kamerama </span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Verzija:</span> 1.0 </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ova aplikacija predstavlja interni softverski alat namenjen za pregled, organizaciju i upravljanje informacijama o kamerama unutar sistema. Razvijen"
                        "a je sa ciljem da olak\u0161a pregled postoje\u0107ih kamera, njihovu evidenciju, kao i brzu dostupnost klju\u010dnih podataka vezanih za svaku pojedina\u010dnu kameru. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Korisnicima omogu\u0107ava: </p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pregled kompletne liste kamera kroz tabelarni prikaz</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Brzu pretragu i filtriranje kamera</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Prikaz detaljnih informacija o svakoj kameri</li>\n"
"<li style=\"\" styl"
                        "e=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Vizuelni prikaz (slika/screenshot) zone koju kamera pokriva</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dodavanje novih kamera u sistem</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Izmenu postoje\u0107ih podataka o kamerama</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Brisanje kamera iz evidencije uz potvrdu </li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Aplikacija je dizajnirana za internu upotrebu i ne uklju\u010duje funkcionalnosti za video streaming niti obradu u\u017eivo snimaka. Fokus je isklju\u010divo na organizac"
                        "iji i preglednosti podataka. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Autor:</span> Milan Vasovic<br /><span style=\" font-weight:600;\">Razvio:</span> AriusSystems<br /><span style=\" font-weight:600;\">Kontakt:</span> milan.vasovic.work@gmail.com </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Licenca:</span><br />Ovaj softver je vlasni\u0161tvo kompanije AriusSystems i namenjen je isklju\u010divo za internu upotrebu. Sva prava su zadr\u017eana. Nije dozvoljeno kopiranje, distribucija, modifikacija ili dalja prodaja ovog softvera bez izri\u010dite dozvole autora. </p></body></html>", None))
        self.mainMenu.setTitle(QCoreApplication.translate("MainWindow", u"Meni", None))
    # retranslateUi

