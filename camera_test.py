import cv2

# Set the IP address and port of the wireless camera
camera_ip = "http://192.168.0.100/"  # Replace with the actual IP address
camera_port = 901  # Replace with the actual port

# Create the video capture object
video_capture = cv2.VideoCapture(f"http://{camera_ip}:{camera_port}/video")

# Check if the video capture object was successfully created
if not video_capture.isOpened():
    print("Failed to connect to the wireless camera.")
    exit()

# Continuously read and display frames from the camera
while True:
    # Read the next frame from the camera
    ret, frame = video_capture.read()

    # Check if the frame was successfully read
    if not ret:
        print("Failed to read frame from the camera.")
        break

    # Display the frame
    cv2.imshow("Wireless Camera", frame)

    # Wait for the 'q' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close the display window
video_capture.release()
cv2.destroyAllWindows()
