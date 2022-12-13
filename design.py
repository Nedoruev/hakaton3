from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCursor


# import re


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(600)
        MainWindow.setFixedWidth(1100)
        MainWindow.setStyleSheet("background:rgb(47, 150, 171)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1101, 601))
        self.frame.setStyleSheet("border: 4px solid \'#FFFFFF\';\n"
                                 "border-radius: 15px;\n"
                                 "margin: 10px;\n"
                                 "background: #FFFFFF")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 1061, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        #
        #        font.setPointSize(-1)
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setStyleSheet(  # "appearance: none;\n"
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;\n"
            "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(  # "appearance: none;\n"
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(  # "appearance: none;\n"
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;\n"
            "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(  # "appearance: none;\n"
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        #        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget = QtWidgets.QTableView(self.frame)  # QTableView  !!!

        self.tableWidget.setGeometry(QtCore.QRect(40, 220, 1030, 351))
        self.tableWidget.setMinimumSize(QtCore.QSize(1030, 351))
        self.tableWidget.setMaximumSize(QtCore.QSize(1011, 351))
        self.tableWidget.setStyleSheet("border: 4px solid \'#2DACEB\';\n"
                                       "border-radius: 15px;\n"
                                       "margin: 10px;\n"
                                       "background: #FFFFFF")
        self.tableWidget.setObjectName("tableWidget")
        #        self.tableWidget.setColumnCount(0)
        #        self.tableWidget.setRowCount(0)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Общежитие 1"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить запись"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить запись"))
        self.pushButton_4.setText(_translate("MainWindow", "Обновить"))
        self.pushButton.setText(_translate("MainWindow", "Выход"))
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


#        self.pushButton.clicked.connect(self.exitfunc)
#    def exitfunc(self):
#        MainWindow.destroy()





class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.close)

        # +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        self.pushButton_3.clicked.connect(self.add_row)

        # 1. Создайте соединение с базой данных, вызвав метод addDatabase() класса QSqlDatabase.
        #    Так как вы хотите соединиться с базой данных SQLite, параметры QSQLITE передаются здесь.
        db = QSqlDatabase.addDatabase('QSQLITE')

        # 2. Вызовите setDatabaseName(), чтобы установить имя базы данных, которое будет использоваться.
        #    Вам нужно только написать путь, а имя файла заканчивается на .db
        #   (если база данных уже существует, используйте базу данных; если она не существует,
        #    будет создана новая);
        db.setDatabaseName('campus_1.db')  # !!! ваша db

        # 3. Вызовите метод open(), чтобы открыть базу данных.
        #    Если открытие прошло успешно, оно вернет True, а в случае неудачи - False.
        db.open()

        # Создайте модель QSqlTableModel и вызовите setTable(),
        # чтобы выбрать таблицу данных для обработки.


        # def showDialog(self):
        room_number_query = QInputDialog.getText(self, 'Input Dialog', 'Enter your room number:')

        room_number = f"Комната_{room_number_query[0]}"

        self.model = QSqlTableModel(self)
        self.model.setTable(room_number)  # !!! тавлица в db
        print(room_number)

        # вызовите метод select(), чтобы выбрать все данные в таблице, и соответствующее
        # представление также отобразит все данные;
        self.model.select()
        self.tableWidget.setModel(self.model)



    def add_row(self):
        r = self.model.record()
        r.setValue("name", "name")
        r.setValue("age", 30)
        r.setValue("gender", "M")
        self.model.insertRecord(-1, r)
        self.model.select()


# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()

    #    MainWindow = QtWidgets.QMainWindow()
    #    ui = Ui_MainWindow()
    #    ui.setupUi(MainWindow)
    #    MainWindow.show()
    sys.exit(app.exec_())
