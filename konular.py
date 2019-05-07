from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5 import QtWidgets
from PyQt5 import QtGui, Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import sys
import sorular,dbase

class TutorialClass():

    def __init__(self,sayacKonu=0,sayacSoru=0,email="       "):
        self.email=email
        self.sayacKonu=sayacKonu
        self.sayacSoru=sayacSoru
        self.acıklama = QtWidgets.QMainWindow()
        self.imagePAth = "pictures/hul.jpg"
        # to improve gui we used this function
        self.initGui()
        self.acıklama.setWindowTitle("Human Learning - Tutorials")
        self.acıklama.setStyleSheet("background-image: url(pictures/frame1.jpg);")
        self.acıklama.showFullScreen()  # to show maxsize

    def initGui(self):
        self.dbObjectT = dbase.Database()

        #We write text in this QTextBrowser
        self.aciklamaEdit = QTextBrowser(self.acıklama)
        self.aciklamaEdit.setGeometry(290, 214, 830, 355)
        self.aciklamaEdit.setFont(QFont("Monoscaped", 17, QFont.StyleItalic))
        self.aciklamaEdit.setStyleSheet("background-image:url(beyaz.jpg);color:Black;font-family:'Arial';")
        self.aciklamaEdit.setText(str(self.dbObjectT.takeSubjectFromDBase()[self.sayacKonu][0]))

        #we created this button to switch questions
        self.soruyaGec = QPushButton(self.acıklama)
        self.soruyaGec.setGeometry(630, 600, 120, 90)
        self.soruyaGec.setStyleSheet("background-image: url(pictures/lets.jpg);")
        self.soruyaGec.clicked.connect(self.getTutorialFromDB)

    def getTutorialFromDB(self):
        self.dbObjectT = dbase.Database()
        self.sayacKonu+=1
        self.goToQuestion()

    def goToQuestion(self):
        self.acıklama.destroy()
        self.questionObje = sorular.QuestionsClass(sayacSoru=self.sayacSoru,sayacKonu=self.sayacKonu,email=self.email)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tutorialObject = TutorialClass(email="p1@hl.com")
    sys.exit(app.exec())