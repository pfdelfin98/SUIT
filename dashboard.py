import sys
import os
import logs
import numpy as np
import pymysql
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QLabel,
)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from datetime import datetime, timedelta
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QTableWidget,
    QScrollArea,
)
import openpyxl
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_Dashboard(object):
    def __init__(self) -> None:
        self.logs_sent = False
        self.existing = False

        # For Excel File
        self.file_name = ""
        self.file_path = ""
        self.folder_name = "Analytics"
        self.folder_path = rf"C:\Users\Public\Documents\{self.folder_name}"  # Change this to your own file path

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        # MainWindow.setWindowFlags(
        #     MainWindow.windowFlags()
        #     & ~QtCore.Qt.WindowMinimizeButtonHint
        #     & ~QtCore.Qt.WindowMaximizeButtonHint
        # )

        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1200, 700)
        self.MainWindow.showMaximized()
        # MainWindow.setWindowFlags(
        #     MainWindow.windowFlags()
        #     & ~QtCore.Qt.WindowCloseButtonHint  # Remove the close button
        # )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Add table widget
        # self.tableWidget = QTableWidget(self.centralwidget)
        # self.tableWidget.setGeometry(QtCore.QRect(310, 150, 850, 450))
        # self.tableWidget.setObjectName("tableWidget")

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 1, 261, 2000))
        self.frame.setStyleSheet("background-color:#c82333;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 101, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(44, 110, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")

        self.dashboardBtn = QtWidgets.QPushButton(self.frame)
        self.dashboardBtn.setGeometry(QtCore.QRect(40, 200, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.dashboardBtn.setFont(font)
        self.dashboardBtn.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.dashboardBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.dashboardBtn.setObjectName("dashboardBtn")

        self.logsBtn = QtWidgets.QPushButton(self.frame)
        self.logsBtn.setGeometry(QtCore.QRect(40, 250, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.logsBtn.setFont(font)
        self.logsBtn.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.logsBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.logsBtn.setObjectName("logsBtn")

        self.detectionBtn = QtWidgets.QPushButton(self.frame)
        self.detectionBtn.setGeometry(QtCore.QRect(40, 300, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.detectionBtn.setFont(font)
        self.detectionBtn.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.detectionBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.detectionBtn.setObjectName("detectionBtn")

        
    
        self.exitBtn = QtWidgets.QPushButton(self.frame)
        self.exitBtn.setGeometry(QtCore.QRect(40, 350, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.exitBtn.setFont(font)
        self.exitBtn.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.exitBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.exitBtn.setObjectName("exitBtn")

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(261, -1, 2000, 61))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(20, 10, 671, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(310, 90, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:black;")
        self.label_10.setObjectName("label_10")

        self.exportDataBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exportDataBtn.setGeometry(QtCore.QRect(1420, 90, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.exportDataBtn.setFont(font)
        self.exportDataBtn.setObjectName("exportDataBtn")
        self.exportDataBtn.setText("Export Data")
        self.exportDataBtn.setStyleSheet(
            """
            QPushButton {
                background-color: #dc3545;  
                border: none;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
                font-family: Arial;
                font-size: 8pt;
            }

            QPushButton:hover {
                background-color: #c82333;  
            }
            """
        )
        self.exportDataBtn.clicked.connect(self.export_data_to_excel)

        self.searchComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.searchComboBox.setGeometry(QtCore.QRect(1180, 95, 200, 30))
        self.searchComboBox.setObjectName("searchComboBox")
        self.searchComboBox.addItem("CABEIHM")
        self.searchComboBox.addItem("CAS")
        self.searchComboBox.addItem("CICS")
        self.searchComboBox.addItem("CET")
        self.searchComboBox.addItem("CONAHS")
        self.searchComboBox.addItem("CTE")
        self.searchComboBox.addItem("LABORATORY SCHOOL")
        self.searchComboBox.currentTextChanged.connect(self.search_logs)

        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setGeometry(QtCore.QRect(1100, 95, 70, 30))
        self.searchLabel.setObjectName("searchLabel")
        self.searchLabel.setText("Department:")

        # BARCHART
        self.barChart = QtWidgets.QWidget(self.centralwidget)
        self.barChart.setGeometry(QtCore.QRect(385, 180, 1100, 500))
        self.barChart.setObjectName("barChart")
        self.barChartLayout = QtWidgets.QVBoxLayout(self.barChart)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1186, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.detectionBtn.clicked.connect(self.open_detection)
        self.logsBtn.clicked.connect(self.open_logs)
        self.exitBtn.clicked.connect(QtWidgets.qApp.quit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate(
                "MainWindow",
                "SUIT: School Uniform Identifier Technology using Object Detection",
            )
        )
        self.label_9.setText(_translate("MainWindow", "      SUIT"))
        self.dashboardBtn.setText(_translate("MainWindow", "Dashboard"))
        self.logsBtn.setText(_translate("MainWindow", "Improper Uniform Monitoring"))
        self.detectionBtn.setText(_translate("MainWindow", "Detection"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))

        self.label_10.setText(_translate("MainWindow", "Dashboard"))
        self.label.setText(_translate("MainWindow", "SUIT: School Uniform Identifier Technology using Object Detection"))

    def start_loading_students(self):
        # Start loading the students initially
        # self.load_logs()
        print("Load Students")

    def open_detection(self):
        # Uniform Detection Window
        print("Opening Uniform Detection...")



    def open_logs(self):
        print("Opening Logs...")
        self.MainWindow.hide()
        self.logs_window = QtWidgets.QMainWindow()
        self.ui = logs.Logs()
        self.ui.setupUi(self.logs_window)
        self.ui.tableWidget.setParent(self.ui.centralwidget)
        self.ui.load_logs()
        self.logs_window.show()

    def search_logs(self):
        self.selected_department = self.searchComboBox.currentText()
        current_date = datetime.now().date()

        # Connect to the MySQL database
        connection = pymysql.connect(
            host="localhost", user="root", password="", database="suit_db"
        )
        self.categories = []
        self.male_log_counts = []
        self.female_log_counts = []

        try:
            # Execute the query and fetch the course and gender data
            cursor = connection.cursor()
            query = f"SELECT \
                        s.course, \
                        SUM(CASE WHEN s.gender = 'male' THEN 1 ELSE 0 END) AS male_log_count, \
                        SUM(CASE WHEN s.gender = 'female' THEN 1 ELSE 0 END) AS female_log_count \
                    FROM \
                        tbl_student s \
                    JOIN \
                        tbl_logs l ON s.id = l.student_id \
                    WHERE l.improper = '1' and s.department = '{self.selected_department}' AND l.date_log = '{current_date}' AND l.log_type = 'LOGGED_IN' \
                    GROUP BY s.course"
            cursor.execute(query)
            if cursor.rowcount > 0:
                for row in cursor.fetchall():
                    course, male_counts, female_counts = row
                    self.categories.append(course)
                    self.male_log_counts.append(male_counts)
                    self.female_log_counts.append(female_counts)

            else:
                self.male_log_counts = [0]
                self.female_log_counts = [0]

        finally:
            connection.close()

        for i in reversed(range(self.barChartLayout.count())):
            self.barChartLayout.itemAt(i).widget().setParent(None)

        figure, ax = plt.subplots()

        self.draw_bar_graph(ax)

        canvas = FigureCanvas(figure)

        self.barChartLayout.addWidget(canvas)

    def draw_bar_graph(self, ax):
        bar_width = 0.35
        x = np.arange(len(self.categories))

        ax.clear()

        ax.bar(
            x - bar_width / 2,
            self.male_log_counts,
            width=bar_width,
            label="Male",
            color="#4F81BD",
        )
        ax.bar(
            x + bar_width / 2,
            self.female_log_counts,
            width=bar_width,
            label="Female",
            color="#C0504D",
        )

        yvalue = ax.get_ybound()[1]
        ax.set_xlabel("Courses")
        ax.set_ylabel("Count")
        ax.set_ybound(upper=(yvalue * 2) / 1.5)
        ax.set_title(f"Improper Uniform Analytics for {self.selected_department} Department")
        ax.set_xticks(x)
        ax.set_xticklabels(self.categories)
        ax.legend()

    def export_data_to_excel(self):
        from openpyxl.chart import BarChart, Reference

        # Connect to the MySQL database
        current_date = datetime.now().date()
        connection = pymysql.connect(
            host="localhost", user="root", password="", database="suit_db"
        )

        try:
            # Execute the query and fetch the gender and gender data
            cursor = connection.cursor()
            query = f"SELECT \
                        s.course, \
                        SUM(CASE WHEN s.gender = 'male' THEN 1 ELSE 0 END) AS male_log_count, \
                        SUM(CASE WHEN s.gender = 'female' THEN 1 ELSE 0 END) AS female_log_count \
                    FROM \
                        tbl_student s \
                    JOIN \
                        tbl_logs l ON s.id = l.student_id \
                    WHERE tbl_logs.improper = '1' and s.department = '{self.selected_department}' AND l.date_log = '{current_date}' AND l.log_type = 'LOGGED_IN' \
                    GROUP BY s.course"
            cursor.execute(query)
            chart_data = cursor.fetchall()

            categories = ("Course", "Male", "Female")
            rows = [categories]  # Column headers for excel file
            for row in chart_data:
                rows.append(row)

            # Create a new Excel workbook and select the active sheet
            workbook = openpyxl.Workbook(write_only=True)
            sheet = workbook.create_sheet()

            for _ in rows:
                sheet.append(_)

            # Bar Chart Config
            chart1 = BarChart()
            chart1.type = "col"
            chart1.style = 10
            chart1.title = "Dashboard"
            chart1.y_axis.title = "Count"
            chart1.x_axis.title = "Courses"
            chart1.height = 10
            chart1.width = 20

            chart_data = Reference(
                sheet, min_col=2, min_row=1, max_row=len(rows), max_col=3
            )
            categories = Reference(sheet, min_col=1, min_row=2, max_row=len(rows))
            chart1.add_data(chart_data, titles_from_data=True)
            chart1.shape = 5
            sheet.add_chart(chart1, "E2")

            # Save the Excel file
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            self.file_name = (
                f"Analytics_{self.selected_department}_{formatted_datetime}.xlsx"
            )

            # Save the Excel file inside the "folder_path" folder
            self.file_path = rf"{self.folder_path}\{self.file_name}"

            # Create the "logs" folder if it doesn't exist
            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path)
            # Save the Excel file
            workbook.save(self.file_path)
            print("Logs Data exported to Excel successfully!")

        except Exception as e:
            print("Error exporting data to Excel:", str(e))

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dashboard()
    ui.setupUi(MainWindow)
    # ui.load_logs()
    MainWindow.show()
    sys.exit(app.exec_())
