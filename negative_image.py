#Compute negative of an image and display it(without using inbuilt function)
from PIL import Image

def negate(pixel):
    return (255-pixel)

def main():
    #open the image 
    img = Image.open("SampleImages/rose_gray.jpg")    
    
    #calculate width and height of the image
    width, height = img.size

    #load the pixel data
    pixels = img.load()
    
    if(img.mode == "RBG"):                  #RGB has 3 channels
        for w in range(width):
            for h in range(height):
                #retrieve the pixel values
                r,g,b = img.getpixel((w,h))
                #negate each pixel 
                pixels[w,h] = (negate(r) , negate(g) , negate(b))

    else:
         for w in range(width):
            for h in range(height):
                #retrieve the pixel value
                p = img.getpixel((w,h))
                
                pixels[w,h] = (negate(p))

    #save altered image        
    img.save("SampleImages/negative_image.jpg")        
  
    
#display the image
def displayImage():
    img = Image.open("SampleImages/negative_image.jpg") 
    img.show()

if __name__ == '__main__':
    main()
    displayImage()

