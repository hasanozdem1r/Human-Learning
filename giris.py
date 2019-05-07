from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import sqlite3
from PyQt5.QtCore import QSize
from PyQt5 import QtWidgets
from PyQt5 import QtGui, Qt
from PyQt5 import QtCore
import konular,adminFile,dbase

class LoginClass():
    def __init__(self):
        self.loginScreen = QMainWindow()
        self.imagePAth = "pictures/hl1.jpg"
        # to improve gui we used this function
        self.initGui()
        self.loginScreen.setWindowTitle("Human Learning - Login")
        self.loginScreen.setStyleSheet("background-image:url(pictures/water.jpg)")
        self.loginScreen.showFullScreen()  # to show maxsize

    def initGui(self):

        # create a tag to write email
        self.mailTag = QLabel(self.loginScreen)
        self.mailTag.setText("EMAİL")
        self.mailTag.setGeometry(185, 290, 100, 100)
        self.mailTag.setStyleSheet("color:white")

        # creata a tag to write password
        self.pwordTag = QLabel(self.loginScreen)
        self.pwordTag.setText("PASSWORD")
        self.pwordTag.setGeometry(185, 350, 100, 100)
        self.pwordTag.setStyleSheet("color:white")
        # ---------------------------------------------------------------------
        # create a label fır background
        self.image = QImage(self.imagePAth)
        self.label = QLabel(self.loginScreen)
        self.label.setGeometry(210, 60, 200, 200)
        self.label.setStyleSheet("background-color:#6e6e6e")
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)

        # create an email field
        self.edit_email = QLineEdit(self.loginScreen)
        self.edit_email.setFont(QFont("MS Gothic", 12, QFont.DemiBold))
        self.edit_email.setGeometry(180, 350, 250, 40)
        self.edit_email.setStyleSheet("color:white;font:16px")

        # create a password field
        self.edit_password = QLineEdit(self.loginScreen)
        self.edit_password.setFont(QFont("MS Gothic", 12, QFont.DemiBold))
        self.edit_password.setGeometry(180, 410, 250, 40)
        self.edit_password.setEchoMode(QLineEdit.Password)
        self.edit_password.setStyleSheet("color:white;font:16px")
        # create the account button
        self.btn_login = QPushButton(self.loginScreen)
        self.btn_login.setGeometry(180, 530, 250, 40)
        self.btn_login.setStyleSheet("background-color:green")
        self.btn_login.setText("LOGİN")
        self.btn_login.setStyleSheet("color:white;font:16px")
        # functions
        self.btn_login.clicked.connect(self.clicked_checkDatabase)
        self.btn_login.clicked.connect(self.edit_email.clear)
        self.btn_login.clicked.connect(self.edit_password.clear)

    # check user informations
    def clicked_checkDatabase(self):
        self.dBaseObje=dbase.Database("",self.edit_email.text(),self.edit_password.text(),"")
        self.dBaseObje.checkInfoToDBForLoginMenu
        if(self.dBaseObje.checkInfoToDBForLoginMenu()[0]):
            self.warningMessage()
        elif self.dBaseObje.checkInfoToDBForLoginMenu()[1]=="User":
            self.goToTutorial()
        elif self.dBaseObje.checkInfoToDBForLoginMenu()[1]=="Manager":
            self.goToAdmin()

    # if something goes wrong
    def warningMessage(self):
        self.mbox = QMessageBox(self.loginScreen)
        self.mbox.setText("Not you?")
        self.mbox.setStyleSheet("backgroung-image:url{pictures/beyaz.jpg};color:orange;background-color:purple;")
        self.mbox.setInformativeText("Please try again.")  # to give detailed information
        self.mbox.setWindowTitle("Warning !!")  # message box title
        self.mbox.setDetailedText("The password or mail address that you've entered is incorrect.")  # pop-up window detailed information
        self.mbox.setIcon(QMessageBox.Warning)
        self.mbox.exec()

    # this functions switch page
    def goToTutorial(self):
        self.loginScreen.destroy()
        self.TutorialOb = konular.TutorialClass(email=self.edit_email.text())

    # this functions switch page
    def goToAdmin(self):
        self.loginScreen.destroy()
        self.adminObject=adminFile.adminClass()
        self.loginScreen.destroy()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginObject = LoginClass()
    sys.exit(app.exec())