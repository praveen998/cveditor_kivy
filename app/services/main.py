import os
from .pdfconverter import input_data,pdf_to_image,jpg_to_png,load_image,load_frames
from .cvcreator import convert_frame_to_pdf
import cv2

INPUT_FILE_PATH=None
OUTPUT_PATH=None
IMAGE=None
IMAGE_LIST=None
FRAMES=[]
FILE_TYPE=None


#file convert to proper format(png)---------------and save to specified folder--------
def file_to_png(path):
    #INPUT_FILE_PATH=input('enter file path:')
    INPUT_FILE_PATH=path
    #get file extension ('.pdf')
    Extension=input_data(INPUT_FILE_PATH)

    if Extension  == '.pdf':
        print('file is pdf')
        pdf_to_image(INPUT_FILE_PATH)

    elif Extension == '.jpg':
        print('file is jpg')
        jpg_to_png(INPUT_FILE_PATH)

    elif Extension == '.png':
        print('file is png')
        jpg_to_png(INPUT_FILE_PATH)

    else:
        print('please upload pdf,jpg,png file!')
    return Extension


#return total frames--------------------------------------------------------------------


def convert_to_frames(TYPE):
    OUTPUT_PATH=os.getcwd()+'\\output'
   # D:\Nibhas\cveditor_kivy\output
    FRAMES=load_image(OUTPUT_PATH)
    mergelist=load_frames(FRAMES,OUTPUT_PATH)

    if TYPE == '.pdf':
        print('type is :',TYPE)
        print('length of merge list:',len(mergelist))
        convert_frame_to_pdf(mergelist)
    else:
        print('type is :',TYPE)

        for i in mergelist:
            cv2.imwrite(os.getcwd()+'\\RESUME\\output.png',i)


#type=file_to_png('..\\..\\massive-neutron-star.jpg')
#convert_to_frames(type)








