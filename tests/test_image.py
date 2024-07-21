import cv2
from hibf_lib.models import FRTorch
from hibf_lib.utils import draw_bbox, draw_text, draw_labelled_bbox
from hibf_lib.models.db_lookup import DBLookup


def check_image(image):
    model = FRTorch()
    db = DBLookup("face_db")
    embedding, crop, bbox = model(image, return_crop=True, return_bbox=True)

    if embedding is None:
        print("No face detected.")
        return None

    n_faces = embedding.size(0)

    names = []
    # Convert to BGR
    for i in range(n_faces):
        name = db.lookup(embedding[i].detach().cpu().numpy())
        names.append(name)

    return names


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Check an image for faces.")
    parser.add_argument("--image", type=str, help="Path to the image.")
    args = parser.parse_args()

    image = cv2.imread(args.image)
    names = check_image(image)
    print(names)
