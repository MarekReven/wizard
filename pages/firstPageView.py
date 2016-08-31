# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstPageView.ui'
#
# Created: Fri May 20 11:18:28 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_firstPage(object):
    def setupUi(self, firstPage):
        firstPage.setObjectName("firstPage")
        firstPage.resize(400, 200)
        self.horizontalLayout = QtWidgets.QHBoxLayout(firstPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelName = QtWidgets.QLabel(firstPage)
        self.labelName.setObjectName("labelName")
        self.horizontalLayout.addWidget(self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(firstPage)
        self.lineEditName.setObjectName("lineEditName")
        self.horizontalLayout.addWidget(self.lineEditName)

        self.retranslateUi(firstPage)
        QtCore.QMetaObject.connectSlotsByName(firstPage)

    def retranslateUi(self, firstPage):
        _translate = QtCore.QCoreApplication.translate
        firstPage.setWindowTitle(_translate("firstPage", "WizardPage"))
        self.labelName.setText(_translate("firstPage", "Imie:"))

