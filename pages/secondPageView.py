# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondPageView.ui'
#
# Created: Fri May 20 11:20:28 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_secondPage(object):
    def setupUi(self, secondPage):
        secondPage.setObjectName("secondPage")
        secondPage.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(secondPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelSurname = QtWidgets.QLabel(secondPage)
        self.labelSurname.setObjectName("labelSurname")
        self.horizontalLayout.addWidget(self.labelSurname)
        self.lineEditSurname = QtWidgets.QLineEdit(secondPage)
        self.lineEditSurname.setObjectName("lineEditSurname")
        self.horizontalLayout.addWidget(self.lineEditSurname)

        self.retranslateUi(secondPage)
        QtCore.QMetaObject.connectSlotsByName(secondPage)

    def retranslateUi(self, secondPage):
        _translate = QtCore.QCoreApplication.translate
        secondPage.setWindowTitle(_translate("secondPage", "WizardPage"))
        self.labelSurname.setText(_translate("secondPage", "Nazwisko:"))

