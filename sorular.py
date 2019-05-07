# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import sys,sqlite3,dbase
from PyQt5 import QtWidgets
from PyQt5 import QtGui, Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import konular
class QuestionsClass(QWidget): #we inherited from QWidget to QuestionsClass to can use sender function

    def __init__(self,sayacSoru=0,sayacKonu=0,email=""):
        super().__init__()
        self.email=email
        self.sayacSoru = sayacSoru
        self.sayacKonu=sayacKonu
        self.questionScreen = QtWidgets.QMainWindow()
        #to improve gui we used this function
        self.initGui()
        self.fixedLabel = QLabel(self.questionScreen)
        self.fixedLabel.setText("        QUESTİONS")
        self.fixedLabel.setFont(QFont("MS Gothic", 22, QFont.StyleItalic))
        self.fixedLabel.setGeometry(520, 150, 500, 60)
        self.fixedLabel.setStyleSheet( "background-image: url(C:/Users/Lenovo Ideapad/Desktop/bey.JPG);background-repeat: no-repeat;")
        self.questionScreen.setWindowTitle("Human Learning - Questions")
        self.questionScreen.setStyleSheet("background-image:url(pictures/frame1.jpg);")
        self.questionScreen.showFullScreen()

    def initGui(self):
        #this TextBrowser contains our questions
        self.AciklamaEdit = QTextBrowser(self.questionScreen)
        self.AciklamaEdit.setGeometry(290, 214, 830, 355)
        self.AciklamaEdit.setFont(QFont("Helvetica", 16, QFont.StyleItalic))
        self.AciklamaEdit.setStyleSheet("background-image: url(pictures/beyaz.png);color:DodgerBlue")
        self.AciklamaEdit.setText(self.getQuestionFromDB()[self.sayacSoru][0])
        # option A
        self.choseA = QPushButton(self.questionScreen)
        self.choseA.setText(self.getQuestionFromDB()[self.sayacSoru][1])
        self.choseA.setGeometry(300, 460, 350, 45)
        self.choseA.setStyleSheet("background-image:url(beyaz.jpg);color:DodgerBlue;font-family:'Arial';")
        self.choseA.setFont(QFont("Helvetica", 11, QFont.Bold))
        self.choseA.clicked.connect(self.changeQuestion)
        # option B
        self.choseB = QPushButton(self.questionScreen)
        self.choseB.setText(self.getQuestionFromDB()[self.sayacSoru][2])
        self.choseB.setGeometry(750, 460, 350, 45)
        self.choseB.setStyleSheet("background-image:url(beyaz.jpg);color:DodgerBlue;font-family:'Arial';")
        self.choseB.setFont(QFont("Helvetica", 11, QFont.Bold))
        self.choseB.clicked.connect(self.changeQuestion)
        # option C
        self.choseC = QPushButton(self.questionScreen)
        self.choseC.setText(self.getQuestionFromDB()[self.sayacSoru][3])
        self.choseC.setGeometry(300, 520, 350, 45)
        self.choseC.setStyleSheet("background-image:url(beyaz.jpg);color:DodgerBlue;font-family:'Arial';")
        self.choseC.setFont(QFont("Helvetica", 11, QFont.Bold))
        self.choseC.clicked.connect(self.changeQuestion)
        #option D
        self.choseD = QPushButton(self.questionScreen)
        self.choseD.setText(self.getQuestionFromDB()[self.sayacSoru][4])
        self.choseD.setGeometry(750, 520, 350, 45)
        self.choseD.setStyleSheet("background-image:url(beyaz.jpg);color:DodgerBlue;font-family:'Arial';")
        self.choseD.setFont(QFont("Helvetica", 11, QFont.Bold))
        self.choseD.clicked.connect(self.changeQuestion)

        self.infoBox=QTextBrowser(self.questionScreen)
        self.infoBox.setStyleSheet("background-image:url(pictures/beyaz.jpg);font-size:25px;color:DodgerBlue;")
        self.infoBox.setGeometry(600,620,200,45)
        self.infoBox.setText("Progress:{}".format(self.getProgressFromDB()))

    def getProgressFromDB(self):
        self.tempObje=dbase.Database(email=self.email)
        return self.tempObje.getProgressToShow()

    def changeQuestion(self):
        self.eventHandler = self.sender()
        if (self.getQuestionFromDB()[self.sayacSoru][5]==str(self.eventHandler.text())):#clicked button is equal to correct answer
                self.dbTmpObje=dbase.Database(email=self.email)
                self.dbTmpObje.updateProgressFromDB()
        self.infoBox.setText("Progress:{}".format(self.getProgressFromDB()))
        self.sayacSoru += 1
        self.AciklamaEdit.setText(self.getQuestionFromDB()[self.sayacSoru][0])
        self.choseA.setText(self.getQuestionFromDB()[self.sayacSoru][1])
        self.choseB.setText(self.getQuestionFromDB()[self.sayacSoru][2])
        self.choseC.setText(self.getQuestionFromDB()[self.sayacSoru][3])
        self.choseD.setText(self.getQuestionFromDB()[self.sayacSoru][4])
        if(self.sayacSoru%10==0):
            self.goToTutorial(self.sayacSoru)

    def getQuestionFromDB(self): #to change question and to take right answer
        self.dbObjecttoQ=dbase.Database()
        return self.dbObjecttoQ.takeQuesFromDBase()

    def goToTutorial(self,sayi):
        self.questionScreen.destroy()
        self.tutObject=konular.TutorialClass(sayacKonu=self.sayacKonu,sayacSoru=self.sayacSoru,email=self.email)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    questionObject = QuestionsClass(email="hasan@hl.com")
    sys.exit(app.exec())