import pymysql
import random
from datetime import datetime


def get_random_department_course():
    departments = {
        "CABEIHM": [
            "BS in Accountancy",
            "BS in Management Accounting",
            "BS in Business Administration",
            "BS in Hospitality Management",
            "BS in Tourism Management",
        ],
        "CAS": [
            "BA in Communication",
            "BS in Criminology",
            "BS in Food Technology",
            "BS in Psychology",
            "BS in Fisheries and Aquatic Sciences",
        ],
        "CICS": ["BS in Computer Science", "BS in Information Technology"],
        "CET": ["BS in Computer Engineering", "BS in Industrial Technology"],
        "CONAHS": ["BS in Nursing", "BS in Nutrition and Dietetics"],
        "CTE": [
            "BS in Elementary Education",
            "BS in Secondary Education",
            "BS in Physical Education",
            "Professional Teacher Education",
        ],
    }
    department, courses = random.choice(list(departments.items()))
    course = random.choice(courses)
    return department, course


def send_logs_to_db(*, unif_detect_choice):
    # Connect to the MySQL database
    current_date = datetime.now()
    connection = pymysql.connect(
        host="localhost", user="root", password="", db="suit_db"
    )
    department, course = get_random_department_course()

    try:
        with connection.cursor() as cursor:
            query = "INSERT INTO tbl_detect_log (date_log, time_log, department, course, unif_detect_result) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(
                query,
                (
                    current_date.date(),
                    current_date.time(),
                    department,
                    course,
                    unif_detect_choice,
                ),
            )
            connection.commit()
    except Exception as e:
        print("Error: ", e)
        connection.close()
        return False
    else:
        print("Successfully sent logs to dbase")
        connection.close()
        return True
