
# Training Model 

## YOLOv8 Object Detection Model Training

Welcome to the training model page of our project. In this document, we'll provide you with an overview of the YOLOv8 object detection model, explain the dataset, and guide you through the training process.


## YOLOv8 Overview

YOLOv8 (You Only Look Once version 8) is a state-of-the-art object detection algorithm. It provides real-time and accurate object detection by dividing an image into a grid and making predictions for objects within each grid cell. YOLOv8 is a versatile framework, and in this project, we've trained a custom YOLOv8 model for the specific task of detecting "Register-Number" and "Subject-Code" within exam answer sheets.

## Dataset

Our dataset consists of 1,276 images, with "Register-Number" and "Subject-Code" annotated in YOLOv8 format. The dataset has been pre-processed and augmented to enhance the diversity and quality of the training data. Augmentation techniques include horizontal and vertical flips, rotations, random cropping, brightness adjustments, exposure adjustments, Gaussian blur, and noise.

## Training Process

To train our custom YOLOv8 model, we used the processed dataset and a specific model configuration. Training involved optimizing the model's parameters to accurately detect "Register-Number" and "Subject-Code" in exam answer sheets. We performed training for a specified number of epochs and evaluated the model's performance on validation data.

## Model Configuration

Our YOLOv8 model is configured with specific hyperparameters, architecture details, and object detection settings. The model configuration file and weights are available in this repository.

## Results and Evaluation

After training the model, we conducted an evaluation to assess its performance. We used various metrics to measure the accuracy, precision, recall, and F1-score of our object detection model.

![R_curve](https://github.com/Marinto-Richee/Enhanced-Hand-Written-Register-Number-Recognition-and-Subject-Code-Detection-in-Examination-Document/assets/65499285/a1092e18-9e8f-4056-a40f-a8be5ef5e8e9|width=100)
![PR_curve](https://github.com/Marinto-Richee/Enhanced-Hand-Written-Register-Number-Recognition-and-Subject-Code-Detection-in-Examination-Document/assets/65499285/129bd01c-9efb-4aef-ad7d-9d3e8ab3685a)
![P_curve](https://github.com/Marinto-Richee/Enhanced-Hand-Written-Register-Number-Recognition-and-Subject-Code-Detection-in-Examination-Document/assets/65499285/a1932b70-2ae8-4f4b-9ebb-ba481d033f59)
![F1_curve](https://github.com/Marinto-Richee/Enhanced-Hand-Written-Register-Number-Recognition-and-Subject-Code-Detection-in-Examination-Document/assets/65499285/7edc6081-b63c-4c5e-b807-109b377aa11e)
![val_batch0_pred](https://github.com/Marinto-Richee/Enhanced-Hand-Written-Register-Number-Recognition-and-Subject-Code-Detection-in-Examination-Document/assets/65499285/6217e0cb-9d6e-4df9-b0c2-239ff036f1e6)
![results](https://github.com/Marinto-Richee/Enhanced-Hand-Written-Register-Number-Recognition-and-Subject-Code-Detection-in-Examination-Document/assets/65499285/afda5cfa-184a-41da-bedc-82079a574d4a)



