# Import an image and display it after adding a value to all its pixels

from PIL import Image

#function to add pixel value
def addPixel(pixel,value):
    return (pixel+value)%255

def main():
    #open the image 
    img = Image.open("SampleImages/rose_gray.jpg")    
    
    #calculate width and height of the image
    width, height = img.size
        
    #load pixel data
    pixels = img.load()
    
    #value to be added to each pixel
    value = 155  

    #going to each pixel of the image and adding a value to it
    if(img.mode == "RBG"):                  #RGB has 3 channels
        for w in range(width):
            for h in range(height):
                #retrieve the pixel values
                r,g,b = img.getpixel((w,h))
                #add value to each pixel 
                pixels[w,h] = (addPixel(r,value) , addPixel(g,value) , addPixel(b,value))

    else:
        for w in range(width):
            for h in range(height):
                #retrieve the pixel value
                p = img.getpixel((w,h))
                #add value to the pixel 
                pixels[w,h] = (addPixel(p,value))

    #save altered image        
    img.save("SampleImages/add_pixel.jpg")        

    
#display the image
def displayImage():
    img = Image.open("SampleImages/add_pixel.jpg") 
    img.show()

if __name__ == '__main__':
    main()
    displayImage()
