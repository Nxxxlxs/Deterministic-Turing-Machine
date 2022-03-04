"""
This module is responsible for reading the input file
"""

from TuringMachine import TuringMachine

def readFile (inputFile):
	"""
	This function reads the lines from a text file, 
	removes pre-defined characters and returns an object 
	of type TuringMachine
	
	:param inputFile: The .txt file to be read
	:return: An object of type TuringMachine
	"""
	
	lines = inputFile.readlines()
	data = []
	functions = []

	try:
		#Manipulating file lines
		for line in lines:
			myLine = line.replace(" ", "")
			myLine = myLine.replace("{", "")
			myLine = myLine.replace("}", "")
			myLine = myLine.replace("(", "")
			myLine = myLine.replace(")", "")
			myLine = myLine.replace("->",",")
			myLine = myLine.rstrip()
			data.append(myLine.rstrip(','))		

		#Taking data about states, symbols and tape
		info = data[1:len(data)-2]

		states = info[0].split(',')
		symbols = info[1].split(',')
		tape = data[len(data)-1]
		tapeSymbols = info[2].split(',')
		
		#Taking data about functions
		info = info[4:len(info)-2]
		
		for line in info:
			myLine = line.split(',')
			functions.append(myLine)
		#Creating the object
		myTuringMachine = TuringMachine(states, symbols, tapeSymbols, functions, tape)
		
		return myTuringMachine
	
	except:
		print('\nCould not read file data correctly \nPlease check that your input file '\
				'meets the requirements described in the README file\n')
	
	
