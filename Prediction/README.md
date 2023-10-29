# PDF to Image Processing and Text Extraction

This document explains the Python code for PDF to image processing and text extraction from exam answer sheets. The code uses object detection and text recognition techniques to extract information such as "Register-Number" and "Subject-Code" from images.

## Introduction

This code is part of a project to automate the process of renaming exam answer sheet PDFs by extracting information like register numbers and subject codes from the documents. The code performs the following steps:

1. Initializes a YOLOv8 model for object detection.
2. Selects an image from a specified folder.
3. Detects and extracts "Register-Number" and "Subject-Code" using YOLOv8.
4. Performs text extraction from the detected regions using the EasyOCR engine.
5. Applies denoising and thresholding to the extracted regions.

## Requirements

Before using this code, make sure you have the following requirements in place:

1. Python installed on your system.
2. Necessary Python libraries installed, including OpenCV, Ultralytics YOLO, Pillow (PIL), supervision, numpy, and EasyOCR.

## Code Description

### Initialization and Model Loading

```python
import matplotlib.pyplot as plt
import cv2
from ultralytics import YOLO
from PIL import Image
import supervision as sv
import os
import numpy as np
import easyocr
import os

# Initialize YOLOv8 model
model = YOLO("runs\detect/train5/weights/last.pt")
```

### Image Selection

```python
# Select an image from a specified folder
folder = input("Enter the folder name (Cropped_image, Paper_Samples_Images): ")
# Code for selecting an image based on user input...
```

### Object Detection

```python
# Perform object detection using YOLO
results = model.predict(image, stream=True)
output = {}
# Process YOLO results to obtain bounding boxes and class names...
```

### Text Extraction

```python
# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'], gpu=True)
# Extract text from regions of interest (ROI)...
```


## Usage

1. Ensure you have Python installed on your system.
2. Install the required Python libraries as mentioned in the "Requirements" section.
3. Run the provided code to perform PDF to image conversion, object detection, and text extraction.

## Dependencies

- Python: [Download](https://www.python.org/downloads/)
- OpenCV: Install using `pip install opencv-python`
- Ultralytics YOLO: Install Ultralytics library
- Pillow (PIL): Install using `pip install Pillow`
- supervision
- numpy: Install using `pip install numpy`
- EasyOCR: Install using `pip install easyocr`

Please ensure that you have the necessary dependencies installed before running the code.
