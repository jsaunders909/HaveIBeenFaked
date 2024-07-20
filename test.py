import cv2
from models import FRTorch
from utils import draw_bbox, draw_text, draw_labelled_bbox
from models.db_lookup import DBLookup

# Get the webcam

cap = cv2.VideoCapture(0)

# Create the face recognition model
width, height = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
model = FRTorch(image_size=256)
db = DBLookup("face_db")

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

    embedding, crop, bbox = model(frame, return_crop=True, return_bbox=True)

    if embedding is None:
        print("No face detected.")
        continue

    n_faces = embedding.size(0)

    # Convert to BGR
    for i in range(n_faces):
        name = db.lookup(embedding[i].detach().cpu().numpy())
        frame = draw_labelled_bbox(frame, bbox[i], name)
    
    # Display the frame
    cv2.imshow("Webcam", frame)

    # Wait for the user to press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break