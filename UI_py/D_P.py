from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_D_P(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(531, 561)
        Dialog.setStyleSheet("background-color:rgb(127, 255, 212);")
        self.view_photo = QtWidgets.QLabel(Dialog)
        self.view_photo.setGeometry(QtCore.QRect(40, 110, 371, 251))
        self.view_photo.setStyleSheet("background-color:rgb(127, 255, 212);")
        self.view_photo.setText("")
        self.view_photo.setObjectName("view_photo")
        self.right_click = QtWidgets.QPushButton(Dialog)
        self.right_click.setGeometry(QtCore.QRect(440, 190, 61, 81))
        self.right_click.setStyleSheet("border-radius:5px;\n"
                                       "border: 2px solid black;")
        self.right_click.setObjectName("right_click")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 70, 221, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.delete_button = QtWidgets.QPushButton(Dialog)
        self.delete_button.setGeometry(QtCore.QRect(140, 370, 151, 31))
        self.delete_button.setStyleSheet("border-radius:5px;\n"
                                         "border: 2px solid black;")
        self.delete_button.setObjectName("delete_button")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 410, 311, 31))
        self.label_2.setObjectName("label_2")
        self.yes_button = QtWidgets.QPushButton(Dialog)
        self.yes_button.setGeometry(QtCore.QRect(60, 450, 81, 41))
        self.yes_button.setStyleSheet("border-radius:5px;\n"
                                      "border: 2px solid black;")
        self.yes_button.setObjectName("yes_button")
        self.no_button = QtWidgets.QPushButton(Dialog)
        self.no_button.setGeometry(QtCore.QRect(330, 450, 81, 41))
        self.no_button.setStyleSheet("border-radius:5px;\n"
                                     "border: 2px solid black;")
        self.no_button.setObjectName("no_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.right_click.setText(_translate("Dialog", "-->"))
        self.delete_button.setText(_translate("Dialog", "Удалить"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:9pt;\">Вы точно хотите удалить выбранное фото?</span></p></body></html>"))
        self.yes_button.setText(_translate("Dialog", "ДА"))
        self.no_button.setText(_translate("Dialog", "НЕТ"))
