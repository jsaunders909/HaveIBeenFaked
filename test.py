import cv2

# Get the webcam

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Read the video stream
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the frame
    cv2.imshow("Webcam", frame)

    # Wait for the user to press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break