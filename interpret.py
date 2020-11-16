import sys
import speech_recognition as sr
from translate import Translator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyttsx3

class Window(QDialog):

    #constructor of class Window
    def __init__(self):
        super(Window,self).__init__()
        self.title = "Language Translator"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.list_lan = ['English','Spanish','Hindi','French','Tamil','German','Bengali','Chinese','Arabic','Greek','Gujarati',
                        'Italian','Korean','Malayalam','Marathi','Punjabi','Russian','Telugu']
        self.GUI()

    #Adding properties to the GUI made using pyqt5
    def GUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)

        vbox = QGridLayout()
        self.source = QComboBox(self)
        self.source.addItems(self.list_lan)
        vbox.addWidget(self.source,0,0)

        self.btn1 = QPushButton("Record",self)
        self.btn1.clicked.connect(self.record)
        vbox.addWidget(self.btn1,2,0)

        self.textbox = QTextEdit(self)
        self.textbox.setFont(QFont("Times",15))
        self.textbox.resize(280,280)
        self.textbox.setPlaceholderText("Enter your text here...")
        vbox.addWidget(self.textbox,1,0)

        self.btn = QPushButton("Translate",self)
        self.btn.clicked.connect(self.translate_func)
        vbox.addWidget(self.btn,3,0)

        
        self.destination = QComboBox(self)
        self.destination.addItems(self.list_lan)
        vbox.addWidget(self.destination,0,1)

        self.textbox2 = QTextEdit(self)
        self.textbox2.setFont(QFont("Times",15))
        self.textbox2.resize(280,280)
        self.textbox2.setPlaceholderText("Translated text will appear here...")
        vbox.addWidget(self.textbox2,1,1)
        self.setLayout(vbox)

    #to refer to a certain language code
    def language(self,lang):
        list = {'arabic':'ar', 'bengali': 'bn', 'chinese':'zh-tw','english':'en','french':'fr','german':'de','greek':'el' , 
                'gujarati':'gu','hindi':'hi','italian':'it' ,'korean':'ko', 'malayalam':'ml' , 'marathi':'mr',
                'punjabi':'pa','russian':'ru',  'spanish':'es', 'tamil':'ta', 'telugu':'te'}
        lang = lang.lower()
        return list[lang]
        
    #audio-to-text using google speech recognition[online]
    def record(self):
        list_record = {'ar':'ar-DZ', 'bn': 'bn-IN','zh-tw':'zh (cmn-Hans-CN)','en':'en-GB','fr':'fr-BE','ge':'de-DE','el':'el-GR' , 
                'gu':'gu-IN','hi':'hi-IN','italian':'it' ,'ko':'ko-KR', 'ml':'ml-IN' , 'mr':'mr-IN',
                'pa':'pa-Guru-IN','ru':'ru-RU',  'es':'es-MX', 'ta':'ta-IN', 'te':'te-IN'}
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            self.audio = self.r.listen(source)
            try:
                var = self.language(self.source.currentText())
                self.text = self.r.recognize_google(self.audio,language=list_record[var])
                self.textbox.setText(self.text)
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Voice not detected: Record Again")
                msg.setWindowTitle("Error")
                msg.exec_()

    #text-to-speech using pyttsx3[offline]    
    def SpeakText(self,command,var):  
        self.engine = pyttsx3.init() 
        self.engine.setProperty("language",var)
        self.engine.say(command) 
        self.engine.runAndWait() 

    #used for language translation 
    def translate_func(self):
        self.srce = self.language(self.source.currentText())
        self.dest = self.language(self.destination.currentText())
        translator = Translator(from_lang=self.srce, to_lang=self.dest)
        self.source_text = self.textbox.toPlainText()
        self.result = translator.translate(self.source_text)
        self.textbox2.setText(self.result)
        self.SpeakText(self.result,self.dest)

 
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()