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

    def __init__(self, name: str, embedding: np.ndarray):
        self.name = name
        self.embedding = embedding

    def __str__(self):
        return f"{self.name}"

    def save(self, path: str):
        """
        Save the recognition data to a file.
        """
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path: str):
        """
        Load the recognition data from a file.
        """
        with open(path, "rb") as f:
            return pickle.load(f)