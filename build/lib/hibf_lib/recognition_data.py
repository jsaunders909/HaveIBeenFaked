import json
import numpy as np


class RecognitionData:
    """
    Class for storing recognition data.
    """

    # The name of the recognized person.
    name: str

    # The recognized text.
    embedding: np.ndarray

    def __init__(self, name: str):
        self.name = name
        self.embedding_left = None
        self.embedding_right = None
        self.embedding_front = None

    def update_left(self, embedding: np.ndarray):
        """
        Update the left embedding.
        """
        self.embedding_left = embedding

    def update_right(self, embedding: np.ndarray):
        """
        Update the right embedding.
        """
        self.embedding_right = embedding

    def update_front(self, embedding: np.ndarray):
        """
        Update the front embedding.
        """
        self.embedding_front = embedding

    def __str__(self):
        return f"{self.name}"

    def save(self, path: str):
        """
        Save the recognition data to a file.
        """
        if all(
            [
                self.embedding_left is None,
                self.embedding_right is None,
                self.embedding_front is None,
            ]
        ):
            print(f"Warning: No embeddings for {self.name}.")
            return

        elif any(
            [
                self.embedding_left is None,
                self.embedding_right is None,
                self.embedding_front is None,
            ]
        ):
            print(f"Warning: Incomplete embeddings for {self.name}.")

        # Create a dictionary to store the data.
        data = {
            "name": self.name,
            "embedding_left": self.embedding_left.tolist() if self.embedding_left is not None else None,
            "embedding_right": self.embedding_right.tolist() if self.embedding_right is not None else None,
            "embedding_front": self.embedding_front.tolist() if self.embedding_front is not None else None,
        }
        
        json.dump(data, open(path, "w"))

    @classmethod
    def load(cls, path: str):
        """
        Load the recognition data from a file.
        """
        data = json.load(open(path, "r"))

        recognition_data = cls(data["name"])
        recognition_data.embedding_left = np.array(data["embedding_left"]) if data["embedding_left"] is not None else None
        recognition_data.embedding_right = np.array(data["embedding_right"]) if data["embedding_right"] is not None else None
        recognition_data.embedding_front = np.array(data["embedding_front"]) if data["embedding_front"] is not None else None

        return recognition_data
