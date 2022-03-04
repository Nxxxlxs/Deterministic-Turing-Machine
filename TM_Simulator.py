"""
This module is responsible for the simulation of a standard deterministic turing machine that computes numerical functions

For its execution, execute the following command:


		python TM_Simulator.py argument1 argument2


argument1 being the input file with extension .txt that contains the information about the turing machine

argument2 being the output file with extension.txt that will be generated with the tape settings
"""

import sys
from TuringMachine import TuringMachine
from ReadFile import readFile


def main():
	"""
	This is the main module that creates and executes the turing machine
	"""
	
	#Takes the input parameters
	param = sys.argv[1:]
	try:
		#Opens the input file and creates the output file
		myInputFile = open(param[0], 'r')
	except:
		print('\nInput file not found\n')
	else:
		#Creates the output file
		myOutputFile = open(param[1], 'w')
		try:
			#Creates the Turing machine and executes it
			newTuringMachine = readFile(myInputFile)
			newTuringMachine.startComputation(myOutputFile)
		except:
			pass
	
if __name__ == "__main__":
	main()
