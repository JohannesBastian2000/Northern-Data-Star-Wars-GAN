import os
import cv2
import numpy as np
import math


class CleanDataSet:
    def __init__(self):
        self.base_dir = os.path.dirname(__file__)
        prototxt_path = os.path.join(self.base_dir + "/model_data/deploy.prototxt")
        caffemodel_path = os.path.join(self.base_dir + "/model_data/weights.caffemodel")
        self.count = 0
        self.model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

    def clean(self, path: str):
        for file in os.listdir(path):
            file_name, file_extension = os.path.splitext(file)
            if file_extension in [".png", ".jpg"]:
                image_path = path + "/" + file
                image = cv2.imread(image_path)
                (h, w) = image.shape[:2]

                blob = cv2.dnn.blobFromImage(
                    cv2.resize(image, (300, 300)),
                    1.0,
                    (300, 300),
                    (104.0, 177.0, 123.0),
                )
                self.model.setInput(blob)
                detections = self.model.forward()
                max_confidence = 0
                xy_difference = abs(h - w)

                for i in range(0, detections.shape[2]):
                    confidence = detections[0, 0, i, 2]
                    max_confidence = max(max_confidence, confidence)

                if max_confidence < 0.2 or xy_difference > 250:
                    os.remove(image_path)
                    print(file_name)
                    print("XYDifference: ", abs(h - w))
                    print("Max confidence: ", max_confidence)

    def get_average_dimensions(self, path: str) -> (int, int):
        average_height = 0
        average_width = 0
        number_of_images = 0
        for file in os.listdir(path):
            file_name, file_extension = os.path.splitext(file)
            if file_extension in [".png", ".jpg"]:
                image_path = path + "/" + file
                image = cv2.imread(image_path)
                (h, w) = image.shape[:2]
                number_of_images += 1
                average_height += h
                average_width += w
        return (average_height // number_of_images, average_width // number_of_images)

    def resize(self, path: str):
        average_height, average_width = self.get_average_dimensions(path)
        print("Average height: %s, width: %s" % (average_height, average_width))
        count = 0
        for file in os.listdir(path):
            file_name, file_extension = os.path.splitext(file)
            if file_extension in [".png", ".jpg"]:
                image_path = path + "/" + file
                image = cv2.imread(image_path)
                (h, w) = image.shape[:2]
                if h == average_height and w == average_width:
                    continue
                resized_image = cv2.resize(
                    image,
                    (average_width, average_height),
                    interpolation=cv2.INTER_LINEAR,
                )
                norm_img = np.zeros((average_width, average_height))
                norm_img = cv2.normalize(
                    resized_image, norm_img, 0, 255, cv2.NORM_MINMAX
                )
                image_path = "%s/faces/%s" % (self.base_dir, file)
                print("Resize image: ", image_path)
                cv2.imwrite(
                    image_path,
                    norm_img,
                )
                count += 1
        print("Processed %s images" % (count))
        print(
            "Images have been resized to height: %s, width: %s"
            % (average_height, average_width)
        )
