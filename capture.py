import cv2
import os 

def capture():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("error could not open webcam")
        return 

    ret, frame = cap.read()

    if ret:
        current_dir = os.getcwd()
        photo_path = os.path.join(current_dir, 'photo.jpg')

        cv2.imwrite(photo_path, frame)
        print('photo has been saved')

        cap.release()
        cv2.destroyAllWindows()

    else:
        print("Error: Failed to Capture Frames.")

capture()
