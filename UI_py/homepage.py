from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:rgb(238,232,170);")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 781, 661))
        self.tabWidget.setStyleSheet("font-size:14px;\n"
"")
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.create_note = QtWidgets.QPushButton(self.tab)
        self.create_note.setGeometry(QtCore.QRect(310, 270, 131, 41))
        self.create_note.setStyleSheet("background-color:rgb(255,248,220);\n"
"border: 2px solid black;\n"
"border-radius:10px;")
        self.create_note.setObjectName("create_note")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(240, 0, 281, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/main_picture.png"))
        self.label.setObjectName("label")
        self.choice_from_file = QtWidgets.QPushButton(self.tab)
        self.choice_from_file.setGeometry(QtCore.QRect(270, 410, 221, 51))
        self.choice_from_file.setStyleSheet("background-color:rgb(255,248,220);\n"
"border: 2px solid black;\n"
"border-radius:10px;")
        self.choice_from_file.setObjectName("choice_from_file")
        self.add_photo_button = QtWidgets.QPushButton(self.tab)
        self.add_photo_button.setGeometry(QtCore.QRect(20, 330, 221, 51))
        self.add_photo_button.setStyleSheet("background-color:rgb(255,248,220);\n"
"border: 2px solid black;\n"
"border-radius:10px;")
        self.add_photo_button.setObjectName("add_photo_button")
        self.delete_photo = QtWidgets.QPushButton(self.tab)
        self.delete_photo.setGeometry(QtCore.QRect(510, 330, 221, 51))
        self.delete_photo.setStyleSheet("background-color:rgb(255,248,220);\n"
"border: 2px solid black;\n"
"border-radius:10px;")
        self.delete_photo.setObjectName("delete_photo")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setObjectName("tab_2")
        self.add_group_button = QtWidgets.QPushButton(self.tab_2)
        self.add_group_button.setGeometry(QtCore.QRect(30, 50, 271, 41))
        self.add_group_button.setStyleSheet("background-color:rgb(255,248,220);\n"
"border: 2px solid black;\n"
"border-radius:10px;")
        self.add_group_button.setObjectName("add_group_button")
        self.notes_view = QtWidgets.QListWidget(self.tab_2)
        self.notes_view.setGeometry(QtCore.QRect(20, 280, 271, 281))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.notes_view.setFont(font)
        self.notes_view.setStyleSheet("background-color:rgb(255,248,220);\n"
"border: 2px solid black;\n"
"border-radius:10px;")
        self.notes_view.setObjectName("notes_view")
        self.groupbox_main = QtWidgets.QComboBox(self.tab_2)
        self.groupbox_main.setGeometry(QtCore.QRect(30, 120, 271, 31))
        self.groupbox_main.setStyleSheet("background-color:rgb(255,248,220);\n"
"border: 2px solid black;\n"
"border-radius:10px;")
        self.groupbox_main.setObjectName("groupbox_main")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(40, 220, 261, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(400, 10, 361, 261))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../images/main_picture.png"))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create_note.setText(_translate("MainWindow", "Создать заметку"))
        self.choice_from_file.setText(_translate("MainWindow", "Создать заметку из файла(txt)"))
        self.add_photo_button.setText(_translate("MainWindow", "Добавить фото"))
        self.delete_photo.setText(_translate("MainWindow", "Удалить фото"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Главная"))
        self.add_group_button.setText(_translate("MainWindow", "Добавить группу"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Список заметок выбранной группы</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Группы"))
