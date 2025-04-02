from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3       
app = QApplication([])
btn_ok = QPushButton('ответить') 
question1 = QLabel('в каком году закончилась холодная война?')
RadioGroupBox = QGroupBox('варианты ответов')
rbtn_1 = QRadioButton('1989')
rbtn_2 = QRadioButton('1991')
rbtn_3 = QRadioButton('2001')
rbtn_4 = QRadioButton('1978')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('результаты теста')
AnsGroupBox.hide()
lb_Result = QLabel('правильно/неправильно')
lb_Correct = QLabel('1991')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)
main_win = QWidget()
main_win.setWindowTitle('история от Соника')
main_layout = QVBoxLayout()
main_layout.addWidget(question1)
main_layout.addWidget(RadioGroupBox)
main_layout.addWidget(AnsGroupBox)
main_layout.addWidget(btn_ok)
answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(question1, wrong1, right_answer, wrong2, wrong3):
    shuffle(answer)
    answer[0] = wrong1
    answer[1] = right_answer
    answer[2] = wrong3
    answer[3] = wrong3
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('не очень простой вопрос')
    if answer[1].isChecked():
        a = 'верно'
        window.score += 1
    else:
        a = 'неверно'
    lb_Correct.setText('правильный ответ: 1991')
    lb_Result.setText('ваш ответ:'+ a)
main_win.score = 0
main_win.total = 0
def next_question():
    main_win.total +=1
def click_ok():
    if 'ответить' == btn_ok.text():
        show_result()
    else:
        next_question()
btn_ok.clicked.connect(click_ok)

    


main_win.setLayout(main_layout)
main_win.show()
app.exec_()