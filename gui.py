# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        Main_Window.setObjectName("Main_Window")
        Main_Window.resize(230, 230)
        Main_Window.setMinimumSize(QtCore.QSize(230, 230))
        Main_Window.setMaximumSize(QtCore.QSize(230, 230))
        self.centralwidget = QtWidgets.QWidget(parent=Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.exit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.exit_button.setMinimumSize(QtCore.QSize(0, 0))
        self.exit_button.setObjectName("exit_button")
        self.vote_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.vote_button.setGeometry(QtCore.QRect(20, 150, 71, 21))
        self.vote_button.setObjectName("vote_button")
        self.text_menu = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.text_menu.setGeometry(QtCore.QRect(10, 10, 211, 111))
        self.text_menu.setReadOnly(True)
        self.text_menu.setObjectName("text_menu")
        self.clear_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(130, 150, 71, 21))
        self.clear_button.setMinimumSize(QtCore.QSize(0, 0))
        self.clear_button.setObjectName("clear_button")
        self.john_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.john_button.setEnabled(True)
        self.john_button.setGeometry(QtCore.QRect(20, 150, 71, 21))
        self.john_button.setObjectName("john_button")
        self.jane_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.jane_button.setGeometry(QtCore.QRect(130, 150, 71, 21))
        self.jane_button.setMinimumSize(QtCore.QSize(0, 0))
        self.jane_button.setObjectName("jane_button")
        self.no_vote_text = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.no_vote_text.setGeometry(QtCore.QRect(20, 130, 121, 20))
        self.no_vote_text.setObjectName("no_vote_text")
        self.varify_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.varify_button.setGeometry(QtCore.QRect(140, 130, 71, 21))
        self.varify_button.setMinimumSize(QtCore.QSize(0, 0))
        self.varify_button.setObjectName("varify_button")
        Main_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Main_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 230, 18))
        self.menubar.setObjectName("menubar")
        Main_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Main_Window)
        self.statusbar.setObjectName("statusbar")
        Main_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def retranslateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("Main_Window", "Vote Menu"))
        self.exit_button.setText(_translate("Main_Window", "Exit"))
        self.vote_button.setText(_translate("Main_Window", "Vote"))
        self.text_menu.setPlainText(_translate("Main_Window", "             Total\n"
"John: 0\n"
"Jane: 0\n"
"\n"
"Please put in your NUID to vote"))
        self.clear_button.setText(_translate("Main_Window", "Clear"))
        self.john_button.setText(_translate("Main_Window", "John"))
        self.jane_button.setText(_translate("Main_Window", "Jane"))
        self.varify_button.setText(_translate("Main_Window", "Varify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Window = QtWidgets.QMainWindow()
    ui = Ui_Main_Window()
    ui.setupUi(Main_Window)
    Main_Window.show()
    sys.exit(app.exec())
