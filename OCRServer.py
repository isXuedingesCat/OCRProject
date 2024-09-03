import numpy as np
import cv2
from ocrcore.infer.predict_system import TextSystem
from ocrcore.infer.infer_config import OCR_CONFIG


class Dict2Obj():
    def __init__(self, args):
        self.__dict__.update(args)


if __name__ == "__main__":
    image = cv2.imread("/home/shijia/pycode/OCRProject/test/OIP-C.jpg")

    args_obj = Dict2Obj(OCR_CONFIG)

    result = TextSystem(args_obj)(image)

    print(result)

    pass

