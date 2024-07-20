import cv2
from models import FRTorch
from utils import draw_bbox, draw_text, draw_labelled_bbox
from recognition_data import RecognitionData

# Get the webcam

cap = cv2.VideoCapture(0)

# Create the face recognition model
width, height = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
model = FRTorch(image_size=256)

# Check if the webcam is opened correctly

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

name = input("Enter the name of the person: ")

print("Starting capture, press 'c' to capture and 'q' to quit.")

# Start capturing the video
while True:
    # Read the frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the frame
    cv2.imshow("Webcam", frame)

    retval = cv2.waitKey(1)

    if retval & 0xFF == ord('q'):
        break

    elif retval & 0xFF == ord('c'):
        embedding, crop, bbox = model(frame, return_crop=True, return_bbox=True)

        if embedding is None:
            print("No face detected.")
            continue

        embedding = embedding[0].detach().cpu().numpy()
        recognition_data = RecognitionData(name, embedding)
        recognition_data.save(f"face_db/{name}.pkl")

        print(f"Saved face data for {name}.")
        break