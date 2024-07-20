# Підключення бібліотеки та модулів
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint



app = QApplication([])  #створюємо додаток
main_window = QWidget() #створюємо вікно
main_window.resize(400,200)
main_window.move(200,200)

btn1 = QPushButton('Згенерувати') #створюємо кнопку
text = QLabel('Переможець')


line  = QVBoxLayout()
line.addWidget(btn1, alignment= Qt.AlignCenter )
line.addWidget(text, alignment= Qt.AlignCenter)


main_window.setLayout(line)
main_window.show()
app.exec_()
