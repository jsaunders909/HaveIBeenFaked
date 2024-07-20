from facenet_pytorch import MTCNN, InceptionResnetV1
import cv2
import torch


class FRTorch:
    def __init__(self):
        # Create a face detection pipeline using MTCNN
        self.mtcnn = MTCNN(
            image_size=160,
            thresholds=[0.6, 0.7, 0.7],
            factor=0.709,
            post_process=True,
            margin=0,
            keep_all=True
        )

        # Create an inception resnet (in eval mode):
        self.resnet = InceptionResnetV1(pretrained="vggface2").eval()

    def __call__(self, image_cv, return_crop=False, return_bbox=False):
        """Get face embedding from image"""

        # Get cropped and prewhitened image tensor
        faces = self.mtcnn(image_cv)

        # If no face is detected, return None
        if faces is None:
            ret = [None]
            if return_crop:
                ret.append(None)
            if return_bbox:
                ret.append(None)
            return ret

        # Calculate embedding
        img_embeddings = self.resnet(faces)

        ret = [img_embeddings]

        if return_crop:
            ret.append(faces.permute(0, 2, 3, 1).detach().cpu().numpy())

        if return_bbox:
            ret.append(self.mtcnn.detect(image_cv)[0])

        return ret
