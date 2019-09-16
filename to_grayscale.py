from PIL import Image
import numpy as np
location="SampleImages/"
name='dark_gray.png'
# name='rose_gray.jpg'
# new_name='dark_gray.png'
# img = Image.open(location+name).convert('LA')
# img.save(location+new_name)
img=Image.open(location+name)
width , height =img.size
pixels=img.load()
linear=[]
for w in range(width):
    for h in range(height):
        p=img.getpixel((w,h))
        linear+=[p[0]]

linear_np=np.array(linear)
# print(linear)
mat=np.reshape(linear_np,(width,height))    
print(mat)
img = Image.fromarray( mat , 'L')
img.save(location+'test.png')
    
        
