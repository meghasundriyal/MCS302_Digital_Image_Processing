<center><h1>Image Processing In Python</h1></center>

Digital Image Processing deals with analysis and manipulation of 'Digitized Images'. This repository contains programs to show basic image processing tasks. 

<h3>Basic installations : </h3>

* Install Python
* Download and install Pillow for Python 

<h3>Test Image : </h3>
<img src="SampleImages/rose_gray.jpg" width="200"> 

The above gray scale image is used for image processing, color images can also be used. 

<h3>Transformations : </h3>

1. [Add pixel value](add_pixel_value.py) : To every pixel a constant value is added. 
2. [Image Negative](negative_image.py) : Each pixel value of the input image is subtracted from the 255(2^8 - 1) and mapped onto the output image. As a result, darker pixels become light and ligter become dark. 
3. [Log Transformation](log_transformation.py) : The log transformations uses the following equation: 
                         <p align = "center"> new pixel = c ∗log(old pixel +1)</p>
where c is a constant. 
4. [Power Law Transformation](power_law_transformation.py) : The general form of Power law (Gamma) transformation function is :
                         <p align = "center"> new pixel = s = c*power(old pixel, gamma) </p>
where c and gamma are constants. 
