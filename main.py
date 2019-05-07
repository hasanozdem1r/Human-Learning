import ilkekran
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import sqlite3 as sql
#from PyQt5.QtCore import QSize
from PyQt5 import QtWidgets
from PyQt5 import QtGui,Qt
from PyQt5 import QtCore

class mainClass():
    def __init__(self):
        app = QApplication(sys.argv)
        firstScreenObject =ilkekran.WelcomeScreenClass()
        sys.exit(app.exec())

if __name__=="__main__":
    mainObject=mainClass()