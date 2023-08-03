import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import dashboard
from error_pop import ErrorDialog


class Ui_Form(object):
    def setupUi(self, Form):
        self.MainWindow = Form
        Form.setObjectName("Form")
        Form.resize(639, 467)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 590, 420))
        self.widget.setStyleSheet(
            "QPushButton#pushButton{\n"
            "    background-color:rgba(85, 98, 112, 255);\n"
            "    color:rgba(255, 255, 255, 200);\n"
            "    border-radius:5px;\n"
            "}\n"
            "QPushButton#pushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(255, 107, 107, 255);\n"
            "    background-position:calc(100% - 10px)center;\n"
            "}\n"
            "QPushButton#pushButton:hover{\n"
            "    background-color:rgba(255, 107, 107, 255);\n"
            "}"
        )
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(290, 40, 260, 330))
        self.label.setStyleSheet(
            "background-color:rgba(255, 255, 255, 255);\n" "border-radius:10px;"
        )
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 25, 270, 360))
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255,114,118, 255), stop:1 rgba(178,20,20,255));\n"
            "border-radius:10px;"
        )
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(330, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 140, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\n"
            "border:2px solid rgba(0, 0, 0, 0);\n"
            "border-bottom-color:rgba(46, 82, 101, 200);\n"
            "color:rgb(0, 0, 0);\n"
            "padding-bottom:7px;"
        )
        self.lineEdit.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 200, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\n"
            "border:2px solid rgba(0, 0, 0, 0);\n"
            "border-bottom-color:rgba(46, 82, 101, 200);\n"
            "color:rgb(0, 0, 0);\n"
            "padding-bottom:7px;"
        )
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(330, 280, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(80, 210, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 220);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(60, 260, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgba(255, 255, 255, 220);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(70, 80, 201, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(150)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("image: url(img/BatStateU-NEU-Logo.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", " User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton.setText(_translate("Form", "Log In"))
        self.label_5.setText(_translate("Form", "SUIT"))
        self.label_6.setText(
            _translate("Form", "School Uniform\n" "Identifier Technology")
        )

    def login(self):
        # Get the entered username and password
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        print("Username:", username)
        print("Password:", password)

        # Perform database connection and login validation
        db = pymysql.connect(host="localhost", user="root", password="", db="suit_db")
        cursor = db.cursor()

        # Perform the login query
        query = "SELECT * FROM tbl_admin WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            # Successful login
            print("Login successful!")
            self.MainWindow.close()
            self.open_dashboard()
        else:
            # Failed login
            print("Invalid username or password")
            self.lineEdit_2.clear()
            self.lineEdit.clear()
            dialog = ErrorDialog()
            dialog.setupUi()
            dialog.exec_()

        # Close the database connection
        cursor.close()
        db.close()

    def open_dashboard(self):
        print("Opening Dashboard...")
        self.MainWindow.hide()
        self.dashboard_window = QtWidgets.QMainWindow()
        self.ui = dashboard.Ui_Dashboard()
        self.ui.setupUi(self.dashboard_window)
        self.dashboard_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
