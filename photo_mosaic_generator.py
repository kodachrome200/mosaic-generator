### Photo Mosaic Generator GUI ###

# This file contains the class for the Photo Mosaic Generator GUI

# Uses tkinter version 8.6

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter import messagebox

from mosaic import MosaicGenerator

class MosaicGUI():
	"""The GUI for the photo mosaic generator."""

	def __init__(self):
		"""Initialize the GUI for the photo mosaic generator."""

		### Get valid file types for images ###
		self.templateTypes = self._initialize_template_file_types()
		self.mosaicTypes = self._initialize_mosaic_file_types()

		### Create root window and set up dimensions ###

		self.root = Tk()
		self.root.title('Photo Mosaic Generator')
		self.root.geometry('800x400')

		### Set up grid for arranging widgets

		# Column configuration
		self.root.grid_columnconfigure(0, weight=1)
		self.root.grid_columnconfigure(1, weight=0)

		### GUI objects for template image ###

		# Template input label
		self.lblTemplate = Label(
				self.root,
				text=f'Select the image file to be used as a template:',
				)
		self.lblTemplate.grid(
				column=0,
				row=0,
				padx=10,
				pady=(20,0),
				sticky='W',
				)

		# Template input text box
		self.txtTemplate = Entry(self.root)
		self.txtTemplate.grid(
				column=0,
				row=1,
				padx=10,
				sticky='WE',
				)

		# Template file dialog button
		self.btnTemplate = Button(
				self.root,
				text='Select',
				width=12,
				command=self._template_file_dialog,
				)
		self.btnTemplate.grid(
				column=1,
				row=1,
				padx=10,
				sticky='E',
				)

		### GUI objects for element image folder ###

		# Elements input label
		self.lblElements = Label(
				self.root,
				text=f'Select a folder for element images of the mosaic:',
				)
		self.lblElements.grid(
				column=0,
				row=2,
				padx=10,
				pady=(20,0),
				sticky='W',
				)

		# Elements input text box
		self.txtElements = Entry(self.root)
		self.txtElements.grid(
				column=0,
				row=3,
				padx=10,
				sticky='WE',
				)

		# Elements folder selector button
		self.btnElements = Button(
				self.root,
				text='Select',
				width=12,
				command=self._elements_folder_dialog,
				)
		self.btnElements.grid(
				column=1,
				row=3,
				padx=10,
				sticky='E',
				)

		### GUI objects for output mosaic image path ###

		# Mosaic input label
		self.lblMosaic = Label(
				self.root,
				text='Select a destination file for the mosaic to be saved:',
				)
		self.lblMosaic.grid(
				column=0,
				row=4,
				padx=10,
				pady=(20,0),
				sticky='W',
				)

		# Mosaic input text box
		self.txtMosaic = Entry(self.root)
		self.txtMosaic.grid(
				column=0,
				row=5,
				padx=10,
				sticky='WE',
				)

		# Mosaic file dialog button
		self.btnMosaic = Button(
				self.root,
				text='Select',
				width=12,
				command=self._mosaic_file_dialog,
				)
		self.btnMosaic.grid(
				column=1,
				row=5,
				padx=10,
				sticky='E',
				)

		### GUI objects for resolution slider

		# Resolution input label
		self.lblResolution = Label(
				self.root,
				text=f'Select a resolution in pixels for sampling the mosaic '
					f'template:')
		self.lblResolution.grid(
				column=0,
				row=6,
				padx=10,
				pady=(20,0),
				sticky='SW',
				)

		# Resolution input scale
		self.sclResolution = Scale(
				self.root,
				from_=1,
				to=100,
				length=200,
				resolution=1,
				orient=HORIZONTAL,
				)
		self.sclResolution.grid(
				column=0,
				row=6,
				padx=10,
				pady=(20,0),
				sticky='E',
				)

		### GUI objects for grid size slider

		# Grid size input label
		self.lblGrid = Label(
				self.root,
				text=f'Select a grid size in pixels for the mosaic element '
					f'images:')
		self.lblGrid.grid(
				column=0,
				row=7,
				padx=10,
				pady=(20,0),
				sticky='SW',
				)

		# Grid size input slider
		self.sclGrid = Scale(
				self.root,
				from_=10,
				to=100,
				length=200,
				resolution=1,
				orient=HORIZONTAL,
				)
		self.sclGrid.grid(
				column=0,
				row=7,
				padx=10,
				pady=(20,0),
				sticky='E',
				)

		### GUI objects for generating mosaic

		# Generate mosaic button
		self.btnGenerate = Button(
				self.root,
				text='Generate',
				width=12,
				command=self._generate_mosaic,
				)
		self.btnGenerate.grid(
				column=1,
				row=8,
				padx=10,
				pady=(20,0),
				sticky='W')


	def run(self):
		# Execute loop for Tkinter GUI
		self.root.mainloop()


	def _initialize_template_file_types(self):
		"""Creates a list of valid file types for selecting the template."""
		
		templateTypes = [
				('All images', '*.bmp *.jpg *.jpeg *.png *.gif'),
				('Bitmap images', '*.bmp'),
				('JPEG images', '*.jpg *.jpeg'),
				('PNG images', '*.png'),
				('GIF images', '*.gif'),
				]

		return templateTypes


	def _initialize_mosaic_file_types(self):
		"""Creates a list of valid file types for the mosaic output."""
		
		mosaicTypes = [
				('Bitmap images', '*.bmp'),
				('JPEG images', '*.jpg *.jpeg'),
				('PNG images', '*.png'),
				('GIF images', '*.gif'),
				]

		return mosaicTypes


	def _template_file_dialog(self):
		"""Opens a tkinter file dialog box and fills the txtTemplate entry with
		the file path if a file is selected."""

		# Open file dialog
		templateFile = askopenfilename(filetypes=self.templateTypes)
		# If file selected, check if txtTemplate already has an entry and clear,
		# then insert path of selected file
		if templateFile:
			curTxt = self.txtTemplate.get()
			if curTxt:
				curTxtEnd = len(curTxt)
				self.txtTemplate.delete(0, curTxtEnd)
			self.txtTemplate.insert(0, templateFile)


	def _elements_folder_dialog(self):
		"""Opens a tkinter askdirectory box and fills the txtElements entry
		with the folder path of the desired mosaic element images."""

		elementsFolder = askdirectory()

		if elementsFolder:
			curTxt = self.txtElements.get()
			if curTxt:
				curTxtEnd = len(curTxt)
				self.txtElements.delete(0,curTxtEnd)
			self.txtElements.insert(0, elementsFolder)



	def _mosaic_file_dialog(self):
		"""Opens a tkinter file dialog box and fills the txtMosaic entry with
		the file path if a file is selected."""

		# Save as dialog
		mosaicFile = asksaveasfilename(filetypes=self.mosaicTypes,
				defaultextension=self.mosaicTypes[0])
		# If file selected, check if txtMosaic already has an entry and clear,
		# then insert path of selected file
		if mosaicFile:
			curTxt = self.txtMosaic.get()
			if curTxt:
				curTxtEnd = len(curTxt)
				self.txtMosaic.delete(0, curTxtEnd)
			self.txtMosaic.insert(0, mosaicFile)


	def _generate_mosaic(self):
		"""Creates an instance of the MosaicGenerator class with the input from
		the user."""

		mg = MosaicGenerator(
			template_path = self.txtTemplate.get(),
			element_path = self.txtElements.get(),
			mosaic_path = self.txtMosaic.get(),
			resolution = self.sclResolution.get(),
			element_size = self.sclGrid.get(),
			)


if __name__ == '__main__':
	mg = MosaicGUI()
	mg.run()