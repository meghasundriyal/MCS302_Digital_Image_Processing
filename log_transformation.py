# Import a gray scale image and perform log transformation

from PIL import Image
import math 
import numpy as np


#function for log transformation
def logTransform(c,pixel):
    new_pixel = c*math.log10(float(pixel+1))
    return round(new_pixel)
                    
def main():
    #open the image 
    img = Image.open("SampleImages/rose_gray.jpg")    
    
    #calculate width and height of the image
    width, height = img.size
        
    #load pixel data
    pixels = img.load()  
    
    #The scaling constant c is chosen so that the maximum output value is 255
    c  = 255/(math.log10(1+ np.amax(img)))

    #going to each pixel of the image and adding a value to it
    for w in range(width):
        for h in range(height):
            #retrieve the pixel value
            p = img.getpixel((w,h))
            #log tranform each pixel 
            pixels[w,h] = (logTransform(c,p))

    #save altered image        
    img.save("SampleImages/log_transformed.jpg")        

#display the image
def displayImage():
    img = Image.open("SampleImages/log_transformed.jpg") 
    img.show()

if __name__ == '__main__':
    main()
    displayImage()
