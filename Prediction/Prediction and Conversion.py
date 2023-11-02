import matplotlib.pyplot as plt
import cv2
from ultralytics import YOLO
import fitz
import os
import numpy as np
import easyocr
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
def rename_pdf(path):
    pdf_document = fitz.open(path)
    page = pdf_document[0]
    pix = page.get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72))
    pix.save("temp.png")
    page_image = cv2.imread("temp.png")
    page_image = cv2.cvtColor(page_image, cv2.COLOR_BGR2RGB)
    model = YOLO("runs\detect/train5/weights/best.pt")
    results = model.predict(page_image,  stream=True)
    output = {}
    for r in results:
        for id in range(0, len(r)):
            x, y, x1, y1 = r.boxes.xyxy.cpu().numpy().astype(int)[id]
            output[r.names[r.boxes.cls.cpu().numpy()[id]]
                   ] = page_image[y:y1, x:x1]
    reader = easyocr.Reader(['en'], gpu=True)
    result = reader.readtext(
        output["Register-Number"], allowlist='0123456789', contrast_ths=1, adjust_contrast=0.1)
    plt.title(result[0][1])
    register_number = result[0][1].upper()
    plt.axis("off")
    plt.imshow(output["Register-Number"])
    plt.show()
    result = reader.readtext(output["Subject-Code"],
                             allowlist='0123456789ETMSCcse', contrast_ths=1, adjust_contrast=0.1)
    plt.title(result[0][1].upper())
    subject_code = result[0][1].upper()
    plt.axis("off")
    plt.imshow(output["Subject-Code"])
    plt.show()
    pdf_document.save(f"Output_Folder\{register_number}_{subject_code}.pdf")
  
rename_pdf("Paper_Samples/00015_212222110050-19EE309-CIA2.pdf")
