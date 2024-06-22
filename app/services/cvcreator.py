import cv2
import numpy as np
from PIL import Image
import os

def convert_frame_to_pdf(frames):
    framelist=[]
    print("converting frames to pdf----------------------------------------")
    print('framelist:',len(frames))
    # Convert numpy arrays to PIL Images
    for i in range(len(frames)):
       pil = cv2.cvtColor(frames[i], cv2.COLOR_BGR2RGB)
       pil=Image.fromarray(pil)
       #pil=pil.convert('RGB')
       framelist.append(pil)

    # Convert images to RGB (required for PDF conversion)
    #pil_image = pil_image1.convert('RGB')
    # Save images as a single PDF
    #print('image type:',type(pil_image1))

    pdf_path = os.getcwd()+'\\RESUME\\output.pdf'
    #pdf_path = 'RESUME\\output.pdf'

    f=framelist.pop(0)
    f.save(pdf_path, save_all=True, append_images=framelist)


def frame_creator(width):
    image = np.ones((220,width,3), dtype=np.uint8) * 255
    return image


def merge_frames(frames,out):
    if frames.shape[1] != out.shape[1]:
       raise ValueError("The width of image1 and image2 must be the same.")
    # Merge image1 on top of image2
    newframe=np.ones((frames.shape[0]+out.shape[0],out.shape[1], 3), dtype=np.uint8) * 255
    x=0
    y=0
    out=logo_overlap(out)
    newframe[y:y+out.shape[0],x:x+out.shape[1]]=out
    y=y+out.shape[0]
    newframe[y:y+frames.shape[0],x:x+frames.shape[1]]=frames
   # merged_image = frames.copy()
    #merged_image[:out.shape[0], :out.shape[1]] = out
    return newframe


def logo_overlap(out):
    path=os.getcwd()+'\\app\\assests\\images\\logo2.png'
    #path='logo2.png'
    logo = cv2.imread(path)
    logo = cv2.resize(logo,(200,200))
    x=20
    y=10
    out[y:y+logo.shape[0],x:x+logo.shape[1]]=logo
    text3="Contact:"
    text1 = "Phone: +91 9400783256"
    text2 = "Phone: +91 8590605292"
    email="Email: cv.nibhashrdsolutions@gmail.com"
    website="Website: www.nibhashr.com"
    position = (x,y)


    # Define the font, font scale, and color
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    color = (138,83,7)  # Black color in BGR

    # Define the thickness of the text
    thickness = 1
    cv2.putText(out, text3, (x+220,y+40), font, font_scale, color, thickness, cv2.LINE_AA)
    cv2.putText(out, text1, (x+230,y+65), font, font_scale, color, thickness, cv2.LINE_AA)
    cv2.putText(out, text2, (x+230,y+90), font, font_scale, color, thickness, cv2.LINE_AA)
    cv2.putText(out, email, (x+230,y+115), font, font_scale, color, thickness, cv2.LINE_AA)
    cv2.putText(out, website, (x+230,y+140), font, font_scale, color, thickness, cv2.LINE_AA)
    return out
# Create a black image (500x500 pixels with 3 color channels (BGR))
image = np.ones((2300,1600, 3), dtype=np.uint8) * 255


'''
# Draw a rectangle from (100, 100) to (400,400) BGR
cv2.rectangle(image, (0,0), (600, 2300),(241,247,176), -1) 


# Load the second image
second_image = cv2.imread('logo.png')
second_image = cv2.resize(second_image,(200,200))
x=10
y=10
image[y:y+second_image.shape[0],x:x+second_image.shape[1]]=second_image
cv2.imwrite('output_image.png', image)

#cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
