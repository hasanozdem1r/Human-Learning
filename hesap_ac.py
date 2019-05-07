from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import sqlite3 as sql
#from PyQt5.QtCore import QSize
from PyQt5 import QtWidgets
from PyQt5 import QtGui, Qt
from PyQt5 import QtCore
import giris,dbase

class createAccountClass():

    def __init__(self):
        # self.app = QtWidgets.QApplication(sys.argv)
        self.cAccountScreen = QtWidgets.QMainWindow()
        self.imagePAth = "pictures/hl1.jpg"

        self.initGui()  # function

        self.cAccountScreen.setWindowTitle("Human Learning - Create an Account")
        self.cAccountScreen.setStyleSheet("background-image:url(pictures/water.jpg)")
        self.cAccountScreen.showFullScreen()  # to show maxsize

    def initGui(self):
        # creata a tag to write name and surname
        self.unameLbl = QtWidgets.QLabel(self.cAccountScreen)
        self.unameLbl.setText("NAME AND SURNAME")
        self.unameLbl.setGeometry(185, 230, 100, 100)
        self.unameLbl.setStyleSheet("color:white")

        # create a tag to write email
        self.mailLbl = QtWidgets.QLabel(self.cAccountScreen)
        self.mailLbl.setText("EMAİL")
        self.mailLbl.setGeometry(185, 290, 100, 100)
        self.mailLbl.setStyleSheet("color:white")

        # creata a tag to write password
        self.pwordLbl = QtWidgets.QLabel(self.cAccountScreen)
        self.pwordLbl.setText("PASSWORD")
        self.pwordLbl.setGeometry(185, 350, 100, 100)
        self.pwordLbl.setStyleSheet("color:white")

        # creata a tag to write confirm password
        self.confirm_pwordLbl = QtWidgets.QLabel(self.cAccountScreen)
        self.confirm_pwordLbl.setText("CONFIRM PASSWORD")
        self.confirm_pwordLbl.setGeometry(185, 410, 150, 100)
        self.confirm_pwordLbl.setStyleSheet("color:white")

        # create a label for background image
        self.image = QtGui.QImage(self.imagePAth)
        self.label = QtWidgets.QLabel(self.cAccountScreen)
        self.label.setGeometry(210, 60, 200, 200)
        self.label.setStyleSheet("background-color:#6e6e6e")
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)

        # create a name surname field
        self.name_surnameEdit = QtWidgets.QLineEdit(self.cAccountScreen)
        self.name_surnameEdit.setGeometry(180, 290, 250, 40)
        self.name_surnameEdit.setStyleSheet("color:white;font:16px")

        # create an email field
        self.emailEdit = QtWidgets.QLineEdit(self.cAccountScreen)
        self.emailEdit.setGeometry(180, 350, 250, 40)
        self.emailEdit.setStyleSheet("color:white;font:16px")


        # create a password field
        self.passwordEdit = QtWidgets.QLineEdit(self.cAccountScreen)
        self.passwordEdit.setGeometry(180, 410, 250, 40)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.setStyleSheet("color:white;font:16px")
        # create a confirm password field
        self.confirmpasswordEdit = QtWidgets.QLineEdit(self.cAccountScreen)
        self.confirmpasswordEdit.setGeometry(180, 470, 250, 40)
        self.confirmpasswordEdit.setEchoMode(QLineEdit.Password)
        self.confirmpasswordEdit.setStyleSheet("color:white;font:16px")

        # create the account button
        self.createAccountBtn = QtWidgets.QPushButton(self.cAccountScreen)
        self.createAccountBtn.setGeometry(180, 530, 250, 40)
        self.createAccountBtn.setText("CREATE AN ACCOUNT")
        self.createAccountBtn.setStyleSheet("color:white;font:16px")

        # button properties
        self.createAccountBtn.clicked.connect(self.clicked_addInformationToDatabase)
        self.createAccountBtn.clicked.connect(self.name_surnameEdit.clear)
        self.createAccountBtn.clicked.connect(self.emailEdit.clear)
        self.createAccountBtn.clicked.connect(self.passwordEdit.clear)
        self.createAccountBtn.clicked.connect(self.confirmpasswordEdit.clear)

    def clicked_addInformationToDatabase(self):
        self.dbObje=dbase.Database(self.name_surnameEdit.text(),self.emailEdit.text(),
                                  self.passwordEdit.text(),self.confirmpasswordEdit.text())
        self.response=self.dbObje.addInfoToDBForCAccountMenu()
        if(self.response):
             self.warningMessage()
             return None
        self.goToLogin()

    # if something goes wrong
    def warningMessage(self):
        self.mbox = QMessageBox(self.cAccountScreen)
        self.mbox.setText("Not you?")
        self.mbox.setStyleSheet("backgroung-image:url{pictures/beyaz.jpg};color:orange;background-color:purple;")
        self.mbox.setInformativeText("Please try again.")  # to give detailed information
        self.mbox.setWindowTitle("Warning !!") # message box title
        self.mbox.setDetailedText("That email or password is taken or doesn't match your passwords.Try again.")  # pop-up window detailed information
        self.mbox.setIcon(QMessageBox.Warning)
        self.mbox.setStyleSheet("color:white;font:14px")
        self.mbox.exec()  # kullanıcı değer girene kadar devam etmesini istiyorsak böyle yaparız.

    # we use this methods to switch page
    def goToLogin(self):
        self.cAccountScreen.destroy()
        self.loginObject=giris.LoginClass()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    CAccountObject = createAccountClass()
    sys.exit(app.exec())
