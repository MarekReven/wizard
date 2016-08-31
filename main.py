# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue May 17 23:00:50 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtWidgets
from wizard import Ui_Wizard
from pages.firstPageView import Ui_firstPage
from pages.secondPageView import Ui_secondPage
from pages.thirdPageView import Ui_thirdPage
from pages.fourthPageView import Ui_fourthPage
from pages.fifthPageView import Ui_fifthPage
from PyQt5.QtWidgets import QApplication, QCompleter, QLineEdit
from PyQt5.QtCore import QStringListModel
from PyQt5.QtCore import Qt
import csv, sqlite3

class my_wizard(QtWidgets.QWizard, Ui_Wizard):
    def __init__(self):
        super(my_wizard, self).__init__()
        self.setupUi(self)
        self.setOption(self.IndependentPages)
        self.button(QtWidgets.QWizard.NextButton).clicked.connect(fill_last_page)
        self.button(QtWidgets.QWizard.FinishButton).clicked.connect(export_data)

class first_page(QtWidgets.QWizardPage, Ui_firstPage):
    def __init__(self):
        super(first_page, self).__init__()
        self.setupUi(self)
        self.registerField('lineEditName*', self.lineEditName)
        self.lineEditName.setPlaceholderText("Wpisz tutaj swoje imię")

class second_page(QtWidgets.QWizardPage, Ui_secondPage):
    def __init__(self):
        super(second_page, self).__init__()
        self.setupUi(self)
        self.registerField('lineEditSurname*', self.lineEditSurname)
        self.lineEditSurname.setPlaceholderText("Wpisz tutaj swoje nazwisko")

class third_page(QtWidgets.QWizardPage, Ui_thirdPage):
    def __init__(self):
        super(third_page, self).__init__()
        self.setupUi(self)
        self.registerField('lineEditCode*', self.lineEditCode)
        self.registerField('lineEditTown*', self.lineEditTown)
        self.registerField('lineEdit_2Street*', self.lineEdit_2Street)
        self.registerField('lineEdit_3Building*', self.lineEdit_3Building)
        self.lineEditCode.setPlaceholderText("Wpisz tutaj swój kod pocztowy")
        self.lineEditTown.setPlaceholderText("AUTOUZUPEŁNIANIE")
        self.lineEdit_2Street.setPlaceholderText("Wpisz tutaj ulicę")
        self.lineEdit_3Building.setPlaceholderText("Wpisz tutaj ulicę")
        self.lineEditCode.textChanged.connect(self.find_town)

    def find_town(self):

        self.code = self.lineEditCode.text()
        for row in curs.execute('SELECT miasta FROM sq_db_tbl WHERE kody = (?)',(self.code,)):
            town = str(row).strip('(),\'')
            self.lineEditTown.setText(town)

class fourth_page(QtWidgets.QWizardPage, Ui_fourthPage):
    def __init__(self):
        super(fourth_page, self).__init__()
        self.setupUi(self)
        self.registerField('lineEditPhone*', self.lineEditPhone)
        self.lineEditPhone.setPlaceholderText("Wpisz tutaj swój numer")

class fifth_page(QtWidgets.QWizardPage, Ui_fifthPage):
    def __init__(self):
        super(fifth_page, self).__init__()
        self.setupUi(self)
        self.label_5.setText(str(firstPage.lineEditName.text()))

def fill_last_page():

    name = firstPage.lineEditName.text()
    surname = secondPage.lineEditSurname.text()
    code = thirdPage.lineEditCode.text()
    town_name = thirdPage.lineEditTown.text()
    street = thirdPage.lineEdit_2Street.text()
    street_no = thirdPage.lineEdit_3Building.text()
    phone = fourthPage.lineEditPhone.text()

    fifthPage.label_5.setText(name)
    fifthPage.label_6.setText(surname)
    fifthPage.label_7.setText(code)
    fifthPage.label_11.setText(town_name)
    fifthPage.label_13.setText(street)
    fifthPage.label_15.setText(street_no)
    fifthPage.label_8.setText(phone)

    return [name, surname, code, town_name, street, street_no, phone]

def export_data():
    with open('user_data.txt', 'w') as  user_data:
        user_data.write("\n".join(fill_last_page()))

def create_db():
    conn = sqlite3.connect("sq_db.db")
    curs = conn.cursor()
    try:
        curs.execute("CREATE TABLE IF NOT EXISTS sq_db_tbl (kody TEXT, miasta TEXT);")
    except Exception as e:
        raise e
    return conn, curs

def insert_data_to_sqlite(conn, curs):

    reader = csv.reader(open('kody.csv', 'r'), delimiter=',')
    curs.execute("DELETE FROM sq_db_tbl;")
    try:
        for row in reader:
            to_db = [row[0], row[1]]
            curs.execute("INSERT INTO sq_db_tbl (kody, miasta) VALUES (?, ?);", to_db)
        conn.commit()
    except Exception as e:
        raise e
    return conn

def make_codes_list(conn):
    c = conn.cursor()
    kody = []
    for row in c.execute('SELECT kody FROM sq_db_tbl'):
        kody.append(str(row).strip("(),'"))
    return kody

def find_town(code):
    conn = sqlite3.connect("sq_db.db")
    curs = conn.cursor()
    town = curs.execute('SELECT miasta FROM sq_db_tbl WHERE kody =' + str(code))
    print(town)

def add_pages_to_wizard():
    mywizard.addPage(firstPage)
    mywizard.addPage(secondPage)
    mywizard.addPage(thirdPage)
    mywizard.addPage(fourthPage)
    mywizard.addPage(fifthPage)

def initiate_completer(codes):
    edit = thirdPage.lineEditCode
    completer = QCompleter()
    edit.setCompleter(completer)
    model = QStringListModel()
    model.setStringList(codes)
    completer.setModel(model)
    edit.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywizard = my_wizard()
    firstPage = first_page()
    secondPage = second_page()
    thirdPage = third_page()
    fourthPage = fourth_page()
    fifthPage = fifth_page()
    add_pages_to_wizard()
    conn, curs = create_db()
    codes = make_codes_list(insert_data_to_sqlite(conn, curs))
    initiate_completer(codes)
    mywizard.exec_()


