from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import webbrowser
import random
import win32com.client
import time
import datetime
import urllib.request
import bs4 as bs
import subprocess
import re
import nltk
import speech_recognition as sr


class Ui_CheeBotWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.cheetts = win32com.client.Dispatch("SAPI.SpVoice")
        self.time1 = datetime.datetime.now().time()
        self.Clukk = time.asctime(time.localtime())
        self.Clocktime = self.Clukk[11:16]
        self.Goodtime = ""
        self.r = sr.Recognizer()

#UI
    def setupUi(self, CheeBotWindow):
        CheeBotWindow.setObjectName("CheeBotWindow")
        CheeBotWindow.resize(273, 373)
        CheeBotWindow.setMaximumSize(QtCore.QSize(273, 398))
        self.centralwidget = QtWidgets.QWidget(CheeBotWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 251, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BotLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andy")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.BotLabel.setFont(font)
        self.BotLabel.setObjectName("BotLabel")
        self.verticalLayout.addWidget(self.BotLabel)
        self.BotLog = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andy")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BotLog.setFont(font)
        self.BotLog.setStatusTip("")
        self.BotLog.setReadOnly(True)
        self.BotLog.setObjectName("BotLog")
        self.verticalLayout.addWidget(self.BotLog)
        self.BotInput = QtWidgets.QLineEdit(self.centralwidget)
        self.BotInput.setGeometry(QtCore.QRect(10, 290, 251, 31))
        self.BotInput.returnPressed.connect(self.heylisten)
        font = QtGui.QFont()
        font.setFamily("Andy")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.BotInput.setFont(font)
        self.BotInput.setObjectName("lineEdit")
        CheeBotWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CheeBotWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 273, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        CheeBotWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CheeBotWindow)
        self.statusbar.setObjectName("statusbar")
        CheeBotWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(CheeBotWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHalp = QtWidgets.QAction(CheeBotWindow)
        self.actionHalp.setObjectName("actionHalp")
        self.menuMenu.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHalp)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(CheeBotWindow)
        QtCore.QMetaObject.connectSlotsByName(CheeBotWindow)

    def retranslateUi(self, CheeBotWindow):
        _translate = QtCore.QCoreApplication.translate
        CheeBotWindow.setWindowTitle(_translate("CheeBotWindow", "CheeBot Alpha"))
        self.BotLabel.setText(_translate("CheeBotWindow", "CheeBot Alpha"))
        self.menuMenu.setTitle(_translate("CheeBotWindow", "Menu"))
        self.menuHelp.setTitle(_translate("CheeBotWindow", "Help"))
        self.actionExit.setText(_translate("CheeBotWindow", "Exit"))
        self.actionHalp.setText(_translate("CheeBotWindow", "Halp"))

#SR
    def heylisten(self):
        while 1:
            with sr.Microphone() as sauce:
                self.r.pause_threshold = 1
                print("adjusting for ambient noise...")
                self.r.adjust_for_ambient_noise(sauce, duration=1)
                print("listening...")
                self.audio = self.r.listen(sauce)
                try :
                    print("reading...")
                    self.command = self.r.recognize_google(self.audio)
                    print("you said "+self.command)
                    break
                except sr.UnknownValueError:
                    print("relistening...")
        self.Botinputting()


