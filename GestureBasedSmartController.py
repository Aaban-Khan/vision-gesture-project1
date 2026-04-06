import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path="../hand_landmarker.task")
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)


def mode_logic(mode, hand, flip, w, h):
    if mode == "Select":
        print("clicked")
    elif mode == "Move":
        # yha loop nhi lagaya cuz hum direct bta rhe hai ki hand[8] use kro! loop lagate agar hume sabhi points par dots draw karne hote
        landmark = hand[8]
        x = int(landmark.x * w)
        y = int(landmark.y * h)
        cv2.circle(flip, (x, y), 5, (0, 0, 255), -1)


cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    flip = cv2.flip(frame, 1)
    h, w, _ = flip.shape

    rgb = cv2.cvtColor(flip, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = detector.detect(mp_image)
    TIPS = [4, 8, 12, 16, 20]
    MIDS = [3, 6, 10, 14, 18]
    NAMES = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
    mode = "IDLE"

    if result.hand_landmarks:
        for hand in result.hand_landmarks:
            finger_count = 0
            fingers_name = []
            for tip, mid, name in zip(TIPS, MIDS, NAMES):

                if hand[tip].y < hand[mid].y:
                    finger_count += 1
                    fingers_name.append(name)
            if fingers_name == ["Index"]:
                mode = "Move"
            elif fingers_name == ["Index", "Middle"]:
                mode = "Select"
            elif fingers_name == ["Thumb", "Index", "Middle", "Ring", "Pinky"]:
                mode = "Reset"
            else:
                mode = "Stop"
            mode_logic(mode, hand, flip, w, h)

            cv2.putText(
                flip,
                f"{finger_count}Finders UP!",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 255),
                1,
            )
            cv2.putText(
                flip,
                f"UP:{', '.join(fingers_name)}",
                (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                1,
            )
            cv2.putText(
                flip,
                f"Mode: {mode}",
                (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                1,
            )

    cv2.imshow("base", flip)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
detector.close()
cv2.destroyAllWindows()
