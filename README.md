## 1. What is CINE-Reader ?

CINE-Reader is an ML model developed to extract useful information from Moroccan identity cards, both new and old versions, with a 94% accuracy rate. Thanks to this model, filling out forms can be accomplished with just one click.

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
The process of extracting personal information from the identity card goes through several steps.
### 4.1. Detecting The Regions Of Interest

<img src="https://github.com/Aysr01/CINE-Reader/assets/114707989/fd2d099c-c63c-4f52-96da-9122d2a36a94" alt="identity card image" width="800">

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

## Web Application
To enhance the usability of our model, we developed a straightforward web application using Django, vanilla CSS, and vanilla JavaScript to facilitate this process. The web app consists primarily of two pages. The first page is dedicated to Identity Card deployment, while the second page displays the extracted data alongside the personal picture. Additionally, users have the ability to edit their information in case of inaccuracies.

<img src="https://github.com/Aysr01/CINE-Reader/assets/114707989/c2ed4511-2931-4607-a8ca-bb540b14ea71" alt="web app main page" width="600">

<img src="https://github.com/Aysr01/CINE-Reader/assets/114707989/30e6edd6-877a-4e42-9d2d-32c18e1ccf29" alt="cards uploaded" width="600">

<img src="https://github.com/Aysr01/CINE-Reader/assets/114707989/d7745879-2f92-40b2-8fd9-5c7094a33a15" alt="results page" width="600">
