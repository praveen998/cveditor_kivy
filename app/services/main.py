from app.services.pdfconverter import pdf_to_image,jpg_to_png
import os
from app.services.pdfconverter import input_data,pdf_to_image,jpg_to_png,load_image

INPUT_FILE_PATH=None
OUTPUT_PATH=None
IMAGE=None
IMAGE_LIST=None
FRAMES=[]


#file convert to proper format(png)---------------and save to specified folder----------
def file_to_png():
    INPUT_FILE_PATH=input('enter file path:')
    Extension=input_data(INPUT_FILE_PATH)
    if Extension  == '.pdf':
        print('file is pdf')
        pdf_to_image(INPUT_FILE_PATH)

    elif Extension == '.jpg':
        print('file is jpg')
        jpg_to_png(INPUT_FILE_PATH)

    elif Extension == '.png':
        print('file is png')

    else:
        print('please upload pdf,jpg,png file!')

#return total frames-------------------------------------------------
def convert_to_frames():
    OUTPUT_PATH='/home/praveen/Desktop/cveditor_kivy/output'
    FRAMES=load_image(OUTPUT_PATH)
    print(len(FRAMES))


file_to_png()
convert_to_frames()








