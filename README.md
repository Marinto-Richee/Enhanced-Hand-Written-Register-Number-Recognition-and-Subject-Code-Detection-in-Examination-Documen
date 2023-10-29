# Enhanced Hand Written Register Number Recognition and Subject Code Detection in Examination Documents

## Overview

This project focuses on automating the extraction of registration numbers from scanned handwritten documents. By leveraging EasyOCR, an Optical Character Recognition (OCR) tool, and implementing various computer vision techniques, we have developed an effective solution for this task.

## Workflow

The project follows a systematic workflow:

### 1. Image Preprocessing

We begin by applying image preprocessing techniques to enhance the quality of input images, making them suitable for effective OCR. Techniques include:
- Grayscale conversion
- Gaussian blur
- Adaptive thresholding
- Morphological operations

Example Preprocessing Code:
```python
# Image Preprocessing Example
import cv2
import numpy as np

# Load the image
image = cv2.imread("input_image.jpg")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Perform adaptive thresholding
_, thresh_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Morphological operations (closing)
kernel = np.ones((3, 3), np.uint8)
morph_image = cv2.morphologyEx(thresh_image, cv2.MORPH_CLOSE, kernel)

# Display the preprocessed image
cv2.imshow("Preprocessed Image", morph_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

### 2. OCR using EasyOCR

EasyOCR is employed to perform OCR on the preprocessed images, accurately extracting text in different languages and styles.

Example OCR Code:
```python
# OCR using EasyOCR
import easyocr

# Load preprocessed image
preprocessed_image = cv2.imread("preprocessed_image.jpg")

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'], gpu=True)

# Perform OCR on the preprocessed image
result = reader.readtext(preprocessed_image)

# Print OCR results
for bbox, text, score in result:
    print("Text:", text)
    print("Confidence:", score)
    print("---")

```

### 3. Text Post-processing

Post OCR, we refine the extracted text to ensure it conforms to the expected format. This involves correcting potential errors and replacing specific characters with their appropriate counterparts.

Example Post-processing Code:
```python
# Text Post-processing Example
import re

def post_process_text(text):
    # Replace specific characters
    text = text.replace("|", "1")
    text = text.replace("/", "1")
    text = text.replace("o", "0")
    
    return text

# Example usage
original_text = "ABC|123/XYZ"
processed_text = post_process_text(original_text)
print("Original Text:", original_text)
print("Processed Text:", processed_text)

```

### 4. Prediction Analysis

We analyze OCR predictions, focusing on the most recurrent and reliable 12-digit predictions, which correspond to the registration numbers we aim to extract.

Example Prediction Analysis Code:
```python
# Prediction Analysis Example
from collections import Counter

# List of predictions
predictions = ["123456789012", "123456789011", "123456789012", "234567890123"]

# Count occurrences of each prediction
prediction_counts = Counter(predictions)

# Most common prediction
most_common_prediction = prediction_counts.most_common(1)[0]

print("Most Common Prediction:", most_common_prediction[0])
print("Count:", most_common_prediction[1])

```

### 5. Flowchart Representation

The entire workflow is visually represented in a comprehensive flowchart, illustrating the logical flow of the process.
![image](https://github.com/Marinto-Richee/Handwritten-Registration-Number-Extraction-Project/assets/65499285/c26b95de-5d0a-4f82-be61-f7490b7ca76d)

## Usage

1. Clone this repository.
2. Install the required dependencies.
3. Execute the provided code using appropriate image paths.

## License

This project is licensed under the [MIT License](LICENSE).
