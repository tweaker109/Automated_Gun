import cv2

for i in range(10):  # Try up to 10 device indices
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Device index {i} is open")
        cap.release()
    else:
        print(f"Device index {i} is not open")

