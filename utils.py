import cv2

def draw_bbox(image, bbox, color=(0, 255, 0), thickness=2):
    """ Draw bounding box on image """
    for x1, y1, x2, y2 in bbox:
        cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
    return image


def draw_text(image, text, position, color=(0, 255, 0), thickness=2, font_scale=1):
    """ Draw text on image """
    cv2.putText(image, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)
    return image

def draw_labelled_bbox(image, bbox, label, color=(0, 255, 0), thickness=4):
    """ Draw labelled bounding box on image """
    bbox = bbox.astype(int)
    x1, y1, x2, y2 = bbox[0], bbox[1], bbox[2], bbox[3]
    image = cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
    image = cv2.putText(image, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return image