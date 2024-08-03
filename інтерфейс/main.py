from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


#Створюємо вікна для відповідей
def wrong_answer():
    lose = QMessageBox()
    lose.resize(150,90)
    lose.setText('Ти програв ' + '😥')
    lose.exec_()
def right_answer():
    win = QMessageBox()
    win.setText('Ти виграв ' +'😊')
    win.resize(150,90)
    win.exec_()

#Створюємо вікно та додаток
app = QApplication([])
main_window = QWidget()
main_window.resize(400,300)
main_window.setWindowTitle('Конкурс від Crazy People')

#Створюємо кнопки та текст
btn1 = QRadioButton('2005')
btn2 = QRadioButton('2010')
btn3 = QRadioButton('2015')
btn4 = QRadioButton('2020')
btn5 = QRadioButton('2000')
btn6 = QRadioButton('2013')
question = QLabel('В якому році канал отримав " золоту кнопку " від YouTube?')

#Створюємо лінії для розміщення віджетів
lineH1 = QHBoxLayout()
lineH2 = QHBoxLayout()
lineH3 = QHBoxLayout()
lineH4 = QHBoxLayout()

lineV1 = QVBoxLayout()


#Накидуємо кнопки на горизонтальні лінії 
lineH1.addWidget(question, alignment = Qt.AlignCenter)
lineH2.addWidget(btn1, alignment = Qt.AlignCenter)
lineH2.addWidget(btn2, alignment = Qt.AlignCenter)
lineH3.addWidget(btn3, alignment = Qt.AlignCenter)
lineH3.addWidget(btn4, alignment = Qt.AlignCenter)
lineH4.addWidget(btn5, alignment = Qt.AlignCenter)
lineH4.addWidget(btn6, alignment = Qt.AlignCenter)
#Накидуємо горизонтальні лінії на вертикальні
lineV1.addLayout(lineH1)
lineV1.addLayout(lineH2)
lineV1.addLayout(lineH3)
lineV1.addLayout(lineH4)



#Відображаємо вертикальну лінію
main_window.setLayout(lineV1)


#Підключаємо кнопки до відповідей
btn1.clicked.connect(right_answer)
btn2.clicked.connect(wrong_answer)
btn3.clicked.connect(wrong_answer)
btn4.clicked.connect(wrong_answer)
btn5.clicked.connect(wrong_answer)
btn6.clicked.connect(wrong_answer)


#Показуємо вікно
main_window.show() 
app.exec_()




