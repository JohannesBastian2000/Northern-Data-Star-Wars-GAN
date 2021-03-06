import os
import cv2
import numpy as np
import shortuuid
import math


class FaceExtractor:
    def __init__(self):
        if not os.path.exists("faces"):
            print("New directory created")
            os.makedirs("faces")

        self.base_dir = os.path.dirname(__file__)
        prototxt_path = os.path.join(self.base_dir + "/model_data/deploy.prototxt")
        caffemodel_path = os.path.join(self.base_dir + "/model_data/weights.caffemodel")
        self.count = 0
        self.model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

    def extract_face(self, image):
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(
            cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0)
        )
        self.model.setInput(blob)
        detections = self.model.forward()
        # Identify each face
        image_id = shortuuid.uuid()
        for i in range(0, detections.shape[2]):
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                adjusted_box = self.calculate_face_safe_area(box.astype("int"), 20)
                (startX, startY, endX, endY) = adjusted_box
                frame = image[startY:endY, startX:endX]
                image_path = "%s/faces/%s_%s.jpg" % (self.base_dir, i, image_id)
                print("save image at: ", image_path)
                if not np.shape(frame) == ():
                    cv2.imwrite(
                        image_path,
                        frame,
                    )
                self.count += 1
                print("Extracted " + str(self.count) + " faces So far")

    def calculate_face_safe_area(self, box, buffet: int = 20) -> (int, int, int):
        startX, startY, endX, endY = box[0], box[1], box[2], box[3]
        x_length = endX - startX
        y_length = endY - startY
        if x_length < y_length:
            diff = (y_length - x_length) // 2
            startX -= diff
            endX += diff

        elif delta_x > delta_y:
            diff = (x_length - y_length) // 2
            startY -= diff
            endY += diff

        delta_x = int(((endX - startX) / 100) * buffet)
        delta_y = int(((endY - startY) / 100) * buffet)
        return (startX - delta_x, startY - delta_y, endX + delta_x, endY + delta_y)
