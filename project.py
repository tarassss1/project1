from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)

from random import shuffle # функція для переміщення відповідей

app = QApplication([])

# СТВОРЕННЯ ГОЛОВНОГО ВІКНА
window = QWidget()
width = 600
height = 500
window.resize(width, height)
window.move(300, 300)
window.setWindowTitle('Memory Card')

# СТВОРЕННЯ ВІДЖЕТІВ
btn_Menu = QPushButton('Меню') # кнопка повернення в головне меню
btn_Sleep = QPushButton('Відпочити') # кнопка забирає головне вікно і повертає його після того, як таймер пройде
box_Minutes = QSpinBox() # ввід кількості секунд
box_Minutes.setValue(30)
btn_OK = QPushButton('Відповісти') # кнопка відповіді
lb_Question = QLabel('') # текст запитання

# СТВОРЕННЯ ПАНЕЛі З ВАРІАНТАМИ
RadioGroupBox = QGroupBox("Варіанти відповідей") # група на екрані для перемикачів із відповідями

RadioGroup = QButtonGroup() # а це для групування перемикачів, щоб керувати їхньою поведінкою
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# СТВОРЕННЯ ПАНЕЛі З РЕЗУЛЬТАТАМИ
AnsGroupBox = QGroupBox("Результат тесту")
lb_Result = QLabel('') # тут розміщується напис "правильно" або "неправильно"
lb_Correct = QLabel('') # тут буде написано текст правильної відповіді




#  РОЗМІЩЕННЯ ПО ЛЕЯУТАХ

# Розміщуємо варіанти відповідей у два стовпці всередині групи:
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальні будуть усередині горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # дві відповіді в перший стовпчик
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # дві відповіді в другий стовпчик
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) #розміщуємо стовпці на одній лінії

RadioGroupBox.setLayout(layout_ans1) # готова "панель" з варіантами відповідей    
# розміщуємо результат:
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

# розміщуємо всі віджети у вікні, вони розташовані в чотири рядки:
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1) # розрив між кнопками робимо якомога довшим
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('секунд')) # 

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2) # задаємо величину кнопки
layout_line4.addStretch(1)

# Тепер створені 4 рядки розмістимо один під одним:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробіли між вмістом

window.setLayout(layout_card)


question = 'Якого кольору банан?'
correct = 'Жовтий'
wrong1 = 'Синій'
wrong2 = 'Чорний'
wrong3 = 'Червоний'

list1 = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
shuffle(list1)
answer = list1[0]
w1 = list1[1]
w2 = list1[2]
w3 = list1[3]

def show_data():
    lb_Question.setText(question)
    lb_Correct.setText(correct)
    answer.setText(correct)
    w1.setText(wrong1)
    w2.setText(wrong2)
    w3.setText(wrong3)

def check_result():
    a = answer.isChecked()
    if a:
        lb_Result.setText('Правильно')
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Наступне запитання')
    else:
        b = w1.isChecked() or w2.isChecked() or w3.isChecked()
        if b:
            lb_Result.setText('Неправильно')
            RadioGroupBox.hide()
            AnsGroupBox.show()
            btn_OK.setText('Наступне запитання')
            

def exit():
    if btn_OK.text() == 'Наступне запитання':
        RadioGroupBox.show()
        AnsGroupBox.hide()
    else:
        check_result()

btn_OK.clicked.connect(exit)
show_data()


# ТАЙМЕР
t = 1000
timer = QTimer()
def sleep_card():
    window.hide()
    timer.setInterval(box_Minutes.value() * t)
    timer.start()
def show_card():
    window.show()
    timer.stop()

btn_Sleep.clicked.connect(sleep_card)
timer.timeout.connect(show_card)

window.show()
app.exec_()