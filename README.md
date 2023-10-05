## 1. What is CINE-Reader ?

CINE-Reader is an ML model developed to extract useful information from Moroccan identity cards with a 94% accuracy. Thanks to this model, filling in forms can be done with one click.

## 2. How does it works ?

CINE-Reader is a combination of two models, namely a fine-tuned YOLOv8n and an EasyOCR model. Grayscaling and a bilateral filter are applied to the identity card image to facilitate the extraction of personal informations.

## 3. How to run project

To run CINE-Reader on your laptop you should do the following steps:

### 3.1. Install Requirements

`pip install -r requirements.txt`

### 3.2. Move To Projects Folder

`cd ocr_project`

### 3.3. Run Server

`python manage.py runserver`

## 4. Pipline

### 4.1. Detecting The Regions Of Interest

<img src="https://github.com/Aysr01/CINE-Reader/assets/114707989/d574e294-7f76-46ab-900d-0534143db23b">

### 4.2. Image Processing

After detecting and cropping the regions of interest, a bilateral filter and grayscale transformation will be applied to the cropped images in order to reduce noise and enhance the images' features. This preprocessing step is essential for facilitating the text extraction process by improving the image quality and simplifying the color information.

### 4.3. Text Recognition

The output of the program is as follows:

`{
"first name": "ZAINEB",
"last name": "EL ALAMI",
"birth date": "05/12/1983",
"CIN": "U1234567"
}`
