from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_C_N_D(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(777, 628)
        Dialog.setStyleSheet("background-color:rgb(255,255,240);")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 711, 151))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setTabletTracking(False)
        self.groupBox.setObjectName("groupBox")
        self.save_button = QtWidgets.QPushButton(self.groupBox)
        self.save_button.setGeometry(QtCore.QRect(340, 30, 91, 41))
        self.save_button.setStyleSheet("background-color:rgb(211,211,211);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.save_button.setObjectName("save_button")
        self.choice_style = QtWidgets.QPushButton(self.groupBox)
        self.choice_style.setGeometry(QtCore.QRect(210, 30, 101, 41))
        self.choice_style.setStyleSheet("background-color:rgb(211,211,211);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.choice_style.setObjectName("choice_style")
        self.groups_box = QtWidgets.QComboBox(self.groupBox)
        self.groups_box.setGeometry(QtCore.QRect(20, 30, 161, 41))
        self.groups_box.setStyleSheet("background-color:rgb(211,211,211);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.groups_box.setObjectName("groups_box")
        self.delete_note_button = QtWidgets.QPushButton(self.groupBox)
        self.delete_note_button.setGeometry(QtCore.QRect(460, 30, 91, 41))
        self.delete_note_button.setStyleSheet("background-color:rgb(211,211,211);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.delete_note_button.setObjectName("delete_note_button")
        self.add_photo = QtWidgets.QPushButton(self.groupBox)
        self.add_photo.setGeometry(QtCore.QRect(580, 30, 111, 41))
        self.add_photo.setStyleSheet("background-color:rgb(211,211,211);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.add_photo.setObjectName("add_photo")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(310, 80, 91, 31))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(30, 170, 721, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.note_text_value = QtWidgets.QPlainTextEdit(Dialog)
        self.note_text_value.setGeometry(QtCore.QRect(30, 220, 321, 381))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(10)
        self.note_text_value.setFont(font)
        self.note_text_value.setStyleSheet("background-color:rgba(127,255,212, 0.5);")
        self.note_text_value.setObjectName("note_text_value")
        self.note_title_line = QtWidgets.QLineEdit(Dialog)
        self.note_title_line.setGeometry(QtCore.QRect(190, 130, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.note_title_line.setFont(font)
        self.note_title_line.setStyleSheet("font-size:16px;\n"
"font-family:\'Courier New\', Courier, monospace;")
        self.note_title_line.setObjectName("note_title_line")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 180, 91, 31))
        self.label_2.setObjectName("label_2")
        self.view_photo = QtWidgets.QLabel(Dialog)
        self.view_photo.setGeometry(QtCore.QRect(380, 260, 371, 251))
        self.view_photo.setStyleSheet("background-color:rgb(255,255,240);")
        self.view_photo.setObjectName("view_photo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Действия"))
        self.save_button.setText(_translate("Dialog", "Сохранить"))
        self.choice_style.setText(_translate("Dialog", "Сменить стиль"))
        self.delete_note_button.setText(_translate("Dialog", "Удалить"))
        self.add_photo.setText(_translate("Dialog", "Сменить фото"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Заголовок</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Текст</span></p></body></html>"))
        self.view_photo.setText(_translate("Dialog", "TextLabel"))
