from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)

from random import shuffle # функція для переміщення відповідей

app = QApplication([])

# СТВОРЕННЯ ВІДЖЕТІВ
btn_Menu = QPushButton('Меню') # кнопка повернення в головне меню
btn_Sleep = QPushButton('Відпочити') # кнопка забирає головне вікно і повертає його після того, як таймер пройде
box_Minutes = QSpinBox() # ввід кількості секунд
box_Minutes.setValue(30)
btn_OK = QPushButton('Відповісти') # кнопка відповіді
lb_Question = QLabel('') # текст запитання

# ПАНЕЛЬ З ВАРІАНТАМИ
RadioGroupBox = QGroupBox("Варианти відповідей") # група на екрані для перемикачів із відповідями

RadioGroup = QButtonGroup() # а це для групування перемикачів, щоб керувати їхньою поведінкою
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Панель з результатом:
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

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.

def show_result():
    ''' показати панель відповідей '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('наступне запитання')

def show_question():
    ''' показати панель відповідей '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')
    # скинути обрану радіо-кнопку
    RadioGroup.setExclusive(False) # зняли обмеження, щоб можна було скинути вибір радіокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # повернули обмеження, тепер тільки одна радіокнопка може бути обрана

card_width, card_height = 600, 500 # початкові розміри
text_wrong = 'Неправильно'
text_correct = 'Правильно'

# у цій версії напишемо в коді одне запитання і відповіді до нього
# відповідні змінні як би поля майбутнього об'єкта "form" (тобто анкета) 
frm_question = 'Яблоко'
frm_right = 'apple'
frm_wrong1 = 'application'
frm_wrong2 = 'building'
frm_wrong3 = 'caterpillar'

# Тепер нам потрібно показати ці дані,
# причому відповіді розподілити випадково між радіокнопками, і пам'ятати кнопку з правильною відповіддю.
# Для цього створимо набір посилань на радіокнопки і перемішаємо його
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)
answer = radio_list[0] # мы не знаем, какой это из радиобаттонов, но можем положить сюда правильный ответ и запомнить это
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]

def show_data():
    ''' показує на екрані потрібну інформацію '''
    # об'єднаємо у функцію схожі дії
    lb_Question.setText(frm_question)
    lb_Correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)

def check_result():
    ''' перевірка, чи правильну відповідь обрано
    якщо відповідь було обрано, то напис "вірно/невірно" набуває потрібного значення
    і показується панель відповідей '''
    correct = answer.isChecked() # у цьому радіобаттоні лежить наша відповідь!
    if correct:
        # відповідь вірна, запишемо
        lb_Result.setText(text_correct) # напис "вірно" або "невірно"
        show_result()
    else:
        incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
        if incorrect:
            # відповідь хибна, запишемо і відобразимо в статистиці
            lb_Result.setText(text_wrong) # напис "вірно" або "невірно"
            show_result()

def click_OK(self):
    # поки що перевіряємо запитання, якщо ми в режимі запитання, інакше нічого
    if btn_OK.text() != 'Наступний':
        check_result()

win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')

win_card.setLayout(layout_card)
show_data()
show_question()
btn_OK.clicked.connect(click_OK)


win_card.show()
app.exec_()