import fitz
import cv2
import numpy as np
import os
from PIL import Image
from .cvcreator import frame_creator,merge_frames
import shutil

#delete all files-----------------------------------
def delete_all_files(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        raise ValueError(f"The folder {folder_path} does not exist.")
    # Iterate over all files and directories in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            # Check if it is a file and delete it
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            # If it is a directory, remove it and all its contents
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


#load frames---delete output folder content---------
def load_frames(frames,path):
    print('delete file path:',path)
    print('frame list:',len(frames))
    delete_all_files(path)
    mergelist=[]
    
    for i in range(len(frames)):
        print('frame shapes:',frames[i].shape[1])
        out=frame_creator(frames[i].shape[1])
        merge=merge_frames(frames[i],out)
        mergelist.append(merge)
        # path='output_frame'+str(i)+'.png'
        #cv2.imwrite(path,merge)
    
    return mergelist



#load image--from-- output folder--------------------------
def load_image(output_path):
    frames=[]
    path=output_path
    try:
        items=os.listdir(path)
        for i in items:
            frames.append(cv2.imread(path+'\\'+i))
            print(i)
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
    output_folder=os.getcwd()+'\\output'
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
    outpath=os.getcwd()
    with Image.open(file_path) as img:
       # img.save(outpath+'\\output\\outputimage.png',"PNG")
       img.save('outputimage.png',"PNG")


#jpg_to_png('massive-neutron-star.jpg')