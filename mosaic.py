import os
from os import path
import numpy as np
from math import ceil
import cv2

from images import TemplateImage, ElementImage

class MosaicGenerator():
	"""This class contains all of the properties and functions for
	generating a mosaic image."""

	def __init__(self, template_path, resolution, element_path, element_size,
		mosaic_path):
		"""
		Initialize an instance of the MosaicGenerator class.

		-Parameters-

		template_path:		path of the template image to be used for generating
							the mosaic

		resolution:			the number of pixels in the template image to be
							represented by an element image of the mosaic.
							Pixel count represents pixels on one side of a square

		element_path:		the folder path for all of the element images to be
							used in the mosaic

		element_size:		the side length of an element image to be used in
							generating the mosaic

		mosaic_path:		the path to save the mosaic image file.
		"""

		self.template_path = template_path
		self.resolution = resolution
		self.element_path = element_path
		self.element_size = element_size
		self.mosaic_path = mosaic_path
		self.ti = TemplateImage(template_path, resolution)
		self.ei = self._get_element_images()

		# TEST
		#for element in self.ei:
			#print(self._compare_rgb_values((255, 125, 0), element.rgb))

		self.mosaic = self._build_mosaic()

		# TEST
		#print(self._get_matching_element(self.ei[6].rgb))

		cv2.imwrite(mosaic_path, self.mosaic)

	def _get_element_images(self):
		"""
		Returns a list of ElementImage objects to be used in generating the
		mosaic.

		element_path:	folder path contianing the element images

		element_size:	the side length of the images for scaling and cropping
		"""

		element_images = []
		image_files = os.listdir(self.element_path)

		for file_name in image_files:
			file_path = self.element_path + '/' + file_name
			element_images.append(ElementImage(file_path, self.element_size))

		return element_images


	def _build_mosaic(self):
		"""
		The main function for building the mosaic.
		"""

		# Get template image and dimensions
		temp = self.ti.template
		temp_x = self.ti.template_width
		temp_y = self.ti.template_height

		# Get mosaic dimensions and declare empty array for RGB values
		mos_x = ceil(self.ti.width / self.resolution) * self.element_size
		mos_y = ceil(self.ti.height / self.resolution) * self.element_size
		mos = np.empty(shape=(mos_y, mos_x, 3), dtype='uint8')

		# Get elements and size of elements
		ei = self.ei
		elm_x = elm_y = self.element_size

		y = 0
		while y < temp_y:
			y_start = elm_y * y
			y_end = elm_y * (y + 1)
			x = 0
			while x < temp_x:
				x_start = elm_x * x
				x_end = elm_x * (x + 1)
				elm_i = self._get_matching_element(temp[y,x])
				elm = ei[elm_i].image
				mos[y_start : y_end, x_start : x_end] = elm
				x += 1

			y += 1

		return mos

	def _get_matching_element(self, rgb):
		"""
		Returns the index of an element image in self.ei that most closely
		matches the rgb value provided.

		rgb:		a tuple of integers representing RGB values of a pixel.
		"""

		# Build a list that contains all of the 'distances' of the image RGB
		# values to the input RGB value.
		distances = []
		for image in self.ei:
			distances.append(self._compare_rgb_values(rgb, image.rgb))

		# Return the index of the element image with the shortest distance
		return distances.index(min(distances))


	def _compare_rgb_values(self, rgb_1, rgb_2):
		"""
		Uses linear algebra to check the 'closeness' of one set of RGB values
		to another. Considers the RGB values as points in 3-space and returns 
		the magnitude of the vector between them as a float.

		rgb_1, rgb_2: 	tuples containing integers for the RGB values
						ex. (R, G, B) = (156, 136, 125)
		"""

		# Get 'distances' between red, green, and blue values of each set
		diff_r = rgb_1[0] - rgb_2[0]
		diff_g = rgb_1[1] - rgb_2[1]
		diff_b = rgb_1[2] - rgb_2[2]

		# Use Pythagorean theorem to return the distance between rgb_1 and rgb_2
		return (diff_r**2 + diff_g**2 + diff_b**2)**0.5