#Bot
    def Botinputting(self):
        #BotVariables


        #Bot Starts
        self.TheInput = self.command
        self.BotInput.clear()
        self.BotLog.insertPlainText(">>"+self.TheInput+'\n')
        self.BotExecuteCommand()
        
    def timegreet(self):
        if self.Clocktime < "12:00":
            self.GoodTime = "Good Morning"
        elif "12:00:00" < self.Clocktime < "13:00":
            self.Goodtime = "Noon"
        elif "13:00:00" < self.Clocktime < "18:00":
            self.Goodtime = "Good Afternoon"
        elif "18:00:00" < self.Clocktime < "20:30":
            self.Goodtime = "Good Evening"
        else:
            self.Goodtime = "Good Night"
        self.BotLog.insertPlainText( self.Goodtime + "\n")
        self.cheetts.Speak(self.Goodtime)

    def BotExecuteCommand(self):
        try:

            if "GOOGLE SEARCH" in self.TheInput.upper():
                webbrowser.open('https://www.google.com/search?q=' + self.TheInput[ self.TheInput.find("google") + 14:], new=2,autoraise=True)

            elif 'FACEBOOK' in self.TheInput.upper():
                self.BotLog.insertPlainText( "Opening Facebook on your current browser" + "\n")
                self.cheetts.Speak("Opening Facebook on your current browser")
                webbrowser.open('https://www.facebook.com/', new=2, autoraise=True)

            elif 'YOUTUBE' in self.TheInput.upper():
                if 'SEARCH' in self.TheInput.upper():
                    youtube1 = self.TheInput.find("search")
                    youtube2 = self.TheInput[youtube1 + 7:]
                    webbrowser.open('https://www.youtube.com/results?search_query=' + youtube2, new=2, autoraise=True)
                    self.BotLog.insertPlainText("now searching for" + youtube2 + "on youtube." + '\n')
                    self.cheetts.Speak("now searching for" + youtube2 + "on youtube.")
                else:
                    webbrowser.open('https://www.youtube.com')
                    self.BotLog.insertPlainText( "now opening youtube on your browser"+"\n")
                    self.cheetts.Speak("now opening youtube on your browser")

            elif 'WHAT IS' in self.TheInput.upper():
                self.BotLog.insertPlainText("Let me look up for that \n")
                self.cheetts.Speak("Let me look up for that")
                self.TheInput = re.sub('\s','+',self.TheInput)
                self.req = urllib.request.Request(url="https://www.google.com/search?q="+self.TheInput,
                                             headers={'User-Agent': "Mozilla"})
                print("Connecting")
                self.resp = urllib.request.urlopen(self.req)
                print("Opening")
                self.soup = bs.BeautifulSoup(self.resp, 'html.parser')
                print("Parsing")
                self.results = self.soup.findAll('div', {'class': 'g'})
                self.BotLog.insertPlainText(self.results[0].text+'\n')
                self.cheetts.Speak(self.results[0].text)
                print(self.results[0])

            elif 'WHO IS' in self.TheInput.upper():
                self.BotLog.insertPlainText("Let me look up for that \n")
                self.cheetts.Speak("Let me look up for that")
                self.TheInput = re.sub('\s', '+', self.TheInput)
                self.req = urllib.request.Request(url="https://www.google.com/search?q=" + self.TheInput,
                                                  headers={'User-Agent': "Mozilla"})
                print("Connecting")
                self.resp = urllib.request.urlopen(self.req)
                print("Opening")
                self.soup = bs.BeautifulSoup(self.resp, 'html.parser')
                print("Parsing")
                self.results = self.soup.findAll('div', {'class': 'g'})
                self.BotLog.insertPlainText(self.results[0].text + '\n')
                self.cheetts.Speak(self.results[0].text)

            elif 'where is' in self.TheInput:
                self.BotLog.insertPlainText("Let me look up for that \n")
                self.cheetts.Speak("Let me look up for that")
                self.TheInput = re.sub('\s', '+', self.TheInput)
                self.req = urllib.request.Request(url="https://www.google.com/search?q=" + self.TheInput,
                                                  headers={'User-Agent': "Mozilla"})
                print("Connecting")
                self.resp = urllib.request.urlopen(self.req)
                print("Opening")
                self.soup = bs.BeautifulSoup(self.resp, 'html.parser')
                print("Parsing")
                self.results = self.soup.findAll('div', {'class': 'g'})
                self.BotLog.insertPlainText(self.results[0].text + '\n')
                self.cheetts.Speak(self.results[0].text)

            elif 'when is' in self.TheInput:
                self.BotLog.insertPlainText("Let me look up for that \n")
                self.cheetts.Speak("Let me look up for that")
                self.TheInput = re.sub('\s', '+', self.TheInput)
                self.req = urllib.request.Request(url="https://www.google.com/search?q=" + self.TheInput,
                                                  headers={'User-Agent': "Mozilla"})
                print("Connecting")
                self.resp = urllib.request.urlopen(self.req)
                print("Opening")
                self.soup = bs.BeautifulSoup(self.resp, 'html.parser')
                print("Parsing")
                self.results = self.soup.findAll('div', {'class': 'g'})
                self.BotLog.insertPlainText(self.results[0].text + '\n')
                self.cheetts.Speak(self.results[0].text)



            elif self.TheInput.upper() == "CLEAR SCREENc":
                self.BotLog.clear()

            elif self.TheInput.upper() == "WHAT TIME IS IT":
                self.thetime = datetime.datetime.strptime(self.Clocktime, "%H:%M")
                self.BotLog.insertPlainText("it is now " + self.thetime.strftime("%I:%M %p") + "\n")
                self.cheetts.Speak("it is now " +  self.thetime.strftime("%I:%M %p"))

            elif self.TheInput.upper in ["HI", "HELLO", "HEY", "YO", "GREETINGS"]:
                self.timegreet()

            elif "SAY" in self.TheInput.upper():
                sayline1 = self.TheInput.find('say')
                sayline2 = self.TheInput[sayline1 + 4:]
                self.BotLog.insertPlainText( sayline2 + '\n')
                self.cheetts.Speak(sayline2)

            elif 'THANK' in self.TheInput.upper():
                self.welcome = random.randrange(0, 3)
                if self.welcome == 1:
                    self.BotLog.insertPlainText( "You're Welcome" + '\n')
                    self.cheetts.Speak("You're Welcome")
                elif self.welcome == 2:
                    self.BotLog.insertPlainText( "No,Thank you" + '\n')
                    self.cheetts.Speak("No,Thank you")
                else:
                    self.BotLog.insertPlainText( "Glad to help you" + '\n')
                    self.cheetts.Speak("Glad to help you")

            elif "HOW ARE YOU" in self.TheInput.upper():
                self.phime = random.randrange(0, 3)
                if self.phime == 1:
                    self.BotLog.insertPlainText( "I'm Fine,How about you?" + '\n')
                    self.cheetts.Speak("I'm Fine,How about you?")
                else:
                    self.BotLog.insertPlainText( "I'm doing well!" + '\n')
                    self.cheetts.Speak("I'm doing well!")

            elif self.TheInput.upper() == "FLIP A COIN":
                self.randomcoin = random.randrange(0, 2)
                if self.randomcoin == 1:
                    self.BotLog.insertPlainText( "Heads" + '\n')
                    self.cheetts.Speak("Heads")
                else:
                    self.BotLog.insertPlainText( "Tails" + '\n')
                    self.cheetts.Speak("Tails")

            elif "RUN" in self.TheInput.upper():
                self.theprogram = self.TheInput[4:]
                if self.theprogram == "steam":
                        subprocess.call('call "C:\Program Files (x86)\Steam\Steam.exe"',shell=True)
                else:
                    self.BotLog.insertPlainText("Sorry,the program is not available \n")
                    self.cheetts.Speak("Sorry,the program is not available \n")
            else :
                self.BotLog.insertPlainText("Do Not Understand"+'\n')
        except Exception:
          self.BotLog.insertPlainText("Sorry,Something Went Wrong")

app = QtWidgets.QApplication(sys.argv)
Test=Ui_CheeBotWindow()
Test.show()
sys.exit(app.exec_())

