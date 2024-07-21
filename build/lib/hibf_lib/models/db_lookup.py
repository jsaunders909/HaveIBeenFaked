# Class which looks at the database and returns matches.
from recognition_data import RecognitionData
import os
import numpy as np


class DBLookup:
    """
    Class which looks at the database and returns matches.
    """

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.load()

    def load(self) -> list[RecognitionData]:
        """
        Load the database.
        """

        db = []

        for file in os.listdir(self.db_path):
            if file.endswith(".pkl"):
                db.append(RecognitionData.load(os.path.join(self.db_path, file)))

        self.db = db

    def lookup(self, embedding: np.ndarray, threshold: float = 0.65) -> str:
        """
        Look up the embedding in the database.
        """

        matches = {}
        for data in self.db:
            closest_match = 1000

            # Check left, right, and front embeddings
            if data.embedding_left is not None:
                dist = np.linalg.norm(data.embedding_left - embedding)
                if dist < closest_match:
                    closest_match = dist
                if dist < threshold:
                    return data.name

            if data.embedding_right is not None:
                dist = np.linalg.norm(data.embedding_right - embedding)
                if dist < closest_match:
                    closest_match = dist
                if dist < threshold:
                    return data.name

            if data.embedding_front is not None:
                dist = np.linalg.norm(data.embedding_front - embedding)
                if dist < closest_match:
                    closest_match = dist
                if dist < threshold:
                    return data.name

            matches[data.name] = closest_match

        # print(f"Matches: {matches}")
        return f"Unknown (Closest Match: {min(matches, key=matches.get)})"
