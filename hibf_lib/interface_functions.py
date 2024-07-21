from hibf_lib.recognition_data import RecognitionData
from hibf_lib.models.db_lookup import DBLookup
from hibf_lib.models.face_recognition import FRTorch


def add_left_image(uid, image, name, database_root="face_db"):
    """
    Add a left image to the database.

    Args:
        uid (str): Unique identifier for the person.
        image (np.ndarray): Image of the person.
        name (str): Name of the person.
        database_root (str): Path to the database.
    Returns:
        bool: True if the image was added to the database, False otherwise.
    """
    model = FRTorch()

    data_path = os.path.join(database_root, f"{uid}.json")

    if os.path.exists(data_path):
        recognition_data = RecognitionData.load(data_path)
        if recognition_data.name != name:
            print(
                f"Name mismatch, entry with uid {uid} already exists with name {recognition_data.name} but you have passed {name}."
            )
            return False
    else:
        recognition_data = RecognitionData(name)

    embedding, crop, bbox = model(image, return_crop=True, return_bbox=True)

    if embedding is None:
        print("No face detected.")
        return False

    embedding = embedding[0].detach().cpu().numpy()
    recognition_data.update_left(embedding)

    recognition_data.save(data_path)
    print("Face data saved.")

    return True


def add_right_image(uid, image, name, database_root="face_db"):
    """
    Add a left image to the database.

    Args:
        uid (str): Unique identifier for the person.
        image (np.ndarray): Image of the person.
        name (str): Name of the person.
        database_root (str): Path to the database.
    Returns:
        bool: True if the image was added to the database, False otherwise.
    """
    model = FRTorch()

    data_path = os.path.join(database_root, f"{uid}.json")

    if os.path.exists(data_path):
        recognition_data = RecognitionData.load(data_path)
        if recognition_data.name != name:
            print(
                f"Name mismatch, entry with uid {uid} already exists with name {recognition_data.name} but you have passed {name}."
            )
            return False
    else:
        recognition_data = RecognitionData(name)

    embedding, crop, bbox = model(image, return_crop=True, return_bbox=True)

    if embedding is None:
        print("No face detected.")
        return False

    embedding = embedding[0].detach().cpu().numpy()
    recognition_data.update_right(embedding)

    recognition_data.save(data_path)
    print("Face data saved.")

    return True


def add_front_image(uid, image, name, database_root="face_db"):
    """
    Add a left image to the database.

    Args:
        uid (str): Unique identifier for the person.
        image (np.ndarray): Image of the person.
        name (str): Name of the person.
        database_root (str): Path to the database.
    Returns:
        bool: True if the image was added to the database, False otherwise.
    """
    model = FRTorch()

    data_path = os.path.join(database_root, f"{uid}.json")

    if os.path.exists(data_path):
        recognition_data = RecognitionData.load(data_path)
        if recognition_data.name != name:
            print(
                f"Name mismatch, entry with uid {uid} already exists with name {recognition_data.name} but you have passed {name}."
            )
            return False
    else:
        recognition_data = RecognitionData(name)

    embedding, crop, bbox = model(image, return_crop=True, return_bbox=True)

    if embedding is None:
        print("No face detected.")
        return False

    embedding = embedding[0].detach().cpu().numpy()
    recognition_data.update_front(embedding)

    recognition_data.save(data_path)
    print("Face data saved.")

    return True


def get_match_from_db(embedding, threshold=0.65, database_root="face_db"):
    """
    Get the match from the database.

    Args:
        embedding (np.ndarray): Embedding to match.
        threshold (float): Threshold for matching.
        database_root (str): Path to the database.
    Returns:
        str: Name of the person if found, None otherwise.
    """
    db_lookup = DBLookup(database_root)
    return db_lookup(embedding, threshold)


def check_image(image, database_root="face_db"):
    """
    Check an image for faces.

    Args:
        image (np.ndarray): Image to check.
        database_root (str): Path to the database.
    Returns:
        list[str]: Names of the people in the image.
    """
    model = FRTorch()
    db = DBLookup(database_root)
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
    import os, sys
    import cv2

    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

    real_trump = "sample_images/Trump.jpg"
    real_biden = "sample_images/Biden.jpg"
    biden_on_trump = "sample_images/Biden_face_on_Trump.jpg"
    trump_on_biden = "sample_images/Trump_face_on_Biden.jpg"

    # Add Trump to the database
    trump = cv2.imread(real_trump)
    add_front_image("trump", trump, "Trump")

    # Add Biden to the database
    biden = cv2.imread(real_biden)
    add_front_image("biden", biden, "Biden")

    # Check Trump
    trump_pred = check_image(trump)
    print("Predicted Trump as", trump_pred)

    # Check Biden
    biden_pred = check_image(biden)
    print("Predicted Biden as", biden_pred)

    # Check Biden on Trump
    biden_on_trump = cv2.imread(biden_on_trump)
    biden_on_trump_pred = check_image(biden_on_trump)
    print("Predicted Biden on Trump as", biden_on_trump_pred)

    # Check Trump on Biden
    trump_on_biden = cv2.imread(trump_on_biden)
    trump_on_biden_pred = check_image(trump_on_biden)
    print("Predicted Trump on Biden as", trump_on_biden_pred)
