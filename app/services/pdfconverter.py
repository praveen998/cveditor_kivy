import fitz
import cv2
import numpy as np
import os
from PIL import Image


#load image------------------------------
def load_image(output_path):
    frames=[]
    path=output_path
    try:
        items=os.listdir(path)
        for i in items:
            frames.append(cv2.imread(path+'/'+i))
        return frames
    except Exception as e:
        print(f'error occured:{e}')
        return None



#return file extension -----------------------------------
def input_data(file_path):
    file_name,file_extension=os.path.splitext(file_path)
    #print("file_extension:",file_extension)
    return file_extension



def pixmap_to_image(pixmap):
    img_bytes = pixmap.samples
    image = cv2.imdecode(np.frombuffer(img_bytes, dtype=np.uint8), flags=cv2.IMREAD_COLOR)
    return image


#convert pdf to image-----------------------------------------------------------------------------
def pdf_to_image(pdf_path):
    print(pdf_path)
    output_folder='/home/praveen/Desktop/cveditor_kivy/output'
    pdf_document=fitz.open(pdf_path)

    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)

        pix = page.get_pixmap()
         # Save the image
        image_path = os.path.join(output_folder, f"outputimage_{page_number + 1}.png")
        pix.save(image_path)
       # img = pixmap_to_image(pix)
       # print(type(img))
       # cv2.imwrite(f"{output_folder}/page_{page_number + 1}.jpg",pix)
    pdf_document.close()


#convert jpg to png---------------------------------------------------------------------------------
def jpg_to_png(file_path):
    with Image.open(file_path) as img:
        img.save('/home/praveen/Desktop/cveditor_kivy/output/outputimage.png',"PNG")


#pdf_to_image('Dr.SanthoshKumar_Akkinapalli_CV_6 (1) (3) (2)(1).pdf')

#jpg_to_png('massive-neutron-star.jpg')