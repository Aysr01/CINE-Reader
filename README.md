**What is CINE-Reader ?**

CINE-Reader is an ML model developed to extract useful information from Moroccan identity cards with a 94% accuracy. Thanks to this model, filling in forms can be done with one click.

**How does it works ?**

CINE-Reader is a combination of two models, namely a fine-tuned YOLOv8n and an EasyOCR model. Grayscaling and a bilateral filter are applied to the identity card image to facilitate the extraction of personal informations.

**How to run it on your laptop ?**

to run CINE-Reader on your laptop you should do the following steps:

1- Install requirements

`pip install -r requirements.txt`

2- Move to projects folder

`cd ocr_project`

3- Run server

`python manage.py runserver`
