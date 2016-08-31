# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fourthPageView.ui'
#
# Created: Fri May 20 11:22:04 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fourthPage(object):
    def setupUi(self, fourthPage):
        fourthPage.setObjectName("fourthPage")
        fourthPage.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(fourthPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelPhone = QtWidgets.QLabel(fourthPage)
        self.labelPhone.setObjectName("labelPhone")
        self.horizontalLayout.addWidget(self.labelPhone)
        self.lineEditPhone = QtWidgets.QLineEdit(fourthPage)
        self.lineEditPhone.setObjectName("lineEditPhone")
        self.horizontalLayout.addWidget(self.lineEditPhone)

        self.retranslateUi(fourthPage)
        QtCore.QMetaObject.connectSlotsByName(fourthPage)

    def retranslateUi(self, fourthPage):
        _translate = QtCore.QCoreApplication.translate
        fourthPage.setWindowTitle(_translate("fourthPage", "WizardPage"))
        self.labelPhone.setText(_translate("fourthPage", "Telefon"))

