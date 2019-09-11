from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_equalization_map(total_pixels,frequency_distribution,l):
    cumulative=[0]*l
    cumulative[0]=frequency_distribution[0]
    for i in range(1,l):
        cumulative[i]=frequency_distribution[i]+cumulative[i-1]
    equalization_map=[0]*l
    for i in range(l):
        equalization_map[i]=int(cumulative[i]*(l-1)/total_pixels)



    # for i in range(len(equalization_map)):
    #     print(i," - ",frequency_distribution[i]," - ",cumulative[i]," - ",equalization_map[i],"\n")
    
    return equalization_map

def equalize(equalization_map,img_matrix,img_linear,frequency_distribution,l) : 
    total_pixels=len(img_linear)
    width=len(img_matrix)
    height=len(img_matrix[0]) 
    new_img_matrix=[[0]*height]*width
    new_img_linear=[0]*total_pixels
    new_frequency_distribution=[0]*l
    for i in range(l):
        new_frequency_distribution[equalization_map[i]]=frequency_distribution[i]
        
    for i in range(total_pixels):
        new_img_linear[i]=equalization_map[img_linear[i]]
    
    for w in range(width):
        
        for h in range(height):
            new_img_matrix[w][h]=[equalization_map[img_matrix[w][h]]]
       

    return new_img_matrix,img_linear,new_frequency_distribution

    



def plot_histogram(linear,name):
    plt.hist( linear, bins=20)
    plt.ylabel('No of times')
    fig = plt.gcf()
    # plt.show()
    fig.savefig(name)
    
def plot_bar(distribution,name):
    index = np.arange(0,256)
    plt.bar(index, distribution )
    plt.xlabel('Intensity Level')
    plt.ylabel('Frequency')
    fig = plt.gcf()
    plt.show()
    fig.savefig(name)
    

def get_image_matrix(name,l):
    img=Image.open(name)
    width , height =img.size
    pixels=img.load()
    total_pixels=width*height
    linear=list(img.getdata())
    img_matrix=[]
    for w in range(width):
        temp_array=[]
        for h in range(height):
            p=img.getpixel((w,h))
            temp_array+=[p]
        img_matrix+=[temp_array]
    return linear , img_matrix
            
def get_frequency_distribution(img_linear,l):
    distribution=[0]*l
    for pixel in img_linear:
        distribution[pixel]+=1
    return distribution

def create_image(equalization_map,name,final_name):
    img = Image.open(name)
    width, height = img.size
    pixels = img.load()
    for w in range(width):
        for h in range(height):
            #retrieve the pixel value
            p = img.getpixel((w,h))
            
            pixels[w,h] = (equalization_map[p])
    img.save(final_name)

def main():
    location="SampleImages/"
    name="rose_gray.jpg"
    l=256
    
    img_linear, img_matrix = get_image_matrix(location+name,l)
    
    total_pixels=len(img_linear)
    print("total pixels",total_pixels,"\n")

    frequency_distribution=get_frequency_distribution(img_linear,l)
    
    equalization_map=get_equalization_map(total_pixels,frequency_distribution,l)

    

    new_img_matrix,img_linear,new_frequency_distribution = equalize(equalization_map ,img_matrix,img_linear,frequency_distribution,l)

    before_plt=plot_bar(frequency_distribution,name+"_before_equalization.png")
    after_plt=plot_bar(new_frequency_distribution,name+"_after_equalization.png")
    create_image(equalization_map,location+name,location+"new_"+name)
   
            
            
            
    
    


if __name__ == '__main__':
    main()
    