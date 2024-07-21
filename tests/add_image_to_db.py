import cv2
from hibf_lib.models import FRTorch
from hibf_lib.utils import draw_bbox, draw_text, draw_labelled_bbox
from hibf_lib.recognition_data import RecognitionData
import uuid


def add_image_to_db(image, name):
    model = FRTorch()
    recognition_data = RecognitionData(name)
    embedding, crop, bbox = model(image, return_crop=True, return_bbox=True)

    if embedding is None:
        print("No face detected.")
        return False

    embedding = embedding[0].detach().cpu().numpy()
    recognition_data.update_front(embedding)

    recognition_data.save(f"face_db/{uuid.uuid4()}.pkl")
    print("Face data saved.")

    return True


if __name__ == "__main__":
    import cv2
    import argparse

    parser = argparse.ArgumentParser(description="Add an image to the database.")
    parser.add_argument("--image", type=str, help="Path to the image.")
    parser.add_argument("--name", type=str, help="Name of the person in the image.")
    args = parser.parse_args()

    image = cv2.imread(args.image)
    add_image_to_db(image, args.name)
