import pickle
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
            cont = input("Do you want to svae the partial embedding? (y/n) ")
            if cont.lower() != "y":
                return

        with open(path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path: str):
        """
        Load the recognition data from a file.
        """
        with open(path, "rb") as f:
            return pickle.load(f)
