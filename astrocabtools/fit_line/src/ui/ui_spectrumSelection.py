# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrumSelection.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_spectrumSelection(object):
    def setupUi(self, spectrumSelection):
        spectrumSelection.setObjectName("spectrumSelection")
        spectrumSelection.setWindowModality(QtCore.Qt.NonModal)
        spectrumSelection.resize(450, 169)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(spectrumSelection.sizePolicy().hasHeightForWidth())
        spectrumSelection.setSizePolicy(sizePolicy)
        spectrumSelection.setAutoFillBackground(False)
        spectrumSelection.setSizeGripEnabled(False)
        spectrumSelection.setModal(False)
        self.gridLayout_2 = QtWidgets.QGridLayout(spectrumSelection)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(spectrumSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.pathLabel = QtWidgets.QLabel(spectrumSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathLabel.sizePolicy().hasHeightForWidth())
        self.pathLabel.setSizePolicy(sizePolicy)
        self.pathLabel.setObjectName("pathLabel")
        self.gridLayout.addWidget(self.pathLabel, 4, 0, 1, 1)
        self.wUnitsCombobox = QtWidgets.QComboBox(spectrumSelection)
        self.wUnitsCombobox.setEnabled(True)
        self.wUnitsCombobox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.wUnitsCombobox.setObjectName("wUnitsCombobox")
        self.wUnitsCombobox.addItem("")
        self.wUnitsCombobox.addItem("")
        self.wUnitsCombobox.addItem("")
        self.gridLayout.addWidget(self.wUnitsCombobox, 7, 1, 1, 1)
        self.fluxColumnLineEdit = QtWidgets.QLineEdit(spectrumSelection)
        self.fluxColumnLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fluxColumnLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fluxColumnLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.fluxColumnLineEdit.setObjectName("fluxColumnLineEdit")
        self.gridLayout.addWidget(self.fluxColumnLineEdit, 6, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(spectrumSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(spectrumSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(spectrumSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(spectrumSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)
        self.redshiftLineEdit = QtWidgets.QLineEdit(spectrumSelection)
        self.redshiftLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redshiftLineEdit.sizePolicy().hasHeightForWidth())
        self.redshiftLineEdit.setSizePolicy(sizePolicy)
        self.redshiftLineEdit.setAutoFillBackground(False)
        self.redshiftLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.redshiftLineEdit.setObjectName("redshiftLineEdit")
        self.gridLayout.addWidget(self.redshiftLineEdit, 5, 1, 1, 1)
        self.redshiftLabel = QtWidgets.QLabel(spectrumSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redshiftLabel.sizePolicy().hasHeightForWidth())
        self.redshiftLabel.setSizePolicy(sizePolicy)
        self.redshiftLabel.setObjectName("redshiftLabel")
        self.gridLayout.addWidget(self.redshiftLabel, 5, 0, 1, 1)
        self.extensionSelectCombobox = QtWidgets.QComboBox(spectrumSelection)
        self.extensionSelectCombobox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.extensionSelectCombobox.setObjectName("extensionSelectCombobox")
        self.extensionSelectCombobox.addItem("")
        self.extensionSelectCombobox.addItem("")
        self.gridLayout.addWidget(self.extensionSelectCombobox, 3, 1, 1, 1)
        self.waveColumnLineEdit = QtWidgets.QLineEdit(spectrumSelection)
        self.waveColumnLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.waveColumnLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.waveColumnLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.waveColumnLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.waveColumnLineEdit.setObjectName("waveColumnLineEdit")
        self.gridLayout.addWidget(self.waveColumnLineEdit, 6, 1, 1, 1)
        self.fUnitsCombobox = QtWidgets.QComboBox(spectrumSelection)
        self.fUnitsCombobox.setEnabled(True)
        self.fUnitsCombobox.setObjectName("fUnitsCombobox")
        self.fUnitsCombobox.addItem("")
        self.fUnitsCombobox.addItem("")
        self.fUnitsCombobox.addItem("")
        self.fUnitsCombobox.addItem("")
        self.fUnitsCombobox.addItem("")
        self.fUnitsCombobox.addItem("")
        self.fUnitsCombobox.addItem("")
        self.fUnitsCombobox.addItem("")
        self.gridLayout.addWidget(self.fUnitsCombobox, 7, 3, 1, 1)
        self.fileButton = QtWidgets.QPushButton(spectrumSelection)
        self.fileButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileButton.sizePolicy().hasHeightForWidth())
        self.fileButton.setSizePolicy(sizePolicy)
        self.fileButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fileButton.setObjectName("fileButton")
        self.gridLayout.addWidget(self.fileButton, 3, 2, 1, 2)
        self.pathInputLabel = QtWidgets.QLabel(spectrumSelection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathInputLabel.sizePolicy().hasHeightForWidth())
        self.pathInputLabel.setSizePolicy(sizePolicy)
        self.pathInputLabel.setText("")
        self.pathInputLabel.setObjectName("pathInputLabel")
        self.gridLayout.addWidget(self.pathInputLabel, 4, 1, 1, 3)
        self.cancelButton = QtWidgets.QPushButton(spectrumSelection)
        self.cancelButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 9, 0, 1, 2)
        self.acceptButton = QtWidgets.QPushButton(spectrumSelection)
        self.acceptButton.setEnabled(False)
        self.acceptButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.acceptButton.setObjectName("acceptButton")
        self.gridLayout.addWidget(self.acceptButton, 9, 2, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(spectrumSelection)
        self.cancelButton.clicked.connect(spectrumSelection.reject)
        self.acceptButton.clicked.connect(spectrumSelection.accept)
        QtCore.QMetaObject.connectSlotsByName(spectrumSelection)

    def retranslateUi(self, spectrumSelection):
        _translate = QtCore.QCoreApplication.translate
        spectrumSelection.setWindowTitle(_translate("spectrumSelection", "spectrumSelection"))
        self.label_5.setText(_translate("spectrumSelection", "File extension"))
        self.pathLabel.setText(_translate("spectrumSelection", "Path: "))
        self.wUnitsCombobox.setCurrentText(_translate("spectrumSelection", "um"))
        self.wUnitsCombobox.setItemText(0, _translate("spectrumSelection", "um"))
        self.wUnitsCombobox.setItemText(1, _translate("spectrumSelection", "angstroms"))
        self.wUnitsCombobox.setItemText(2, _translate("spectrumSelection", "nm"))
        self.fluxColumnLineEdit.setPlaceholderText(_translate("spectrumSelection", "1"))
        self.label_2.setText(_translate("spectrumSelection", "Flux units"))
        self.label_4.setText(_translate("spectrumSelection", "Flux column"))
        self.label_3.setText(_translate("spectrumSelection", "Wavelength column"))
        self.label.setText(_translate("spectrumSelection", "Wavelength units"))
        self.redshiftLineEdit.setPlaceholderText(_translate("spectrumSelection", "0.0"))
        self.redshiftLabel.setText(_translate("spectrumSelection", "Redshift: "))
        self.extensionSelectCombobox.setItemText(0, _translate("spectrumSelection", "Ascii file (.txt)"))
        self.extensionSelectCombobox.setItemText(1, _translate("spectrumSelection", "Fits file (.fits)"))
        self.waveColumnLineEdit.setPlaceholderText(_translate("spectrumSelection", "0"))
        self.fUnitsCombobox.setItemText(0, _translate("spectrumSelection", "erg/s/cm2/um"))
        self.fUnitsCombobox.setItemText(1, _translate("spectrumSelection", "Jy"))
        self.fUnitsCombobox.setItemText(2, _translate("spectrumSelection", "mJy"))
        self.fUnitsCombobox.setItemText(3, _translate("spectrumSelection", "uJy"))
        self.fUnitsCombobox.setItemText(4, _translate("spectrumSelection", "W/m2/Hz"))
        self.fUnitsCombobox.setItemText(5, _translate("spectrumSelection", "erg/s/cm2/Hz"))
        self.fUnitsCombobox.setItemText(6, _translate("spectrumSelection", "W/m2/Angstroms"))
        self.fUnitsCombobox.setItemText(7, _translate("spectrumSelection", "erg/s/cm2/Angstroms"))
        self.fileButton.setText(_translate("spectrumSelection", "Select File"))
        self.cancelButton.setText(_translate("spectrumSelection", "Cancel"))
        self.acceptButton.setText(_translate("spectrumSelection", "Accept"))

