from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3 as sql
#from PyQt5.QtCore import QSize
from PyQt5 import QtWidgets
from PyQt5 import QtGui, Qt
from PyQt5 import QtCore
import sys,dbase
class adminClass():

    def __init__(self):
        self.adminScreen=QtWidgets.QMainWindow()
        self.adminScreen.setWindowTitle("Human Learning - Manager")
        self.adminScreen.setStyleSheet("background-image:url(pictures/adminpage.jpg);")
        self.setUI()
        self.adminScreen.showFullScreen()

    def setUI(self):

        "to add information with typing"
        self.editInfo=QTextEdit(self.adminScreen)
        self.editInfo.setGeometry(150,220,220,200)
        self.btnSendTutorialToDB=QPushButton("Add Tutorial with Typing",self.adminScreen)
        self.btnSendTutorialToDB.setGeometry(160,180,200,30)
        self.btnSendTutorialToDB.clicked.connect(self.sendTutorialToDB)

        "to show user"
        self.listUserEdit=QTextBrowser(self.adminScreen)
        self.listUserEdit.setGeometry(1000,220,220,200)
        self.listUserEdit.setStyleSheet("color:black;text-decoration:underline;")
        self.btnToshowUser=QPushButton(self.adminScreen)
        self.btnToshowUser.setGeometry(1010,180,200,30)
        self.btnToshowUser.setText("Show all accounts")
        self.btnToshowUser.clicked.connect(self.clicked_getUserFromDB)

        "to delete user"
        self.btnToDelUser=QPushButton(self.adminScreen)
        self.btnToDelUser.setGeometry(1020,480,200,30)
        self.btnToDelUser.setText("Delete an Account")
        self.btnToDelUser.clicked.connect(self.delUserFromDB)
        self.editDelUser=QLineEdit(self.adminScreen)
        self.editDelUser.setGeometry(1010,520,220,30)

        "to add tutorial with link"
        self.btnSendLink=QPushButton(self.adminScreen)
        self.btnSendLink.setGeometry(160,480,200,30)
        self.btnSendLink.setText("Add Tutorial with Link")
        self.btnSendLink.clicked.connect(self.sendTutorialWithLink)
        self.getLink=QLineEdit(self.adminScreen)
        self.getLink.setGeometry(150,520,220,30)

    # if something goes wrong
    def warningMessage(self):
        self.mbox = QMessageBox(self.adminScreen)
        self.mbox.setText("Not you?")
        self.mbox.setStyleSheet("backgroung-image:url{pictures/beyaz.jpg};color:orange;background-color:purple;")
        self.mbox.setInformativeText("Please try again.")  # to give detailed information
        self.mbox.setWindowTitle("Warning !!")  # message box title
        self.mbox.setDetailedText("The password or mail address that you've entered is incorrect.")  # pop-up window detailed information
        self.mbox.setIcon(QMessageBox.Warning)
        self.mbox.exec()

    def delUserFromDB(self):
        # self.editDelUser.text("https://www.w3schools.com/python/python_lambda.asp")
        self.dbObject=dbase.Database(email=self.editDelUser.text())
        self.dbObject.deleteUsFromDB()
        self.editDelUser.clear()
        self.clicked_getUserFromDB()

    def clicked_getUserFromDB(self):
        dbObje = dbase.Database()
        self.listUserEdit.clear()
        for i in dbObje.getEmailandProgressFromDB():
            tempStr = "Email:{} \nProgress:{} \nHierarchy:{}".format(i[1], i[4], i[5])
            self.listUserEdit.append(tempStr)
            self.listUserEdit.append("")

    def sendTutorialToDB(self):
        dbObje=dbase.Database(subject=self.editInfo.toPlainText())
        dbObje.addTutorialToDB()
        self.editInfo.clear()

    def sendTutorialWithLink(self):
        self.dbOb1=dbase.Database(link=self.getLink.text())
        self.dbOb1.addTutoriailWithLinkToDB()
        self.getLink.clear()

if __name__=="__main__":
    app=QApplication(sys.argv)
    adminObject=adminClass()
    sys.exit(app.exec())
