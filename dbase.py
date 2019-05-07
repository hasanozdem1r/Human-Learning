import sqlite3 as sql
import re,urllib.parse,urllib.request

class Database(object):
    def __init__(self,name_sname=None,email=None,pword=None,cpword=None,subject=None,link=""):
        #when constructor started,system connect to database
        self.connect = sql.connect("database/informations.sqlite")
        self.cursor = self.connect.cursor()

        self.name_sname=name_sname
        self.email=email
        self.pword=pword
        self.cpword=cpword
        self.subject=subject
        self.link=link

    def checkInfoToDBForLoginMenu(self): #this function is being used by LoginClass
        self.cursor.execute("SELECT * from 'bilgiler' WHERE Email=?",(self.email,)) #this code check in database for email
        self.data_informations=self.cursor.fetchall() #bilgiler(Name Surname,Email,Password,CPassword,Proggress,Hierarchy)


        if(len(self.data_informations)==0):
            self.listToCheck = [True, "User"]
            return self.listToCheck
        elif (self.data_informations[0][1]==self.email) and self.data_informations[0][2]==self.pword:
            self.listToCheck = [True,self.data_informations[0][5]]
            self.listToCheck[0]=False
            return self.listToCheck
        else:
            self.listToCheck = [True, self.data_informations[0][5]]
            return self.listToCheck

    def addInfoToDBForCAccountMenu(self): #this function is being used by CAccountClass
        self.response = False
        self.cursor.execute("SELECT * FROM bilgiler ")
        self.data_informations=self.cursor.fetchall() #bilgiler(Name Surname,Email,Password,CPassword,Progress)
        self.elementsList = [self.name_sname,self.email,self.pword,self.cpword,0,"User"]
        if (self.pword != self.cpword):
            self.connect.close()
            return True
        elif(self.name_sname=="" or self.pword=="" or self.cpword=="" or self.email==""):
            self.connect.close()
            return True
        for i in self.data_informations:
            if (i[1]==self.email):
                self.response=True
                self.connect.close()
                return True
                break
        self.response = False
        self.cursor.execute("INSERT INTO bilgiler VALUES(?,?,?,?,?,?)",self.elementsList)
        self.connect.commit()
        self.connect.close()
        return False

    def takeSubjectFromDBase(self): #this function is being used by TutorailClass
        self.cursor.execute("SELECT * FROM tutorials")
        self.dataTutorials = self.cursor.fetchall()
        self.connect.close()
        return self.dataTutorials

    def takeQuesFromDBase(self):#this function is being used by QuestionClass
        self.cursor.execute("SELECT * FROM questions")
        self.dataQuestions=self.cursor.fetchall()
        self.connect.close()
        return self.dataQuestions

    def getEmailandProgressFromDB(self): #this function is being used by adminClass
        self.cursor.execute("SELECT * FROM bilgiler")
        self.mail_progress=self.cursor.fetchall()
        self.connect.close()
        return self.mail_progress

    def addTutorialToDB(self): #this function is being used by adminClass
        temp_liste=[self.subject] #we used  this list because sqlite3 doesnt accept string parameter to execute something
        if self.subject=="":
            self.connect.close()
            return True
        self.cursor.execute("INSERT INTO tutorials VALUES (?)",temp_liste)
        self.connect.commit()
        self.connect.close()
        return True

    def deleteUsFromDB(self):
        temp_list=[self.email] #we used  this list because sqlite3 doesnt accept string parameter to execute something
        self.cursor.execute("DELETE FROM 'bilgiler' WHERE Email=?",temp_list)
        self.connect.commit()
        self.connect.close()

    def addTutoriailWithLinkToDB(self):#this function just supports links of w3schools
        if self.link =="":
            self.link="https://www.w3schools.com/python/python_lambda.asp"
        self.values = {'s': 'basics', 'submit': 'search'}
        self.data = urllib.parse.urlencode(self.values)
        self.data = self.data.encode('utf-8')
        TAG_RE = re.compile(r'<[^>]+>')
        cleanCode = lambda text: TAG_RE.sub('', text) #to clean HTML tags
        self.url = str(self.link)
        self.req = urllib.request.Request(str(self.link), self.data)
        self.response = urllib.request.urlopen(self.req)
        self.responseData = self.response.read()
        # --------------
        self.paragraphs = re.findall(r'<p>(.*?)</p>',str(self.responseData))  # bu iki tag arasında olan ne varsa çeker .*? sağlıyor bu işlemi
        self.withoutHTML = ""
        for eachParagrap in self.paragraphs:
            self.withoutHTML += (cleanCode(eachParagrap))
        self.cursor.execute("SELECT * FROM tutorials")
        self.tempData=self.cursor.fetchall()
        for i in self.tempData:
            if self.withoutHTML==i[0]:#if database contains value of withouthtml
                self.connect.close()
                return True
        if self.withoutHTML=="":#if value of withouthtml equal NULL
            self.connect.close()
            return True
        self.tempList=[self.withoutHTML]
        self.cursor.execute("INSERT INTO tutorials VALUES (?)",self.tempList)
        self.connect.commit()
        self.connect.close()

    def updateProgressFromDB(self):
        self.cursor.execute("SELECT Progress FROM bilgiler WHERE Email=?",[self.email])
        if (len(self.cursor.fetchall())==0):
            return True
        self.cursor.execute("SELECT Progress FROM bilgiler WHERE Email=?",[self.email])
        self.currentProgressOfUser=self.cursor.fetchall()
        self.currentProgressOfUser=int(self.currentProgressOfUser[0][0])
        self.currentProgressOfUser+=5
        self.cursor.execute("UPDATE bilgiler SET Progress=? WHERE Email=?",[self.currentProgressOfUser,self.email])
        self.connect.commit()

    def getProgressToShow(self):
        self.cursor.execute("SELECT Progress FROM bilgiler WHERE Email=?",(self.email,))
        return self.cursor.fetchall()[0][0]

if __name__=="__main__":
    dbObject=Database(email="hasan@hl.com")
    dbObject.getProgress()


