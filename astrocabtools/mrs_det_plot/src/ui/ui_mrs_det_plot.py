# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mrs_det_plot.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MrsDetPlot(object):
    def setupUi(self, MrsDetPlot):
        MrsDetPlot.setObjectName("MrsDetPlot")
        MrsDetPlot.resize(1334, 647)
        self.centralwidget = QtWidgets.QWidget(MrsDetPlot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.midPlot = QtWidgets.QGroupBox(self.centralwidget)
        self.midPlot.setMinimumSize(QtCore.QSize(0, 150))
        self.midPlot.setMaximumSize(QtCore.QSize(16777215, 150))
        self.midPlot.setTitle("")
        self.midPlot.setObjectName("midPlot")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.midPlot)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.midLayout_vbox = QtWidgets.QVBoxLayout()
        self.midLayout_vbox.setObjectName("midLayout_vbox")
        self.gridLayout_18.addLayout(self.midLayout_vbox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.midPlot, 2, 0, 1, 3)
        self.midButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.midButton.sizePolicy().hasHeightForWidth())
        self.midButton.setSizePolicy(sizePolicy)
        self.midButton.setObjectName("midButton")
        self.gridLayout.addWidget(self.midButton, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setRowWrapPolicy(QtWidgets.QFormLayout.WrapAllRows)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setObjectName("formLayout_4")
        self.frame3Label = QtWidgets.QLabel(self.groupBox_3)
        self.frame3Label.setObjectName("frame3Label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame3Label)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.frameSlider3 = QtWidgets.QSlider(self.groupBox_3)
        self.frameSlider3.setEnabled(False)
        self.frameSlider3.setOrientation(QtCore.Qt.Horizontal)
        self.frameSlider3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.frameSlider3.setObjectName("frameSlider3")
        self.gridLayout_14.addWidget(self.frameSlider3, 0, 1, 1, 2)
        self.frameMinimumLabel3 = QtWidgets.QLabel(self.groupBox_3)
        self.frameMinimumLabel3.setText("")
        self.frameMinimumLabel3.setObjectName("frameMinimumLabel3")
        self.gridLayout_14.addWidget(self.frameMinimumLabel3, 1, 1, 1, 1)
        self.frameMaximumLabel3 = QtWidgets.QLabel(self.groupBox_3)
        self.frameMaximumLabel3.setText("")
        self.frameMaximumLabel3.setObjectName("frameMaximumLabel3")
        self.gridLayout_14.addWidget(self.frameMaximumLabel3, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.frameLineEdit3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.frameLineEdit3.setEnabled(False)
        self.frameLineEdit3.setMaximumSize(QtCore.QSize(35, 30))
        self.frameLineEdit3.setObjectName("frameLineEdit3")
        self.gridLayout_14.addWidget(self.frameLineEdit3, 0, 0, 2, 1)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout_14)
        self.integration3Label = QtWidgets.QLabel(self.groupBox_3)
        self.integration3Label.setObjectName("integration3Label")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.integration3Label)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.integrationSlider3 = QtWidgets.QSlider(self.groupBox_3)
        self.integrationSlider3.setEnabled(False)
        self.integrationSlider3.setOrientation(QtCore.Qt.Horizontal)
        self.integrationSlider3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.integrationSlider3.setObjectName("integrationSlider3")
        self.gridLayout_15.addWidget(self.integrationSlider3, 0, 1, 1, 2)
        self.integrationMinimumLabel3 = QtWidgets.QLabel(self.groupBox_3)
        self.integrationMinimumLabel3.setText("")
        self.integrationMinimumLabel3.setObjectName("integrationMinimumLabel3")
        self.gridLayout_15.addWidget(self.integrationMinimumLabel3, 1, 1, 1, 1)
        self.integrationMaximumLabel3 = QtWidgets.QLabel(self.groupBox_3)
        self.integrationMaximumLabel3.setText("")
        self.integrationMaximumLabel3.setObjectName("integrationMaximumLabel3")
        self.gridLayout_15.addWidget(self.integrationMaximumLabel3, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.integrationLineEdit3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.integrationLineEdit3.setEnabled(False)
        self.integrationLineEdit3.setMaximumSize(QtCore.QSize(35, 30))
        self.integrationLineEdit3.setObjectName("integrationLineEdit3")
        self.gridLayout_15.addWidget(self.integrationLineEdit3, 0, 0, 2, 1)
        self.formLayout_4.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout_15)
        self.gridLayout_3.addLayout(self.formLayout_4, 0, 3, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setRowWrapPolicy(QtWidgets.QFormLayout.WrapAllRows)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.frame2Label = QtWidgets.QLabel(self.groupBox_3)
        self.frame2Label.setObjectName("frame2Label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame2Label)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.frameSlider2 = QtWidgets.QSlider(self.groupBox_3)
        self.frameSlider2.setEnabled(False)
        self.frameSlider2.setOrientation(QtCore.Qt.Horizontal)
        self.frameSlider2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.frameSlider2.setObjectName("frameSlider2")
        self.gridLayout_12.addWidget(self.frameSlider2, 0, 1, 1, 2)
        self.frameMaximumLabel2 = QtWidgets.QLabel(self.groupBox_3)
        self.frameMaximumLabel2.setText("")
        self.frameMaximumLabel2.setObjectName("frameMaximumLabel2")
        self.gridLayout_12.addWidget(self.frameMaximumLabel2, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.frameMinimumLabel2 = QtWidgets.QLabel(self.groupBox_3)
        self.frameMinimumLabel2.setText("")
        self.frameMinimumLabel2.setObjectName("frameMinimumLabel2")
        self.gridLayout_12.addWidget(self.frameMinimumLabel2, 1, 1, 1, 1)
        self.frameLineEdit2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.frameLineEdit2.setEnabled(False)
        self.frameLineEdit2.setMaximumSize(QtCore.QSize(35, 30))
        self.frameLineEdit2.setObjectName("frameLineEdit2")
        self.gridLayout_12.addWidget(self.frameLineEdit2, 0, 0, 2, 1)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout_12)
        self.integration2Label = QtWidgets.QLabel(self.groupBox_3)
        self.integration2Label.setObjectName("integration2Label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.integration2Label)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.integrationMinimumLabel2 = QtWidgets.QLabel(self.groupBox_3)
        self.integrationMinimumLabel2.setText("")
        self.integrationMinimumLabel2.setObjectName("integrationMinimumLabel2")
        self.gridLayout_13.addWidget(self.integrationMinimumLabel2, 1, 1, 1, 1)
        self.integrationSlider2 = QtWidgets.QSlider(self.groupBox_3)
        self.integrationSlider2.setEnabled(False)
        self.integrationSlider2.setOrientation(QtCore.Qt.Horizontal)
        self.integrationSlider2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.integrationSlider2.setObjectName("integrationSlider2")
        self.gridLayout_13.addWidget(self.integrationSlider2, 0, 1, 1, 2)
        self.integrationMaximumLabel2 = QtWidgets.QLabel(self.groupBox_3)
        self.integrationMaximumLabel2.setText("")
        self.integrationMaximumLabel2.setObjectName("integrationMaximumLabel2")
        self.gridLayout_13.addWidget(self.integrationMaximumLabel2, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.integrationLineEdit2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.integrationLineEdit2.setEnabled(False)
        self.integrationLineEdit2.setMaximumSize(QtCore.QSize(35, 30))
        self.integrationLineEdit2.setObjectName("integrationLineEdit2")
        self.gridLayout_13.addWidget(self.integrationLineEdit2, 0, 0, 2, 1)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout_13)
        self.gridLayout_3.addLayout(self.formLayout_3, 0, 2, 1, 1)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setRowWrapPolicy(QtWidgets.QFormLayout.WrapAllRows)
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setObjectName("formLayout_5")
        self.frame4Label = QtWidgets.QLabel(self.groupBox_3)
        self.frame4Label.setObjectName("frame4Label")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame4Label)
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.frameSlider4 = QtWidgets.QSlider(self.groupBox_3)
        self.frameSlider4.setEnabled(False)
        self.frameSlider4.setTracking(True)
        self.frameSlider4.setOrientation(QtCore.Qt.Horizontal)
        self.frameSlider4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.frameSlider4.setObjectName("frameSlider4")
        self.gridLayout_16.addWidget(self.frameSlider4, 0, 1, 1, 2)
        self.frameMaximumLabel4 = QtWidgets.QLabel(self.groupBox_3)
        self.frameMaximumLabel4.setText("")
        self.frameMaximumLabel4.setObjectName("frameMaximumLabel4")
        self.gridLayout_16.addWidget(self.frameMaximumLabel4, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.frameMinimumLabel4 = QtWidgets.QLabel(self.groupBox_3)
        self.frameMinimumLabel4.setText("")
        self.frameMinimumLabel4.setObjectName("frameMinimumLabel4")
        self.gridLayout_16.addWidget(self.frameMinimumLabel4, 1, 1, 1, 1)
        self.frameLineEdit4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.frameLineEdit4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameLineEdit4.sizePolicy().hasHeightForWidth())
        self.frameLineEdit4.setSizePolicy(sizePolicy)
        self.frameLineEdit4.setMaximumSize(QtCore.QSize(35, 30))
        self.frameLineEdit4.setObjectName("frameLineEdit4")
        self.gridLayout_16.addWidget(self.frameLineEdit4, 0, 0, 2, 1)
        self.formLayout_5.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout_16)
        self.integration4Label = QtWidgets.QLabel(self.groupBox_3)
        self.integration4Label.setObjectName("integration4Label")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.integration4Label)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.integrationMaximumLabel4 = QtWidgets.QLabel(self.groupBox_3)
        self.integrationMaximumLabel4.setText("")
        self.integrationMaximumLabel4.setObjectName("integrationMaximumLabel4")
        self.gridLayout_17.addWidget(self.integrationMaximumLabel4, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.integrationMinimumLabel4 = QtWidgets.QLabel(self.groupBox_3)
        self.integrationMinimumLabel4.setText("")
        self.integrationMinimumLabel4.setObjectName("integrationMinimumLabel4")
        self.gridLayout_17.addWidget(self.integrationMinimumLabel4, 1, 1, 1, 1)
        self.integrationSlider4 = QtWidgets.QSlider(self.groupBox_3)
        self.integrationSlider4.setEnabled(False)
        self.integrationSlider4.setOrientation(QtCore.Qt.Horizontal)
        self.integrationSlider4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.integrationSlider4.setObjectName("integrationSlider4")
        self.gridLayout_17.addWidget(self.integrationSlider4, 0, 1, 1, 2)
        self.integrationLineEdit4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.integrationLineEdit4.setEnabled(False)
        self.integrationLineEdit4.setMaximumSize(QtCore.QSize(35, 30))
        self.integrationLineEdit4.setObjectName("integrationLineEdit4")
        self.gridLayout_17.addWidget(self.integrationLineEdit4, 0, 0, 2, 1)
        self.formLayout_5.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout_17)
        self.gridLayout_3.addLayout(self.formLayout_5, 0, 4, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setRowWrapPolicy(QtWidgets.QFormLayout.WrapAllRows)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.frame1Label = QtWidgets.QLabel(self.groupBox_3)
        self.frame1Label.setObjectName("frame1Label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame1Label)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frameMinimumLabel1 = QtWidgets.QLabel(self.groupBox_3)
        self.frameMinimumLabel1.setText("")
        self.frameMinimumLabel1.setObjectName("frameMinimumLabel1")
        self.gridLayout_10.addWidget(self.frameMinimumLabel1, 1, 1, 1, 1)
        self.frameSlider1 = QtWidgets.QSlider(self.groupBox_3)
        self.frameSlider1.setEnabled(False)
        self.frameSlider1.setOrientation(QtCore.Qt.Horizontal)
        self.frameSlider1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.frameSlider1.setObjectName("frameSlider1")
        self.gridLayout_10.addWidget(self.frameSlider1, 0, 1, 1, 2)
        self.frameMaximumLabel1 = QtWidgets.QLabel(self.groupBox_3)
        self.frameMaximumLabel1.setText("")
        self.frameMaximumLabel1.setObjectName("frameMaximumLabel1")
        self.gridLayout_10.addWidget(self.frameMaximumLabel1, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.frameLineEdit1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.frameLineEdit1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameLineEdit1.sizePolicy().hasHeightForWidth())
        self.frameLineEdit1.setSizePolicy(sizePolicy)
        self.frameLineEdit1.setMinimumSize(QtCore.QSize(0, 0))
        self.frameLineEdit1.setMaximumSize(QtCore.QSize(35, 30))
        self.frameLineEdit1.setObjectName("frameLineEdit1")
        self.gridLayout_10.addWidget(self.frameLineEdit1, 0, 0, 2, 1)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout_10)
        self.integration1Label = QtWidgets.QLabel(self.groupBox_3)
        self.integration1Label.setObjectName("integration1Label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.integration1Label)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.integrationSlider1 = QtWidgets.QSlider(self.groupBox_3)
        self.integrationSlider1.setEnabled(False)
        self.integrationSlider1.setOrientation(QtCore.Qt.Horizontal)
        self.integrationSlider1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.integrationSlider1.setObjectName("integrationSlider1")
        self.gridLayout_11.addWidget(self.integrationSlider1, 0, 1, 1, 2)
        self.integrationMinimumLabel1 = QtWidgets.QLabel(self.groupBox_3)
        self.integrationMinimumLabel1.setText("")
        self.integrationMinimumLabel1.setObjectName("integrationMinimumLabel1")
        self.gridLayout_11.addWidget(self.integrationMinimumLabel1, 1, 1, 1, 1)
        self.integrationMaximumLabel1 = QtWidgets.QLabel(self.groupBox_3)
        self.integrationMaximumLabel1.setText("")
        self.integrationMaximumLabel1.setObjectName("integrationMaximumLabel1")
        self.gridLayout_11.addWidget(self.integrationMaximumLabel1, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.integrationLineEdit1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.integrationLineEdit1.setEnabled(False)
        self.integrationLineEdit1.setMaximumSize(QtCore.QSize(35, 30))
        self.integrationLineEdit1.setObjectName("integrationLineEdit1")
        self.gridLayout_11.addWidget(self.integrationLineEdit1, 0, 0, 2, 1)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout_11)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.fileButton4 = QtWidgets.QPushButton(self.groupBox_3)
        self.fileButton4.setObjectName("fileButton4")
        self.gridLayout_3.addWidget(self.fileButton4, 1, 4, 1, 1)
        self.fileButton3 = QtWidgets.QPushButton(self.groupBox_3)
        self.fileButton3.setObjectName("fileButton3")
        self.gridLayout_3.addWidget(self.fileButton3, 1, 3, 1, 1)
        self.fileButton2 = QtWidgets.QPushButton(self.groupBox_3)
        self.fileButton2.setObjectName("fileButton2")
        self.gridLayout_3.addWidget(self.fileButton2, 1, 2, 1, 1)
        self.fileButton1 = QtWidgets.QPushButton(self.groupBox_3)
        self.fileButton1.setObjectName("fileButton1")
        self.gridLayout_3.addWidget(self.fileButton1, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.yLabel1 = QtWidgets.QLabel(self.groupBox_2)
        self.yLabel1.setObjectName("yLabel1")
        self.gridLayout_8.addWidget(self.yLabel1, 0, 2, 1, 1)
        self.zUnitLabel1 = QtWidgets.QLabel(self.groupBox_2)
        self.zUnitLabel1.setText("")
        self.zUnitLabel1.setObjectName("zUnitLabel1")
        self.gridLayout_8.addWidget(self.zUnitLabel1, 0, 6, 1, 1)
        self.zLabel1 = QtWidgets.QLabel(self.groupBox_2)
        self.zLabel1.setObjectName("zLabel1")
        self.gridLayout_8.addWidget(self.zLabel1, 0, 4, 1, 1)
        self.xlineEdit1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.xlineEdit1.setReadOnly(True)
        self.xlineEdit1.setObjectName("xlineEdit1")
        self.gridLayout_8.addWidget(self.xlineEdit1, 0, 1, 1, 1)
        self.xLabel3 = QtWidgets.QLabel(self.groupBox_2)
        self.xLabel3.setObjectName("xLabel3")
        self.gridLayout_8.addWidget(self.xLabel3, 2, 0, 1, 1)
        self.ylineEdit1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.ylineEdit1.setReadOnly(True)
        self.ylineEdit1.setObjectName("ylineEdit1")
        self.gridLayout_8.addWidget(self.ylineEdit1, 0, 3, 1, 1)
        self.zlineEdit1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.zlineEdit1.setReadOnly(True)
        self.zlineEdit1.setObjectName("zlineEdit1")
        self.gridLayout_8.addWidget(self.zlineEdit1, 0, 5, 1, 1)
        self.showAxisButton1 = QtWidgets.QPushButton(self.groupBox_2)
        self.showAxisButton1.setEnabled(False)
        self.showAxisButton1.setObjectName("showAxisButton1")
        self.gridLayout_8.addWidget(self.showAxisButton1, 0, 7, 1, 1)
        self.showPointButton2 = QtWidgets.QPushButton(self.groupBox_2)
        self.showPointButton2.setEnabled(False)
        self.showPointButton2.setObjectName("showPointButton2")
        self.gridLayout_8.addWidget(self.showPointButton2, 1, 8, 1, 1)
        self.zUnitLabel2 = QtWidgets.QLabel(self.groupBox_2)
        self.zUnitLabel2.setText("")
        self.zUnitLabel2.setObjectName("zUnitLabel2")
        self.gridLayout_8.addWidget(self.zUnitLabel2, 1, 6, 1, 1)
        self.xlineEdit3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.xlineEdit3.setObjectName("xlineEdit3")
        self.gridLayout_8.addWidget(self.xlineEdit3, 2, 1, 1, 1)
        self.yLabel2 = QtWidgets.QLabel(self.groupBox_2)
        self.yLabel2.setObjectName("yLabel2")
        self.gridLayout_8.addWidget(self.yLabel2, 1, 2, 1, 1)
        self.zlineEdit2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.zlineEdit2.setReadOnly(True)
        self.zlineEdit2.setObjectName("zlineEdit2")
        self.gridLayout_8.addWidget(self.zlineEdit2, 1, 5, 1, 1)
        self.zUnitLabel3 = QtWidgets.QLabel(self.groupBox_2)
        self.zUnitLabel3.setText("")
        self.zUnitLabel3.setObjectName("zUnitLabel3")
        self.gridLayout_8.addWidget(self.zUnitLabel3, 2, 6, 1, 1)
        self.ylineEdit3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.ylineEdit3.setReadOnly(True)
        self.ylineEdit3.setObjectName("ylineEdit3")
        self.gridLayout_8.addWidget(self.ylineEdit3, 2, 3, 1, 1)
        self.zlineEdit3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.zlineEdit3.setReadOnly(True)
        self.zlineEdit3.setObjectName("zlineEdit3")
        self.gridLayout_8.addWidget(self.zlineEdit3, 2, 5, 1, 1)
        self.showAxisButton3 = QtWidgets.QPushButton(self.groupBox_2)
        self.showAxisButton3.setEnabled(False)
        self.showAxisButton3.setObjectName("showAxisButton3")
        self.gridLayout_8.addWidget(self.showAxisButton3, 2, 7, 1, 1)
        self.showAxisButton2 = QtWidgets.QPushButton(self.groupBox_2)
        self.showAxisButton2.setEnabled(False)
        self.showAxisButton2.setObjectName("showAxisButton2")
        self.gridLayout_8.addWidget(self.showAxisButton2, 1, 7, 1, 1)
        self.yLabel3 = QtWidgets.QLabel(self.groupBox_2)
        self.yLabel3.setObjectName("yLabel3")
        self.gridLayout_8.addWidget(self.yLabel3, 2, 2, 1, 1)
        self.ylineEdit2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.ylineEdit2.setReadOnly(True)
        self.ylineEdit2.setObjectName("ylineEdit2")
        self.gridLayout_8.addWidget(self.ylineEdit2, 1, 3, 1, 1)
        self.zLabel2 = QtWidgets.QLabel(self.groupBox_2)
        self.zLabel2.setObjectName("zLabel2")
        self.gridLayout_8.addWidget(self.zLabel2, 1, 4, 1, 1)
        self.showPointButton1 = QtWidgets.QPushButton(self.groupBox_2)
        self.showPointButton1.setEnabled(False)
        self.showPointButton1.setObjectName("showPointButton1")
        self.gridLayout_8.addWidget(self.showPointButton1, 0, 8, 1, 1)
        self.xlineEdit2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.xlineEdit2.setReadOnly(True)
        self.xlineEdit2.setObjectName("xlineEdit2")
        self.gridLayout_8.addWidget(self.xlineEdit2, 1, 1, 1, 1)
        self.zLabel3 = QtWidgets.QLabel(self.groupBox_2)
        self.zLabel3.setObjectName("zLabel3")
        self.gridLayout_8.addWidget(self.zLabel3, 2, 4, 1, 1)
        self.xLabel1 = QtWidgets.QLabel(self.groupBox_2)
        self.xLabel1.setObjectName("xLabel1")
        self.gridLayout_8.addWidget(self.xLabel1, 0, 0, 1, 1)
        self.showPointButton3 = QtWidgets.QPushButton(self.groupBox_2)
        self.showPointButton3.setEnabled(False)
        self.showPointButton3.setObjectName("showPointButton3")
        self.gridLayout_8.addWidget(self.showPointButton3, 2, 8, 1, 1)
        self.xLabel2 = QtWidgets.QLabel(self.groupBox_2)
        self.xLabel2.setObjectName("xLabel2")
        self.gridLayout_8.addWidget(self.xLabel2, 1, 0, 1, 1)
        self.xLabel4 = QtWidgets.QLabel(self.groupBox_2)
        self.xLabel4.setObjectName("xLabel4")
        self.gridLayout_8.addWidget(self.xLabel4, 3, 0, 1, 1)
        self.xlineEdit4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.xlineEdit4.setReadOnly(True)
        self.xlineEdit4.setObjectName("xlineEdit4")
        self.gridLayout_8.addWidget(self.xlineEdit4, 3, 1, 1, 1)
        self.yLabel4 = QtWidgets.QLabel(self.groupBox_2)
        self.yLabel4.setObjectName("yLabel4")
        self.gridLayout_8.addWidget(self.yLabel4, 3, 2, 1, 1)
        self.ylineEdit4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.ylineEdit4.setReadOnly(True)
        self.ylineEdit4.setObjectName("ylineEdit4")
        self.gridLayout_8.addWidget(self.ylineEdit4, 3, 3, 1, 1)
        self.zLabel4 = QtWidgets.QLabel(self.groupBox_2)
        self.zLabel4.setObjectName("zLabel4")
        self.gridLayout_8.addWidget(self.zLabel4, 3, 4, 1, 1)
        self.zlineEdit4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.zlineEdit4.setReadOnly(True)
        self.zlineEdit4.setObjectName("zlineEdit4")
        self.gridLayout_8.addWidget(self.zlineEdit4, 3, 5, 1, 1)
        self.showAxisButton4 = QtWidgets.QPushButton(self.groupBox_2)
        self.showAxisButton4.setEnabled(False)
        self.showAxisButton4.setObjectName("showAxisButton4")
        self.gridLayout_8.addWidget(self.showAxisButton4, 3, 7, 1, 1)
        self.showPointButton4 = QtWidgets.QPushButton(self.groupBox_2)
        self.showPointButton4.setEnabled(False)
        self.showPointButton4.setObjectName("showPointButton4")
        self.gridLayout_8.addWidget(self.showPointButton4, 3, 8, 1, 1)
        self.zUnitLabel4 = QtWidgets.QLabel(self.groupBox_2)
        self.zUnitLabel4.setText("")
        self.zUnitLabel4.setObjectName("zUnitLabel4")
        self.gridLayout_8.addWidget(self.zUnitLabel4, 3, 6, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.scaleLabel = QtWidgets.QLabel(self.centralwidget)
        self.scaleLabel.setObjectName("scaleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.scaleLabel)
        self.stretchLabel = QtWidgets.QLabel(self.centralwidget)
        self.stretchLabel.setObjectName("stretchLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.stretchLabel)
        self.colourLabel = QtWidgets.QLabel(self.centralwidget)
        self.colourLabel.setObjectName("colourLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.colourLabel)
        self.zoomLabel = QtWidgets.QLabel(self.centralwidget)
        self.zoomLabel.setObjectName("zoomLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.zoomLabel)
        self.stretchGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.stretchGroupBox.setEnabled(False)
        self.stretchGroupBox.setTitle("")
        self.stretchGroupBox.setObjectName("stretchGroupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.stretchGroupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioBScale3 = QtWidgets.QRadioButton(self.stretchGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioBScale3.sizePolicy().hasHeightForWidth())
        self.radioBScale3.setSizePolicy(sizePolicy)
        self.radioBScale3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioBScale3.setObjectName("radioBScale3")
        self.horizontalLayout_3.addWidget(self.radioBScale3)
        self.radioBScale2 = QtWidgets.QRadioButton(self.stretchGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioBScale2.sizePolicy().hasHeightForWidth())
        self.radioBScale2.setSizePolicy(sizePolicy)
        self.radioBScale2.setObjectName("radioBScale2")
        self.horizontalLayout_3.addWidget(self.radioBScale2)
        self.radioBScale1 = QtWidgets.QRadioButton(self.stretchGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioBScale1.sizePolicy().hasHeightForWidth())
        self.radioBScale1.setSizePolicy(sizePolicy)
        self.radioBScale1.setObjectName("radioBScale1")
        self.horizontalLayout_3.addWidget(self.radioBScale1)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.stretchGroupBox)
        self.centerButton = QtWidgets.QPushButton(self.centralwidget)
        self.centerButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerButton.sizePolicy().hasHeightForWidth())
        self.centerButton.setSizePolicy(sizePolicy)
        self.centerButton.setObjectName("centerButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.centerButton)
        self.scaleGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.scaleGroupBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleGroupBox.sizePolicy().hasHeightForWidth())
        self.scaleGroupBox.setSizePolicy(sizePolicy)
        self.scaleGroupBox.setTitle("")
        self.scaleGroupBox.setObjectName("scaleGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scaleGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minMaxRadioB = QtWidgets.QRadioButton(self.scaleGroupBox)
        self.minMaxRadioB.setObjectName("minMaxRadioB")
        self.horizontalLayout.addWidget(self.minMaxRadioB)
        self.zscaleRadioB = QtWidgets.QRadioButton(self.scaleGroupBox)
        self.zscaleRadioB.setObjectName("zscaleRadioB")
        self.horizontalLayout.addWidget(self.zscaleRadioB)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.scaleGroupBox)
        self.colourGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.colourGroupBox.setEnabled(False)
        self.colourGroupBox.setTitle("")
        self.colourGroupBox.setObjectName("colourGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.colourGroupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.radioBColor3 = QtWidgets.QRadioButton(self.colourGroupBox)
        self.radioBColor3.setObjectName("radioBColor3")
        self.gridLayout_4.addWidget(self.radioBColor3, 0, 1, 1, 1)
        self.radioBColor1 = QtWidgets.QRadioButton(self.colourGroupBox)
        self.radioBColor1.setObjectName("radioBColor1")
        self.gridLayout_4.addWidget(self.radioBColor1, 0, 0, 1, 1)
        self.radioBColor4 = QtWidgets.QRadioButton(self.colourGroupBox)
        self.radioBColor4.setObjectName("radioBColor4")
        self.gridLayout_4.addWidget(self.radioBColor4, 0, 2, 1, 1)
        self.radioBColor5 = QtWidgets.QRadioButton(self.colourGroupBox)
        self.radioBColor5.setObjectName("radioBColor5")
        self.gridLayout_4.addWidget(self.radioBColor5, 1, 0, 1, 1)
        self.radioBColor2 = QtWidgets.QRadioButton(self.colourGroupBox)
        self.radioBColor2.setObjectName("radioBColor2")
        self.gridLayout_4.addWidget(self.radioBColor2, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.colourGroupBox)
        self.gridLayout.addLayout(self.formLayout, 0, 2, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MrsDetPlot.setCentralWidget(self.centralwidget)

        self.retranslateUi(MrsDetPlot)
        QtCore.QMetaObject.connectSlotsByName(MrsDetPlot)

    def retranslateUi(self, MrsDetPlot):
        _translate = QtCore.QCoreApplication.translate
        MrsDetPlot.setWindowTitle(_translate("MrsDetPlot", "mrs_det_plot - Beta version"))
        self.midButton.setText(_translate("MrsDetPlot", "Show \'.fits\' images"))
        self.frame3Label.setText(_translate("MrsDetPlot", "F3"))
        self.integration3Label.setText(_translate("MrsDetPlot", "I3"))
        self.frame2Label.setText(_translate("MrsDetPlot", "F2"))
        self.integration2Label.setText(_translate("MrsDetPlot", "I2"))
        self.frame4Label.setText(_translate("MrsDetPlot", "F4"))
        self.integration4Label.setText(_translate("MrsDetPlot", "I4"))
        self.frame1Label.setText(_translate("MrsDetPlot", "F1"))
        self.integration1Label.setText(_translate("MrsDetPlot", "I1"))
        self.fileButton4.setText(_translate("MrsDetPlot", "Search \'.fits\' File 4"))
        self.fileButton3.setText(_translate("MrsDetPlot", "Search \'.fits\' File 3"))
        self.fileButton2.setText(_translate("MrsDetPlot", "Search \'.fits\' File 2"))
        self.fileButton1.setText(_translate("MrsDetPlot", "Search \'.fits\' File 1"))
        self.yLabel1.setText(_translate("MrsDetPlot", "Y1"))
        self.zLabel1.setText(_translate("MrsDetPlot", "Z1"))
        self.xLabel3.setText(_translate("MrsDetPlot", "X3"))
        self.showAxisButton1.setText(_translate("MrsDetPlot", "Show axis plot"))
        self.showPointButton2.setText(_translate("MrsDetPlot", "Show point plot"))
        self.yLabel2.setText(_translate("MrsDetPlot", "Y2"))
        self.showAxisButton3.setText(_translate("MrsDetPlot", "Show axis plot"))
        self.showAxisButton2.setText(_translate("MrsDetPlot", "Show axis plot"))
        self.yLabel3.setText(_translate("MrsDetPlot", "Y3"))
        self.zLabel2.setText(_translate("MrsDetPlot", "Z2"))
        self.showPointButton1.setText(_translate("MrsDetPlot", "Show point plot"))
        self.zLabel3.setText(_translate("MrsDetPlot", "Z3"))
        self.xLabel1.setText(_translate("MrsDetPlot", "X1"))
        self.showPointButton3.setText(_translate("MrsDetPlot", "Show point plot"))
        self.xLabel2.setText(_translate("MrsDetPlot", "X2"))
        self.xLabel4.setText(_translate("MrsDetPlot", "X4"))
        self.yLabel4.setText(_translate("MrsDetPlot", "Y4"))
        self.zLabel4.setText(_translate("MrsDetPlot", "Z4"))
        self.showAxisButton4.setText(_translate("MrsDetPlot", "Show axis plot"))
        self.showPointButton4.setText(_translate("MrsDetPlot", "Show point plot"))
        self.scaleLabel.setText(_translate("MrsDetPlot", "Scale"))
        self.stretchLabel.setText(_translate("MrsDetPlot", "Stretch"))
        self.colourLabel.setText(_translate("MrsDetPlot", "Colour"))
        self.zoomLabel.setText(_translate("MrsDetPlot", "Zoom"))
        self.radioBScale3.setText(_translate("MrsDetPlot", "Sqrt"))
        self.radioBScale2.setText(_translate("MrsDetPlot", "Log"))
        self.radioBScale1.setText(_translate("MrsDetPlot", "Linear"))
        self.centerButton.setText(_translate("MrsDetPlot", "Zoom Fit"))
        self.minMaxRadioB.setText(_translate("MrsDetPlot", "MinMax Interval"))
        self.zscaleRadioB.setText(_translate("MrsDetPlot", "Zscale Interval"))
        self.radioBColor3.setText(_translate("MrsDetPlot", "Accent"))
        self.radioBColor1.setText(_translate("MrsDetPlot", "Gray"))
        self.radioBColor4.setText(_translate("MrsDetPlot", "Heat"))
        self.radioBColor5.setText(_translate("MrsDetPlot", "Rainbow"))
        self.radioBColor2.setText(_translate("MrsDetPlot", "CoolWarm"))

