# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fit_line.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FitLine(object):
    def setupUi(self, FitLine):
        FitLine.setObjectName("FitLine")
        FitLine.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FitLine)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.generationPointsButton = QtWidgets.QPushButton(self.centralwidget)
        self.generationPointsButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generationPointsButton.sizePolicy().hasHeightForWidth())
        self.generationPointsButton.setSizePolicy(sizePolicy)
        self.generationPointsButton.setObjectName("generationPointsButton")
        self.horizontalLayout_2.addWidget(self.generationPointsButton)
        self.showPointsButton = QtWidgets.QPushButton(self.centralwidget)
        self.showPointsButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showPointsButton.sizePolicy().hasHeightForWidth())
        self.showPointsButton.setSizePolicy(sizePolicy)
        self.showPointsButton.setObjectName("showPointsButton")
        self.horizontalLayout_2.addWidget(self.showPointsButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.clearLastButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearLastButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearLastButton.sizePolicy().hasHeightForWidth())
        self.clearLastButton.setSizePolicy(sizePolicy)
        self.clearLastButton.setObjectName("clearLastButton")
        self.horizontalLayout.addWidget(self.clearLastButton)
        self.clearFittingButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearFittingButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearFittingButton.sizePolicy().hasHeightForWidth())
        self.clearFittingButton.setSizePolicy(sizePolicy)
        self.clearFittingButton.setObjectName("clearFittingButton")
        self.horizontalLayout.addWidget(self.clearFittingButton)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.indicationLabel = QtWidgets.QLabel(self.centralwidget)
        self.indicationLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.indicationLabel.sizePolicy().hasHeightForWidth())
        self.indicationLabel.setSizePolicy(sizePolicy)
        self.indicationLabel.setText("")
        self.indicationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.indicationLabel.setObjectName("indicationLabel")
        self.gridLayout.addWidget(self.indicationLabel, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loadPltButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadPltButton.sizePolicy().hasHeightForWidth())
        self.loadPltButton.setSizePolicy(sizePolicy)
        self.loadPltButton.setObjectName("loadPltButton")
        self.horizontalLayout_3.addWidget(self.loadPltButton)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_3.addWidget(self.saveButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.middlePlot = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middlePlot.sizePolicy().hasHeightForWidth())
        self.middlePlot.setSizePolicy(sizePolicy)
        self.middlePlot.setTitle("")
        self.middlePlot.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.middlePlot.setFlat(False)
        self.middlePlot.setObjectName("middlePlot")
        self.gridLayout.addWidget(self.middlePlot, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        FitLine.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FitLine)
        self.statusbar.setObjectName("statusbar")
        FitLine.setStatusBar(self.statusbar)

        self.retranslateUi(FitLine)
        QtCore.QMetaObject.connectSlotsByName(FitLine)

    def retranslateUi(self, FitLine):
        _translate = QtCore.QCoreApplication.translate
        FitLine.setWindowTitle(_translate("FitLine", "FitLine"))
        self.generationPointsButton.setText(_translate("FitLine", "Mark points"))
        self.showPointsButton.setText(_translate("FitLine", "Show fitting data parameters"))
        self.clearButton.setText(_translate("FitLine", "Clear all"))
        self.clearLastButton.setText(_translate("FitLine", "Clear lattest fitting model"))
        self.clearFittingButton.setText(_translate("FitLine", "Clear fitting models"))
        self.loadPltButton.setText(_translate("FitLine", "Load spectrum"))
        self.saveButton.setText(_translate("FitLine", "Save as png"))
