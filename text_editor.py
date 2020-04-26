'''

Author: Erik Lagerström
Description: A sample project to create a text editor that allows opening,
			editing and saving text files using python

'''


# Create window
# Add open button to select a text file, add save and quit button

#!/usr/bin/python

import os
import tkinter
from tkinter import *
from tkinter import filedialog

class Editor():

	__root = tkinter.Tk()

	__width = 400
	__height = 400
	__textArea = tkinter.Text(__root)

	# Adding the menu options we want
	__menubar = tkinter.Menu(__root)

	# Adding scroll bar
	__scrollBar = tkinter.Scrollbar(__textArea)
	__file = None

	def __init__(self, **kwargs):

		try:
			self.__width = kwargs['width']
			self.__height = kwargs['height']
		except KeyError:
			pass

		# Initialize the geometry of the window, no care taken to center window
		self.__root.geometry(str(self.__width) + 'x' + str(self.__height))
		self.__root.title("Untitled - Super Editor 1.0")

		self.__root.grid_rowconfigure(0, weight=1)
		self.__root.grid_columnconfigure(0, weight=1)

		#Add controls (widget)
		self.__textArea.grid(sticky=N + E  + S + W)

		self.__filemenu = tkinter.Menu(self.__menubar,tearoff = 0)

		#Add labels and buttons to menus
		self.__filemenu.add_command(label="New", command=self.__newfile)
		self.__filemenu.add_command(label="Save", command=self.__savefile)
		self.__filemenu.add_command(label="Save as...", command=self.__savefileas)
		self.__filemenu.add_command(label="Open", command=self.__openfile)
		self.__menubar.add_cascade(label='File', menu = self.__filemenu)

		self.__editmenu = tkinter.Menu(self.__menubar, tearoff = 0)
		self.__editmenu.add_command(label='Copy', command = self.__copy)
		self.__editmenu.add_command(label='Cut', command = self.__cut)
		self.__editmenu.add_command(label='Paste', command = self.__paste)
		self.__menubar.add_cascade(label='Edit', menu = self.__editmenu)

		self.__menubar.add_command(label="Exit", command=self.__root.quit)
		
		self.__scrollBar.pack(side=RIGHT, fill=Y)
		self.__scrollBar.config(command=self.__textArea.yview)
		self.__textArea.config(yscrollcommand=self.__scrollBar.set)
		self.__root.config(menu=self.__menubar)

	def run(self):
		self.__root.mainloop()

	def __newfile(self):
		self.__root.title("Untitled - Super Editor 1.0")
		self.__textArea.delete(1.0, END)
		self.__file = None

	def __savefile(self):

		# Editing an untitled window
		if self.__file is None:
			self.__file = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension = ".txt",
					filetypes = [("All Files", "*.*"),("Text Files", "*.txt"),("Python FIles", "*.py")])


			#Proceed and try to get the requested file name
			if self.__file == "":
				self.__file = None
			else:
				file = open(self.__file, "w")
				file.write(self.__textArea.get(1.0, END))
				file.close()

				self.__root.title(os.path.basename(self.__root) + ' - Super Editor 1.0')
		
		# Editing a previously existing .txt or whatever
		else:
			file = open(self.__file, "w")
			file.write(self.__textArea.get(1.0, END))
			file.close()

	def __savefileas(self):
		self.__file = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension = ".txt",
					filetypes = [("All Files", "*.*"),("Text Files", "*.txt"),("Python FIles", "*.py")])

			#Proceed and try to get the requested file name
		if self.__file == "":
			self.__file = None
		else:
			file = open(self.__file, "w")
			file.write(self.__textArea.get(1.0, END))
			file.close()

			self.__root.title(os.path.basename(self.__root) + ' - Super Editor 1.0')

	def __openfile(self):
		self.__file = filedialog.askopenfilename(filetypes = [("Text Files", "*.txt"),("Python FIles", "*.py")])
		# No file to open
		if self.__file == "":
			self._file = None
		else:
			# Found valid file, open it and display in in textarea
			self.__root.title(os.path.basename(self.__file) + " - Super Editor 1.0" )
			self.__textArea.delete(1.0, END)

			file = open(self.__file, 'r')
			self.__textArea.insert(1.0, file.read())
			file.close()
			#Concern: might want to keep file open until we save the edited file to avoid data races/version problems
		
	def __copy(self):
		pass

	def __cut(self):
		pass

	def __paste(self):
		pass



# Only want to specifically start the editor if the script is run directly
if __name__ == '__main__':
	Editor = Editor()
	Editor.run()