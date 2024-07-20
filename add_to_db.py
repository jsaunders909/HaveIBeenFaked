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
recognition_data = RecognitionData(name)

print("You will now need to capture 3 photos of the person's face")
print("One photo looking straight ahead, one looking to the left, and one looking to the right.")
print("Press 'l' to capture the left photo, 'r' to capture the right photo, and 'f' to capture the front photo.")
print("When you are done, press 's' to save the face data.")
print("At any time, press 'q' to quit.")

input("Press Enter to continue...")
print("Starting capture...")

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

    elif retval & 0xFF == ord('s'):
        embedding, crop, bbox = model(frame, return_crop=True, return_bbox=True)
        recognition_data.save(f"face_db/{name}.pkl")

        print("Face data saved.")
        break

    elif retval & 0xFF == ord('l'):
        print("Capturing left photo...")
        embedding, crop, bbox = model(frame, return_crop=True, return_bbox=True)

        if embedding is None:
            print("No face detected.")
            continue

        embedding = embedding[0].detach().cpu().numpy()
        
        recognition_data.update_left(embedding)
        print("Left photo captured.")

    elif retval & 0xFF == ord('r'):
        print("Capturing right photo...")
        embedding, crop, bbox = model(frame, return_crop=True, return_bbox=True)

        if embedding is None:
            print("No face detected.")
            continue

        embedding = embedding[0].detach().cpu().numpy()
        
        recognition_data.update_right(embedding)
        print("Right photo captured.")
    
    elif retval & 0xFF == ord('f'):
        print("Capturing front photo...")
        embedding, crop, bbox = model(frame, return_crop=True, return_bbox=True)

        if embedding is None:
            print("No face detected.")
            continue

        embedding = embedding[0].detach().cpu().numpy()
        
        recognition_data.update_front(embedding)
        print("Front photo captured.")
