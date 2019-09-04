#Import a gray scale image and perform pwer law / gamma transformation 
from PIL import Image
import math 
import numpy as np


#function for log transformation
def powerLawTransform(c,pixel,gamma):
    new_pixel = c*pow(pixel,(1/gamma))
    return round(new_pixel)

def main():
    #open the image 
    img = Image.open("SampleImages/rose_gray.jpg")    
    
    #calculate width and height of the image
    width, height = img.size
        
    #load pixel data
    pixels = img.load()  
    
    #The scaling constant c is chosen so that the maximum output value is 255
    c = 255/(math.log10(1+ np.amax(img)))
    gamma = float(input("Enter a value for gamma : "))

    #going to each pixel of the image and adding a value to it
    for w in range(width):
        for h in range(height):
            #retrieve the pixel value
            p = img.getpixel((w,h))
            #add value to the pixel 
            pixels[w,h] = powerLawTransform(c,p,gamma)

    img.save("SampleImages/gamma_transformed.jpg")


#display the image
def displayImage():
    img = Image.open("SampleImages/gamma_transformed.jpg") 
    img.show()

if __name__ == '__main__':
    main()
    displayImage()