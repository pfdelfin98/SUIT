import cv2
import cvzone
import math
import time
import screeninfo
from ultralytics import YOLO


class UniformDetectionWindow(object):
    def __init__(self):
        self.model = YOLO("./segment/weights/best.pt")
        self.classnames = [
            "Female_Uniform",
            "Male_Uniform",
        ]

        # Detection Config
        self.accepted_valid_conf = 0.7

        # Video config
        screen = screeninfo.get_monitors()[0]
        width, height = screen.width, screen.height
        self.video_width = width
        self.video_height = height
        self.x = -5  # Adjust for screen pop up position
        self.y = 20  # Adjust for screen pop up position

    def uniform_detection_func(self):
        # cap = cv2.VideoCapture("./segment/test/male/vid/1.mp4")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_height)
        cap.set(cv2.CAP_PROP_FPS, 25)

        valid_count = 0
        prev_time = time.time()
        valid_detection_duration = 0
        invalid_detection_duration = 0

        detection_started = False
        detection_start_time = None
        last_valid_detection_time = 0

        while True:
            success, frame = cap.read()
            results = self.model(frame, stream=True, conf=0.5, agnostic_nms=True)

            detection_found = False

            for r in results:
                boxes = r.boxes
                for box in boxes:
                    # Bounding Box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    w, h = x2 - x1, y2 - y1

                    # Confidence
                    confidence = math.ceil((box.conf[0] * 100)) / 100
                    if confidence > self.accepted_conf:
                        valid_count += 1
                        detection_found = True

                        if not detection_started:
                            detection_start_time = time.time()
                            detection_started = True

                        last_valid_detection_time = time.time()

                    # Class Name
                    cls = int(box.cls[0])

                    cvzone.cornerRect(frame, (x1, y1, w, h))
                    cvzone.putTextRect(
                        frame,
                        f"{self.classnames[cls]} {confidence}",
                        (max(0, x1), max(35, y1)),
                        scale=1,
                        thickness=1,
                    )

            if detection_found:
                invalid_detection_duration = 0
            else:
                invalid_detection_duration = time.time() - last_valid_detection_time

            current_time = time.time()

            if current_time - prev_time >= 1.0:
                print(f"Valid detection seconds: {abs(valid_detection_duration)}")
                print(
                    f"No/Invalid detection seconds: {0 if abs(invalid_detection_duration)>1000 else abs(invalid_detection_duration)}"
                )
                valid_count = 0
                prev_time = current_time

            if detection_started:
                if detection_found:
                    valid_detection_duration = current_time - detection_start_time
                else:
                    valid_detection_duration = 0
                    detection_started = False

            window_name = "Uniform Detection"
            cv2.namedWindow(window_name, cv2.WINDOW_FULLSCREEN)
            cv2.moveWindow(window_name, self.x, self.y)
            cv2.imshow(window_name, frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
