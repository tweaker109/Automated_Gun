import cv2
from pyfirmata import Arduino, util
import pyfirmata
import time

print("Running Target Detection...")

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the camera
cap = cv2.VideoCapture(1)  # Use device index 0 for laptop webcam & 1 for external webcam

board = Arduino('COM3')  # Replace 'COMX' with the actual serial port of your Arduino board

# Set home coordinates
home = 200

step_pin_x = 5
dir_pin_x = 2
en_pin_x = 8

step_pin_y = 9
dir_pin_y = 3
en_pin_y = 10

trigger = 12

board.digital[step_pin_y].mode = pyfirmata.OUTPUT
board.digital[dir_pin_y].mode = pyfirmata.OUTPUT
board.digital[en_pin_y].mode = pyfirmata.OUTPUT
board.digital[en_pin_y].write(0)  # Set the EN pin LOW to enable the motor

board.digital[step_pin_x].mode = pyfirmata.OUTPUT
board.digital[dir_pin_x].mode = pyfirmata.OUTPUT
board.digital[en_pin_x].mode = pyfirmata.OUTPUT
board.digital[en_pin_x].write(0)  # Set the EN pin LOW to enable the motor

def step_xmotor(steps, delay_time):
    board.digital[dir_pin_x].write(1)  # Set the DIR pin HIGH to move in a particular direction
    for _ in range(steps):
        board.digital[step_pin_x].write(1)
        time.sleep(delay_time)
        board.digital[step_pin_x].write(0)
        time.sleep(delay_time)

def step_ymotor(steps, delay_time):
    board.digital[dir_pin_y].write(1)  # Set the DIR pin HIGH to move in a particular direction
    for _ in range(steps):
        board.digital[step_pin_y].write(1)
        time.sleep(delay_time)
        board.digital[step_pin_y].write(0)
        time.sleep(delay_time)

def actuate_solenoid(pin, duration):
    board.digital[pin].mode = pyfirmata.OUTPUT
    board.digital[pin].write(1)  # Activate the solenoid
    time.sleep(duration)
    board.digital[pin].write(0) # Deactivate the solenoid

def home_motors(steps, delay_time):
    board.digital[dir_pin_x].write(1)  # Set the DIR pin HIGH to move in a particular direction
    for _ in range(steps):
        board.digital[step_pin_x].write(1)
        time.sleep(delay_time)
        board.digital[step_pin_x].write(0)
        time.sleep(delay_time)
    board.digital[dir_pin_y].write(1)  # Set the DIR pin HIGH to move in a particular direction
    for _ in range(steps):
        board.digital[step_pin_y].write(1)
        time.sleep(delay_time)
        board.digital[step_pin_y].write(0)
        time.sleep(delay_time)

# Define the top right corner coordinates
top_right_x = 400
top_right_y = 400

# Home motors
home_motors(home, 0.0002)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Get the dimensions of the frame
    height, width, _ = frame.shape

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Check if a face is detected
    if len(faces) > 0:
        # Iterate over the detected faces
        for (x, y, w, h) in faces:
            # Calculate the bottom left corner coordinates
            bottom_left_x = int(x / width * top_right_x)
            bottom_left_y = int(y / height * top_right_y)

            # Draw a green square around the face
            cv2.rectangle(frame, (bottom_left_x, bottom_left_y), (top_right_x, top_right_y), (0, 255, 0), 2)

            # Calculate the center coordinates of the face
            face_center_x = int((x + w / 2) / width * top_right_x)
            face_center_y = int((y + h / 2) / height * top_right_y)

            # Print the calculated coordinates
            print("x:", face_center_x)
            print("y:", face_center_y)

            # Actuate motors
            step_ymotor(face_center_y, 0.0002)  # Call the step_motor function with the desired number of steps and delay time
            step_xmotor(face_center_x, 0.0002)  # Call the step_motor function with the desired number of steps and delay time

            # Actuate solenoid
            actuate_solenoid(trigger, 1.5)

            # Display the frame
            cv2.imshow('USB Webcam', frame)

            # Delay for 0.5 seconds
            time.sleep(0.5)

    else:
        # No face detected, set the face_center coordinates to (200, 200)
        face_center_x = 200
        face_center_y = 200

        # Print the default coordinates
        print("No face detected")

        # Display the frame without a rectangle
        cv2.imshow('USB Webcam', frame)

    time.sleep(0.5)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Home motors
home_motors(home, 0.0002)

# Release the webcam and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()

# Turn off the Arduino
board.exit()


