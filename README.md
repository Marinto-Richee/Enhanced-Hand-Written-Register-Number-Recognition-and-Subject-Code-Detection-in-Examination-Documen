# Enhanced Hand Written Register Number Recognition and Subject Code Detection in Examination Documents

Automating the process of renaming exam answer sheet PDFs by extracting information like register numbers and subject codes from the documents.


## About

Automated Exam Answer Sheet PDF Renamer is a project designed to streamline the process of renaming exam answer sheet PDFs. The traditional manual renaming process is time-consuming and error-prone. This project automates the task by extracting critical information such as student register numbers and subject codes from the answer sheets.

## Features

- Automated exam answer sheet PDF renaming.
- Utilizes YOLOv8 object detection for precise extraction of "Register-Number" and "Subject-Code."
- Employs EasyOCR for accurate text extraction.
- Implements extensive data augmentation techniques to enhance model performance.

## Project Flow
![image](https://github.com/Marinto-Richee/Enhanced-Hand-Written-Register-Number-Recognition-and-Subject-Code-Detection-in-Examination-Document/assets/65499285/1f0d0790-8bb7-44c2-a699-6531989ea669)

## What are we doing in this project?
- We are trying to implement an alternate model and OCR strategy to convert the detected the Register Numbers and Subject Codes to texts.
- We are trying to create a dataset for the above task.
- We are trying to implement a model to detect the Register Numbers and Subject Codes from the front page of the answer sheet.
- Once the detection is done, we are trying to extract the detected Register Numbers and Subject Codes to text.
- To achieve this, we need build an AI model to extract the text from the detected bounding boxes (Register Number and Subject Code).
- We are exploring mulitple OCR strategies and AI models to achieve this task.

## Building the Dataset for OCR
- You can contribute to the dataset building process by helping us to label the data.
- The data is available in the following link: [Dataset](https://drive.google.com/drive/folders/1fD8st-EmKq2WK7Ip04sHmJANMDH-RPgK?usp=sharing)
- You will have to rename each image with the corresponding text in the image.
- Create 3 folders: "Annotated", "Wrong Predictions" and "Upside Down".
    * **Annotated** - Move the images to this folder if you are able to determine the text in the image and have successfully renamed the file.
    * **Wrong Predictions** - Move the images to this folder if the text in the image is not an Register Number, or if you are unable to determine the text in the image.
    * **Upside Down** - Move the images to this folder if the image is upside down.
- Move the images to the respective folders based on the image.

## License
This project is licensed under the [MIT License](LICENSE).
