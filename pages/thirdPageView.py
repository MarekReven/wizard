# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thirdPageView.ui'
#
# Created: Fri May 20 11:21:21 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_thirdPage(object):
    def setupUi(self, thirdPage):
        thirdPage.setObjectName("thirdPage")
        thirdPage.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(thirdPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(thirdPage)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditCode = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditCode.setObjectName("lineEditCode")
        self.gridLayout.addWidget(self.lineEditCode, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditTown = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditTown.setObjectName("lineEditTown")
        self.gridLayout.addWidget(self.lineEditTown, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2Street = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2Street.setObjectName("lineEdit_2Street")
        self.gridLayout.addWidget(self.lineEdit_2Street, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)
        self.lineEdit_3Building = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3Building.setObjectName("lineEdit_3Building")
        self.gridLayout.addWidget(self.lineEdit_3Building, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(thirdPage)
        QtCore.QMetaObject.connectSlotsByName(thirdPage)

    def retranslateUi(self, thirdPage):
        _translate = QtCore.QCoreApplication.translate
        thirdPage.setWindowTitle(_translate("thirdPage", "WizardPage"))
        self.groupBox.setTitle(_translate("thirdPage", "Adres"))
        self.label.setText(_translate("thirdPage", "Kod pocztowy:"))
        self.label_2.setText(_translate("thirdPage", "Miasto:"))
        self.label_3.setText(_translate("thirdPage", "Ulica:"))
        self.label_4.setText(_translate("thirdPage", "Nr budynku/mieszkania:"))

