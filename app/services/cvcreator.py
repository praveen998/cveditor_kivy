import cv2
import numpy as np

# Create a black image (500x500 pixels with 3 color channels (BGR))
image = np.ones((2300,1600, 3), dtype=np.uint8) * 255


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
