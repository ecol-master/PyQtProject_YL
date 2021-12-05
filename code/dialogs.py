from PyQt5.QtWidgets import QDialog, QPushButton, QPlainTextEdit
from PyQt5.QtWidgets import QMessageBox, QComboBox
from PyQt5.QtGui import QPixmap
import csv
import os
from UI_py.C_N_D import Ui_C_N_D
from UI_py.D_P import Ui_D_P


# класс для заметок, используется в основном окне
class CreateNewNote(QDialog, Ui_C_N_D):
    def __init__(self):
        super().__init__()
        # наЫстройка окна
        self.setupUi(self)
        self.setFixedSize(777, 628)
        self.setWindowTitle('Создание заметки')

        # настройка всплывающего окна для ошибки, при пустом заголовке
        self.error_title = QMessageBox()
        self.error_title.setWindowTitle('Ошибка')
        self.error_title.setText('Введите текст в поле заголовка')
        self.error_title.setIcon(QMessageBox.Warning)

        # настройка всплывающего окна при удалении несозданной заметки
        self.error_delet = QMessageBox()
        self.error_delet.setWindowTitle('Ошибка')
        self.error_delet.setText('Для начала создайте заметку')
        self.error_delet.setIcon(QMessageBox.Warning)

        # настройка combo-box для показа групп заметок
        self.groups_box: QComboBox
        self.groups_box = self.groups_box

        self.delete_note_button: QPushButton
        self.delete_note_button = self.delete_note_button

        # список всех кнопок на диалоге / лэйблов ( кроме того на котором картинка )
        self.buttons = [self.groups_box, self.choice_style, self.save_button,
                        self.delete_note_button, self.add_photo]
        self.labels = [self.label, self.label_2]

        # нажатие на смену стиля
        self.choice_style.clicked.connect(self.set_styles)

        # виды оформления / тот который стоит сейчас
        self.styles = self.return_styles()
        self.now_style, self.style = 0, None

        self.save_button: QPushButton
        self.save_button = self.save_button

    # проверяет заметку на правильность заполнения при вводе
    def check_note(self):
        title = self.note_title_line.text()
        self.note_text_value: QPlainTextEdit
        text = self.note_text_value.toPlainText()
        theme = self.groups_box.currentText()
        if title == '':
            self.error_title.show()
        elif theme == '':
            pass
        else:
            return [title, text, theme]

    # метод для очищения виджета, после добавления записи
    def clear_parametrs(self):
        self.note_title_line.setText('')
        self.note_text_value: QPlainTextEdit
        self.note_text_value.setPlainText('')
        self.groups_box.setItemText(0, 'Общие')

    # для получения стилей
    def return_styles(self):
        with open('../styles_themes.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            return list(reader)[1:4:2]

    # меняет стили на окне заметки
    def set_styles(self):
        if self.now_style == 0:
            self.style = self.styles[1]
        else:
            self.style = self.styles[0]
        self.setStyleSheet(self.style[0])
        self.note_text_value.setStyleSheet(self.style[1])
        self.view_photo.setStyleSheet(self.style[2])
        for i in self.buttons:
            i: QPushButton
            i.setStyleSheet(self.style[3])
        self.groupBox.setStyleSheet(self.style[4])
        for i in self.labels:
            i.setStyleSheet(self.style[5])
        self.note_title_line.setStyleSheet(self.style[6])
        if self.now_style == 1:
            self.now_style = 0
        else:
            self.now_style = 1


# диалог который открывается для удаления картинок
class DeletePictures(QDialog, Ui_D_P):
    def __init__(self):
        super().__init__()
        # настройка главного окна
        self.setupUi(self)
        self.setWindowTitle('Удаление заметки')
        # список с элементами которые нужно скрыть/открыть
        self.box_yes_or_no = [self.yes_button, self.no_button, self.label_2]

        # сразу скрою все элементы / поставлю картинки на окно
        self.hide_elements()

        # привязываю к кнопкам обрабтчики
        self.delete_button.clicked.connect(self.show__elements)
        self.no_button.clicked.connect(self.hide_elements)
        self.right_click.clicked.connect(self.click_button_change)

        self.images = os.listdir('../images')
        self.now_index = 0

        self.set_image()
        self.check_main_picture()

    # вспомогательная функция, скрывает элементы
    def hide_elements(self):
        for i in self.box_yes_or_no:
            i.hide()

    # функция открывает скрытые элементы
    def show__elements(self):
        for i in self.box_yes_or_no:
            i.show()

    # функция проверяет на main_picture
    def check_main_picture(self):
        if self.label.text() == 'main_picture.png':
            self.delete_button: QPushButton
            self.delete_button.setEnabled(False)
        else:
            self.delete_button.setEnabled(True)

    def set_image(self):
        pixmap = QPixmap(f'images/{self.images[self.now_index]}')
        self.view_photo.setPixmap(pixmap)
        self.label.setText(self.images[self.now_index])

    # по нажатию клавиши прокрутки меняет фотку и текст
    def click_button_change(self):
        self.images = os.listdir('../images')
        if self.now_index + 1 >= len(self.images):
            self.now_index = -1

        self.now_index += 1
        pixmap = QPixmap(f'images/{self.images[self.now_index]}')
        self.view_photo.setPixmap(pixmap)
        self.label.setText(self.images[self.now_index])
        self.check_main_picture()
