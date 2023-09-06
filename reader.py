from ultralytics import YOLO
import easyocr
from image_processing import Processor
import numpy as np
from PIL import Image
import os



class CineReader:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.ocr = easyocr.Reader(lang_list=["fr"], gpu=False)
        self.processor = Processor()

    def get_regions(self, path, degree):
        image = self.processor.load(path)
        try:
            image = image[:,:,:3]
        except:
            pass
        image = self.processor.rotate(image, degree)
        pred1 = self.model(image)
        int_regions = pred1[0].boxes.xyxy
        ls = self.processor.correct(pred1[0].boxes)
        return ls, int_regions, image
    
    def read_text(self, image : np.ndarray, reader, lst) -> str :
        text = reader.readtext(image, allowlist = lst)
        k = len(text)
        conf = text[0][2]
        text = " ".join([text[j][1] for j in range(k)]).upper()
        return text, conf

    def __call__(self, images_path, rot):

        best_conf_cin = []
        degrees = rot.split(",")
        d = {"name": "", "birth_date": "", "cin": "", "adresse": ""}
        classes = {1.0: "name", 2.0:"birth_date", 3.0:"cin", 4.0:"adresse"}

        for img, degree in zip(images_path, degrees) :

            ls, int_regions, image = self.get_regions(img, int(degree))

            for cl , i in ls.items():
                # cut the image and apply effects on it
                cutted_image = self.processor.xy_to_image(int_regions[i], image)
                
                if cl != 0.0 :
                    # cut the image and apply effects on it
                    cutted_image = self.processor.effect(cutted_image)

                    # read text from image
                    if cl == 1.0:
                        im1 , im2 = self.processor.split_image(cutted_image)
                        text1, _ = self.read_text(im1, self.ocr, "ABCDEFGHIJKLMNOPQRSTVUWXYZ -")
                        text2, _ = self.read_text(im2, self.ocr,"ABCDEFGHIJKLMNOPQRSTVUWXYZ -")
                        text = text1 + " " + text2
                    elif cl == 2.0:
                        text, _ = self.read_text(cutted_image, self.ocr, "0123456789.")
                    elif cl == 3.0:
                        text, conf = self.read_text(cutted_image, self.ocr, "ABCDEFGHIJKLMNOPQRSTVUWXYZ0123456789")
                        if best_conf_cin == []:
                            best_conf_cin.append((text, conf))
                        else:
                            if conf > best_conf_cin[0][1]:
                                best_conf_cin[0] = (text, conf)
                            text = best_conf_cin[0][0]
                    else:
                        text, _ = self.read_text(cutted_image, self.ocr,"ABCDEFGHIJKLMNOPQRSTVUWXYZ0123456789 -")
                    d[classes[cl]] = text
                    
                else :
                    pdc = Image.fromarray(cutted_image)
                    pdc.save(r"cine_reader\static\images\pdc.png", dpi=(500,500))

            # remove images
        return d
    


if __name__ == "__main__" :

    ocr = CineReader(r"model\best_lite.pt")
    d, image = ocr([r"C:\Users\ayoub\OneDrive\Bureau\WhatsApp Image 2023-08-09 at 19.11.56.jpg", r"C:\Users\ayoub\OneDrive\Bureau\WhatsApp Image 2023-08-09 at 19.12.02.jpg"],"270,0")
    print(d)
