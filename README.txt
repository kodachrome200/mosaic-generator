Photo Mosaic Generator 0.1 for Linux

By Alex Martin, github: kodachrome200

Built using:
Python 3.9.0
Tkinter 8.6
OpenCV 4.2.0
Numpy 1.17.4

***This project is one of my first, and this version is a very preliminary proof-of-concept; there is very little error-checking for image inputs for the template image or element images. I plan to continually update this as time allows***


Basic functionality:

1.	Run in python3 using photo_mosaic_generator.py.

2.	Select a template image for generating the mosaic

3.	Select a folder containing images that will make up the elements of the mosaic

4.	Select an output image destination for saving the mosaic

5.	Select sampling resolution - the number of pixels in the template image that will be
	replaced by a single element image in the mosaic. For example, a resolution of 10 means
	that a 10x10 pixel area of the template image will be replaced by an element image that
	best matches its color and shading.

6.	Select the element image grid size - the size in pixels of an element image in the mosaic.
	For example, a grid size of 50 means that each element in the mosaic will be a 50x50 image.
	The sampling resolution has no bearing on the element image size; you can replace every pixel in the template image with a 100x100 image if you'd like, but the file size may end up being enormous.

7. 	Press the generate button. The completed mosaic image will be saved in the location you
	chose.


Details:

photo_mosaic_generator.py contains the GUI class
mosaic.py contains the class for generating the mosaic image
images.py contains the classes for the template and element images, as well as functions for manipulating these images to generate components of the mosaic.