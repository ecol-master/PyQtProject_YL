from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, \
    QPushButton, QFileDialog
from PyQt5.QtWidgets import QListWidget, QInputDialog
from PyQt5.QtCore import Qt
from dialogs import CreateNewNote, DeletePictures
import sys
import sqlite3
from add_photo_in_folder import save_image_in_folder
from PyQt5.QtGui import QPixmap
import os
from UI_py.homepage import Ui_MainWindow


class NoteWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # настройка главного окна
        self.setupUi(self)
        self.setFixedSize(786, 664)
        self.setWindowTitle('Программа - Заметочник')

        # соединение с базой данных
        self.con = sqlite3.connect('../notes_db.sqlite')
        self.cur = self.con.cursor()

        # список id заметок, которые в данный момент находят на виджете
        self.now_notes_on_lw = []

        # работа с фото на заметке
        self.images = None
        self.now_im_index = -1

        # объект диалогового окна для добавления заметки и работа с ним
        self.dialog_add_note = CreateNewNote()
        self.dialog_add_note.save_button.clicked.connect(self.save_note_btn_dialog)
        self.dialog_add_note.delete_note_button.clicked.connect(self.delete_note)
        self.dialog_add_note.add_photo.clicked.connect(self.set_image_on_dialog)

        # объект диалогово окна для удаления заметки
        self.delete_pict_dialog = DeletePictures()
        self.delete_pict_dialog.yes_button.clicked.connect(self.click_yes_button)

        # настройка group-box для главной страницы
        self.groupbox_main: QComboBox
        self.groupbox_main.currentTextChanged.connect(self.set_notes_on_lw)

        # блок, в котором к кнопкам на главном окне привязываются функции-обработчики
        self.create_note: QPushButton
        self.create_note.clicked.connect(self.click_button_add_note)
        self.choice_from_file.clicked.connect(self.open_file_to_note)
        self.add_group_button.clicked.connect(self.add_group)
        self.add_photo_button.clicked.connect(self.add_photo)
        self.delete_photo.clicked.connect(self.delete_photo_func)

        # привязываю к списку заметок обработчик нажатия
        self.notes_view: QListWidget
        self.update_groups_box()
        self.notes_view.itemClicked.connect(self.click_note_on_lw)
        self.dialog_id_open = None

        self.set_notes_on_lw()

    # функция для показа окна
    def click_button_add_note(self):
        self.dialog_add_note.clear_parametrs()
        self.dialog_id_open = None
        pixmap = QPixmap(f'../images/main_picture.png')
        self.dialog_add_note.view_photo.setPixmap(pixmap)
        self.dialog_add_note.show()

    # функция при помощи метода check_note получает заголовок и текст
    # которые записывает в базу данных и сохраняет изменения
    def save_note_btn_dialog(self):
        # получаю данные с заметки
        information = self.dialog_add_note.check_note()
        if information is not None:
            name_im = self.images[
                self.now_im_index] if self.images != None else 'main_picture.png'
            if self.dialog_id_open is None:
                self.cur.execute("""INSERT INTO notes(title, text, theme, image_id)
                                    VALUES (?, ?, ?, (SELECT id FROM images_project
                                                    WHERE name_image = ?))
                                    """, (
                    information[0], information[1], information[2],
                    name_im))

            else:
                self.cur.execute("""UPDATE notes 
                                    SET title = ?,
                                        text = ?, 
                                        theme = ?,
                                        image_id = (SELECT id FROM images_project
                                                    WHERE name_image = ?)
                                    WHERE id = ?
                                    """, (information[0], information[1],
                                          information[2], name_im, self.dialog_id_open))
                self.dialog_id_open = None
            self.con.commit()
            self.dialog_add_note.close()
            self.set_notes_on_lw()
            self.dialog_add_note.clear_parametrs()
            self.set_notes_on_lw()
            self.images = None
            self.now_im_index = 0
            self.print_db()

    # выводит данные из бд
    def print_db(self):
        notes = self.cur.execute("""SELECT * FROM notes""")
        for i in notes:
            print(i)

    # функция получает новую группу и убедившись в ее уникальности,
    def add_group(self):
        name = (QInputDialog.getText(self, "Введите группу",
                                     "Какая новая группа?"))[0]
        name = str(name).capitalize()
        if name != '':
            groups = [i[0] for i in
                      self.cur.execute("""SELECT theme FROM themes""").fetchall()]
            if name not in groups:
                self.cur.execute("""INSERT INTO themes(theme) VALUES (?)""", (name,))
                self.con.commit()
                self.update_groups_box()

    # функция открывает окно для выбора файла, считывает текст и открывает заметку
    # для создания новой
    def open_file_to_note(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать файл', '',
                                                'Заметка (*.txt);;Заметка (*.txt);;Все файлы (*)')[
            0]
        if file_name != '':
            self.dialog_add_note.clear_parametrs()
            self.dialog_id_open = None
            self.dialog_add_note.show()
            name_on_title = (file_name.split('/')[-1]).split('.')[0]
            text = open(file_name, 'r').read()
            self.dialog_add_note.note_title_line.setText(name_on_title)
            self.dialog_add_note.note_text_value.setPlainText(text)
            pixmap = QPixmap(f'../images/main_picture.png')
            self.dialog_add_note.view_photo.setPixmap(pixmap)

    # функция для обновления заметок на втором таб виджете
    def update_groups_box(self):
        groups = self.cur.execute("""SELECT theme FROM themes""").fetchall()
        groups = [i[0] for i in groups]
        self.groupbox_main.clear()
        self.dialog_add_note.groups_box.clear()
        self.groupbox_main.addItems(groups)
        self.dialog_add_note.groups_box.addItems(groups)

    # функция считывает имя темы и на лист виджет ставит заголовки заметок
    # с этой группой
    def set_notes_on_lw(self):
        group = self.groupbox_main.currentText()
        notes = self.cur.execute("""SELECT id, title FROM notes WHERE theme = ?""",
                                 (group,)).fetchall()
        self.notes_view: QListWidget
        self.notes_view.clear()
        # ставлю заголовки заметок на список
        self.notes_view.addItems((i[1]) + '\n' for i in notes)
        self.now_notes_on_lw = []
        self.now_notes_on_lw = [i[0] for i in notes]

    # обработчик на нажатие элемента
    def click_note_on_lw(self, item):
        # получаю  индекс элемента на который нажали
        self.notes_view: QListWidget
        note_index = self.notes_view.indexFromItem(item).row()
        note_id = self.now_notes_on_lw[note_index]

        # получаю данные из бд
        information = self.cur.execute("""SELECT * FROM notes WHERE id = ?""",
                                       (note_id,)).fetchone()
        groups = self.cur.execute("""SELECT theme FROM themes""").fetchall()
        groups = [i[0] for i in groups]
        index_group = groups.index(information[-2])
        image_name = self.cur.execute("""SELECT name_image FROM images_project
                                            WHERE id = ?""",
                                      (information[-1],)).fetchone()
        # ставлю на заметку данные
        self.dialog_add_note.show()
        self.dialog_add_note.note_title_line.setText(information[1])
        self.dialog_add_note.note_text_value.setPlainText(information[2])
        self.dialog_add_note.groups_box.setItemText(index_group, information[3])
        pixmap = QPixmap(f'images/{image_name[0]}')
        self.dialog_add_note.view_photo.setPixmap(pixmap)
        self.dialog_id_open = note_id

    # функция удаляет запись при нажатии на кнопку
    def delete_note(self):
        if self.dialog_id_open is not None:
            self.cur.execute("""DELETE FROM notes 
                                    WHERE id = ?""", (self.dialog_id_open,))
            self.con.commit()
            self.dialog_add_note.close()
            self.set_notes_on_lw()
        else:
            self.dialog_add_note.error_delet.show()

    # функция открывает окно и получает путь к файлу
    # передает путь в функцию, которая сохраняет в бд и в images
    # и базе данных
    def add_photo(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать файл', '',
                                                '(*.jpg *.png *.jpeg);;;;Все файлы (*)')[
            0]
        name_files = ['jpg', 'png', 'jpeg']
        name = file_name.split('.')[-1]
        if file_name:
            if name in name_files:
                name_file = save_image_in_folder(file_name=file_name)
                self.cur.execute("""INSERT INTO images_project(name_image)
                                    VALUES (?)""", (name_file,))
                self.con.commit()

    # функция для работы с картинками на диалоге
    def set_image_on_dialog(self):
        images = os.listdir('../images')
        self.images = images
        self.now_im_index += 1
        if (self.now_im_index + 1) == len(self.images):
            pixmap = QPixmap(f'images/{self.images[self.now_im_index]}')
            self.now_im_index = -1
        else:
            pixmap = QPixmap(f'images/{self.images[self.now_im_index]}')
        self.dialog_add_note.view_photo.setPixmap(pixmap)

    # фунция открывает диалоговое окно для удаления фотографий
    # delete_photo
    def delete_photo_func(self):
        self.delete_pict_dialog.show()

    # функция для второго диалога
    # при окончательном удалении
    def click_yes_button(self):
        self.delete_pict_dialog.hide_elements()
        image_name = self.delete_pict_dialog.label.text()
        os.remove(f'images/{image_name}')
        self.cur.execute("""UPDATE notes
                                    SET image_id = 1
                                    WHERE image_id = (SELECT id FROM images_project
                                                        WHERE name_image = ?)""",
                         (image_name,))
        self.cur.execute("""DELETE from images_project
                            WHERE name_image = ?""", (image_name,))

        self.con.commit()

    # обработчик на нажатия стрелочек, переключение таб-виджетов
    def keyPressEvent(self, event):
        if event.key() == Qt.RightEdge or event.key() == Qt.LeftEdge:
            self.tabWidget.setCurrentIndex(1)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = NoteWindow()
    wind.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
