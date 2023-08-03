import sys
import os
import logs
import numpy as np
import pymysql
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QScrollArea,
)
import openpyxl
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from docxtpl import DocxTemplate, InlineImage


class Ui_Dashboard(object):
    def __init__(self) -> None:
        self.logs_sent = False
        self.existing = False

        # For Excel File
        self.file_name = ""
        self.file_path = ""
        self.folder_name = "Analytics"
        self.folder_path = rf"C:\Users\SampleUser\Desktop\{self.folder_name}"  # Change this to your own file path

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow

        MainWindow.setObjectName("MainWindow")
        self.MainWindow.showMaximized()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

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

        self.logoutBtn = QtWidgets.QPushButton(self.frame)
        self.logoutBtn.setGeometry(QtCore.QRect(40, 350, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.logoutBtn.setFont(font)
        self.logoutBtn.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.logoutBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.logoutBtn.setObjectName("logoutBtn")

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

        self.exportDocxBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exportDocxBtn.setGeometry(QtCore.QRect(1550, 90, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.exportDocxBtn.setFont(font)
        self.exportDocxBtn.setObjectName("exportDocxBtn")
        self.exportDocxBtn.setText("Export Document")
        self.exportDocxBtn.setStyleSheet(
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
        self.exportDocxBtn.clicked.connect(self.export_data_to_docx)

        # Filter
        self.available_filters = {
            "ALL": 0,
            "Daily": [datetime.now().day, "day"],
            "Weekly": [datetime.now().isocalendar()[1], "week"],
            "Monthly": [datetime.now().month, "month"],
            "Yearly": [datetime.now().year, "year"],
        }
        self.filterComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.filterComboBox.setGeometry(QtCore.QRect(970, 95, 100, 30))
        self.filterComboBox.setObjectName("filterComboBox")
        [
            self.filterComboBox.addItem(filter)
            for filter in self.available_filters.keys()
        ]
        self.filterComboBox.setCurrentIndex(0)
        self.filterComboBox.currentTextChanged.connect(self.search_logs)

        self.filterLabel = QtWidgets.QLabel(self.centralwidget)
        self.filterLabel.setGeometry(QtCore.QRect(920, 95, 70, 30))
        self.filterLabel.setObjectName("filterLabel")
        self.filterLabel.setText("Filters:")

        # Search
        self.searchComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.searchComboBox.setGeometry(QtCore.QRect(1180, 95, 200, 30))
        self.searchComboBox.setObjectName("searchComboBox")
        self.searchComboBox.addItem("ALL")
        self.searchComboBox.addItem("CABEIHM")
        self.searchComboBox.addItem("CAS")
        self.searchComboBox.addItem("CICS")
        self.searchComboBox.addItem("CET")
        self.searchComboBox.addItem("CONAHS")
        self.searchComboBox.addItem("CTE")
        self.searchComboBox.addItem("LABORATORY SCHOOL")
        self.searchComboBox.setCurrentIndex(0)
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
        self.logoutBtn.clicked.connect(QtWidgets.qApp.quit)
        self.search_logs()

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
        self.logoutBtn.setText(_translate("MainWindow", "Exit"))

        self.label_10.setText(_translate("MainWindow", "Dashboard"))
        self.label.setText(
            _translate(
                "MainWindow",
                "SUIT: School Uniform Identifier Technology using Object Detection",
            )
        )

    def start_loading_students(self):
        # Start loading the students initially
        # self.load_logs()
        print("Load Students")

    def open_detection(self):
        from UniformDetection import UniformDetectionWindow

        detection = UniformDetectionWindow()

        detection.uniform_detection_func()

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
        # Get the selected department and filter
        self.selected_department = self.searchComboBox.currentText()
        self.selected_filter = self.filterComboBox.currentText()
        current_date = datetime.now().date()

        # Connect to the MySQL database
        connection = pymysql.connect(
            host="localhost", user="root", password="", database="suit_db"
        )
        self.categories = []
        self.improper_log_count = []
        self.proper_log_count = []

        try:
            # Execute the query and fetch the course and gender data
            cursor = connection.cursor()
            if self.selected_department == "ALL" and self.selected_filter == "ALL":
                query = "SELECT department, SUM(CASE WHEN unif_detect_result = 'IMPROPER' THEN 1 ELSE 0 END) AS improper_log_count, SUM(CASE WHEN unif_detect_result = 'PROPER' THEN 1 ELSE 0 END) AS proper_log_count FROM tbl_detect_log GROUP BY department"
            elif self.selected_department == "ALL" and self.selected_filter != "ALL":
                query = f"SELECT department, SUM(CASE WHEN unif_detect_result = 'IMPROPER' THEN 1 ELSE 0 END) AS improper_log_count, SUM(CASE WHEN unif_detect_result = 'PROPER' THEN 1 ELSE 0 END) AS proper_log_count FROM tbl_detect_log WHERE {self.available_filters[self.selected_filter][1]}(date_log)={self.available_filters[self.selected_filter][0]} GROUP BY department"
            elif self.selected_department != "ALL" and self.selected_filter == "ALL":
                query = f"SELECT course, SUM(CASE WHEN unif_detect_result = 'IMPROPER' THEN 1 ELSE 0 END) AS improper_log_count, SUM(CASE WHEN unif_detect_result = 'PROPER' THEN 1 ELSE 0 END) AS proper_log_count FROM tbl_detect_log WHERE department= '{self.selected_department}' GROUP BY course"
            else:
                query = f"SELECT course, SUM(CASE WHEN unif_detect_result = 'IMPROPER' THEN 1 ELSE 0 END) AS improper_log_count, SUM(CASE WHEN unif_detect_result = 'PROPER' THEN 1 ELSE 0 END) AS proper_log_count FROM tbl_detect_log WHERE department = '{self.selected_department}' and {self.available_filters[self.selected_filter][1]}(date_log)={self.available_filters[self.selected_filter][0]} GROUP BY course"

            cursor.execute(query)
            if cursor.rowcount > 0:
                for row in cursor.fetchall():
                    course, improper_log_count, proper_log_count = row
                    self.categories.append(course)
                    self.improper_log_count.append(improper_log_count)
                    self.proper_log_count.append(proper_log_count)

            else:
                self.improper_log_count = [0]
                self.proper_log_count = [0]

        finally:
            connection.close()

        for i in reversed(range(self.barChartLayout.count())):
            self.barChartLayout.itemAt(i).widget().setParent(None)

        figure, ax = plt.subplots()

        self.draw_bar_graph(ax)

        canvas = FigureCanvas(figure)

        self.barChartLayout.addWidget(canvas)

        # Save the plot image
        img = self.figuretoimage(plt.gcf())
        img.save("Plot image.png")

    def draw_bar_graph(self, ax, is_department: bool = False):
        bar_width = 0.35
        x = np.arange(len(self.categories))
        xlabel = "Courses"
        if is_department:
            xlabel = "Departments"

        ax.clear()

        ax.bar(
            x - bar_width / 2,
            self.improper_log_count,
            width=bar_width,
            label="Improper",
            color="#4F81BD",
        )
        ax.bar(
            x + bar_width / 2,
            self.proper_log_count,
            width=bar_width,
            label="Proper",
            color="#C0504D",
        )

        yvalue = ax.get_ybound()[1]
        ax.set_xlabel(xlabel)
        ax.set_ylabel("Count")
        ax.set_ybound(upper=(yvalue * 2) / 1.5)
        ax.set_title(
            f"School Uniform Analytics for {self.selected_department} Department"
        )
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
            categories = ("Course", "Improper Uniform", "Proper Uniform")
            if self.selected_department == "ALL" and self.selected_filter == "ALL":
                query = "SELECT department, SUM(CASE WHEN unif_detect_result = 'IMPROPER' THEN 1 ELSE 0 END) AS improper_log_count, SUM(CASE WHEN unif_detect_result = 'PROPER' THEN 1 ELSE 0 END) AS proper_log_count FROM tbl_detect_log GROUP BY department"
                categories = ("Department", "Improper Uniform", "Proper Uniform")
            elif self.selected_department == "ALL" and self.selected_filter != "ALL":
                query = f"SELECT department, SUM(CASE WHEN unif_detect_result = 'IMPROPER' THEN 1 ELSE 0 END) AS improper_log_count, SUM(CASE WHEN unif_detect_result = 'PROPER' THEN 1 ELSE 0 END) AS proper_log_count FROM tbl_detect_log WHERE {self.available_filters[self.selected_filter][1]}(date_log)={self.available_filters[self.selected_filter][0]} GROUP BY department"
                categories = ("Department", "Improper Uniform", "Proper Uniform")
            elif self.selected_department != "ALL" and self.selected_filter == "ALL":
                query = f"SELECT course, SUM(CASE WHEN unif_detect_result = 'IMPROPER' THEN 1 ELSE 0 END) AS improper_log_count, SUM(CASE WHEN unif_detect_result = 'PROPER' THEN 1 ELSE 0 END) AS proper_log_count FROM tbl_detect_log WHERE department= '{self.selected_department}' GROUP BY course"
            else:
                query = f"SELECT course, SUM(CASE WHEN unif_detect_result = 'IMPROPER' THEN 1 ELSE 0 END) AS improper_log_count, SUM(CASE WHEN unif_detect_result = 'PROPER' THEN 1 ELSE 0 END) AS proper_log_count FROM tbl_detect_log WHERE department = '{self.selected_department}' and {self.available_filters[self.selected_filter][1]}(date_log)={self.available_filters[self.selected_filter][0]} GROUP BY course"

            cursor.execute(query)
            chart_data = cursor.fetchall()

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
            self.file_name = f"{self.selected_filter}_Analytics_for_{self.selected_department}_{formatted_datetime}.xlsx"

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

    def export_data_to_docx(self):
        self.selected_department = "ALL"
        # Connect to the MySQL database
        connection = pymysql.connect(
            host="localhost", user="root", password="", database="suit_db"
        )
        self.categories = []
        self.improper_log_count = []
        self.proper_log_count = []

        try:
            # Execute the query and fetch the course and gender data
            cursor = connection.cursor()
            query = f"SELECT department, SUM(CASE WHEN unif_detect_result = 'IMPROPER' THEN 1 ELSE 0 END) AS improper_log_count, SUM(CASE WHEN unif_detect_result = 'PROPER' THEN 1 ELSE 0 END) AS proper_log_count FROM tbl_detect_log GROUP BY department"

            cursor.execute(query)
            if cursor.rowcount > 0:
                for row in cursor.fetchall():
                    course, improper_log_count, proper_log_count = row
                    self.categories.append(course)
                    self.improper_log_count.append(improper_log_count)
                    self.proper_log_count.append(proper_log_count)

            else:
                self.improper_log_count = [0]
                self.proper_log_count = [0]

        finally:
            connection.close()

        for i in reversed(range(self.barChartLayout.count())):
            self.barChartLayout.itemAt(i).widget().setParent(None)

        figure, ax = plt.subplots()

        self.draw_bar_graph(ax)

        self.filterComboBox.setCurrentIndex(0)
        self.searchComboBox.setCurrentIndex(0)
        # Save the plot image
        chart_img = self.figuretoimage(plt.gcf())
        self.generate_docx(chart_img)

    def figuretoimage(self, figure):
        import io
        from PIL import Image

        buf = io.BytesIO()
        figure.savefig(buf, bbox_inches="tight", dpi=400)
        buf.seek(0)
        img = Image.open(buf)
        return img

    def generate_docx(self, chart_img):
        now = datetime.now()
        datetime_str = now.strftime("%m-%d-%Y-%H-%M-%S")

        newimg = chart_img.resize((450, 250))
        newimg.save("chart.png")
        try:
            doc = DocxTemplate(r"templates\report.docx")
            dic = {
                "graph": InlineImage(doc, "chart.png"),
                "date": now.strftime("%m/%d/%Y, %H:%M:%S"),
            }

            doc.render(dic)
            document_name = (
                f"Document_Analytics_{self.selected_department}_{datetime_str}.docx"
            )
            document_path = rf"{self.folder_path}\{document_name}"
            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path)
            doc.save(document_path)
            print("Dashboard All Data exported to Word successfully!")
        except Exception as e:
            print("Error exporting data to Word:", str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dashboard()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
