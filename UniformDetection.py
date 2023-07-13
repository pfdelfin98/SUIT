import cv2
import cvzone
import math
import time
import screeninfo
from ultralytics import YOLO
from send_logs import send_logs_to_db


class UniformDetectionWindow(object):
    def __init__(self):
        self.detect_person_model = YOLO("yolov8m.pt")
        self.classNames_person = ["Person"]

        self.detect_unif_model = YOLO("./segment/weights/best.pt")
        self.classnames = [
            "Female_Uniform",
            "Male_Uniform",
        ]

        # Detection Config
        self.accepted_valid_conf = 0.8

        # Video config
        screen = screeninfo.get_monitors()[0]
        width, height = screen.width, screen.height
        self.video_width = width
        self.video_height = height
        self.x = -5  # Adjust for screen pop up position
        self.y = 20  # Adjust for screen pop up position

    def uniform_detection_func(self):
        cap = cv2.VideoCapture("./segment/test/male/vid/3.mp4")
        # cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_height)

        person_detected = False
        detection_found = False

        valid_detection_started = False
        valid_detection_start_time = None
        valid_detection_duration = 0

        invalid_detection_started = False
        invalid_detection_start_time = None
        invalid_detection_duration = 0

        log_sent = False
        while True:
            success, img = cap.read()
            results = self.detect_person_model(
                img, stream=True, classes=[0, 1], conf=0.9
            )
            for r in results:
                if len(r) > 0:
                    person_detected = True
                else:
                    person_detected = False

                if person_detected:
                    unif_results = self.detect_unif_model(
                        img, stream=True, conf=self.accepted_valid_conf
                    )
                    for unif_r in unif_results:
                        if len(unif_r) > 0:
                            unif_boxes = unif_r.boxes
                            for u_box in unif_boxes:
                                # Bounding Box
                                x1, y1, x2, y2 = u_box.xyxy[0]
                                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                                w, h = x2 - x1, y2 - y1
                                u_conf = math.ceil((u_box.conf[0] * 100)) / 100

                                if u_conf > self.accepted_valid_conf:
                                    detection_found = True

                                    if not valid_detection_started:
                                        valid_detection_start_time = time.time()
                                        valid_detection_started = True
                                # Class Name
                                cls = int(u_box.cls[0])

                                cvzone.cornerRect(img, (x1, y1, w, h))

                                cvzone.putTextRect(
                                    img,
                                    f"{self.classnames[cls]} {u_conf}",
                                    (max(0, x1), max(35, y1)),
                                    scale=1,
                                    thickness=1,
                                )
                        else:
                            print("Invalid Uniform Detected")
                            detection_found = False

                            if not invalid_detection_started:
                                invalid_detection_start_time = time.time()
                                invalid_detection_started = True

                    if detection_found:
                        invalid_detection_duration = 0
                    else:
                        valid_detection_duration = 0

                    current_time = time.time()
                    print(f"Valid detection seconds: {int(valid_detection_duration)}")
                    print(
                        f"Invalid detection seconds: {int(invalid_detection_duration)}"
                    )

                    if valid_detection_started:
                        if detection_found:
                            valid_detection_duration = (
                                current_time - valid_detection_start_time
                            )

                    if invalid_detection_started:
                        if not detection_found:
                            invalid_detection_duration = (
                                current_time - invalid_detection_start_time
                            )

                    if int(valid_detection_duration) >= 5:
                        cvzone.putTextRect(
                            img,
                            f"Proper uniform Detected",
                            (10, 25),
                            scale=2,
                            thickness=2,
                            colorR=(0, 255, 0),  # Green
                        )
                        if not log_sent:
                            print("------------")
                            print("Sending logs to db")
                            print("------------")
                            send_logs_to_db(unif_detect_choice="PROPER")
                            log_sent = True
                    elif int(invalid_detection_duration) >= 5:
                        cvzone.putTextRect(
                            img,
                            f"Improper Uniform Detected",
                            (10, 25),
                            scale=2,
                            thickness=2,
                            colorR=(0, 0, 255),  # Red
                        )
                        if not log_sent:
                            print("------------")
                            print("Sending logs to db")
                            print("------------")
                            send_logs_to_db(unif_detect_choice="IMPROPER")
                            log_sent = True
                    else:
                        cvzone.putTextRect(
                            img,
                            f"Person Detected",
                            (10, 25),
                            scale=2,
                            thickness=2,
                            colorR=(255, 0, 0),  # Blue
                        )
                else:
                    current_time = time.time()
                    valid_detection_duration = 0
                    invalid_detection_duration = 0
                    valid_detection_started = False
                    invalid_detection_started = False
                    log_sent = False
                    cvzone.putTextRect(
                        img,
                        f"No Person Detected",
                        (10, 25),
                        scale=2,
                        thickness=3,
                        font=cv2.FONT_HERSHEY_PLAIN,
                        colorR=(0, 0, 0),
                    )

            cv2.imshow("Image", img)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            cv2.waitKey(1)
