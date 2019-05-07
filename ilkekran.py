from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import giris,hesap_ac

class WelcomeScreenClass():
    def __init__(self):
        super().__init__()
        self.firstScreen = QMainWindow()
        self.firstScreen.setWindowTitle("Human Learning")
        self.firstScreen.setStyleSheet("background-image:url(pictures/firstwithlogo.jpg);")
        self.setUI()
        self.firstScreen.showFullScreen()

    def setUI(self):
        #if you wannt to switch for login page,users should push this button
        self.chooseLoginBtn = QPushButton(self.firstScreen)
        self.chooseLoginBtn.setText("Login")
        self.chooseLoginBtn.setGeometry(196, 600, 200, 80)
        self.chooseLoginBtn.setStyleSheet("color:white;font:16px")
        self.chooseLoginBtn.clicked.connect(self.goToLogin)
        #if you wannt to switch for create account page,users should push this button
        self.chooseCAccountBtn = QPushButton(self.firstScreen)
        self.chooseCAccountBtn.setText("Create an Account")
        self.chooseCAccountBtn.setGeometry(1016, 600, 200, 80)
        self.chooseCAccountBtn.setStyleSheet("color:white;font:16px")
        self.chooseCAccountBtn.clicked.connect(self.goToCAccount)

    #we use this method of switch page to go page of login
    def goToLogin(self):
        self.firstScreen.destroy()
        self.loginObject=giris.LoginClass()

    # we use this method of switch page to go page of create account
    def goToCAccount(self):
        self.firstScreen.destroy()
        self.cAccountObjecy=hesap_ac.createAccountClass()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    firstObject = WelcomeScreenClass()
    sys.exit(app.exec())