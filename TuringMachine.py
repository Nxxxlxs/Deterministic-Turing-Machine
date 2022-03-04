"""
This module is responsible for representing the Turing machine
"""

class TuringMachine:
	
	"""
	
	This class is a representation of a Turing machine as a 5 tuple.

		Q = set of states (default q [0 - 9] +)
		Σ = input alphabet ({1} for unary representation of numeric arguments)
		Γ = tape alphabet ({1, B} the white symbol will separate the arguments numbers on tape)
		δ = format transition function (qi, x) -> (qj, y, D) so, being in the state qi, reading x, goes to state q, writes y and moves in the direction of D,
			D will be L to the left or R to the right.
		q0 = initial state
	"""
		
	def __init__(self, aStates, aSymbols, aTapeSymbols, aFunctions, aTape):
		"""
		
		Class constructor
		
		:param aStates: set of states
		:param aSymbols: input alphabet
		:param aTapeSymbols: tape alphabet
		:param aFunctions: transition functions
		:param aTape: input tape
		
		:return: 
		"""
		self.__states = aStates
		self.__symbols = aSymbols
		self.__tapeSymbols = aTapeSymbols
		self.__functions = aFunctions
		self.__tape = aTape
	
	#Returns the set of states
	def getStates(self):
		"""
		
		Get the set of states
		
		:return: list
		"""
		return self.__states
	
	#Returns the input alphabet
	def getSymbols(self):
		"""
		
		Get the input alphabet
		
		:return: list
		"""
		return self.__symbols
	
	def getTapeSymbols(self):
		"""
		
		Get the tape alphabet
		
		:return: list
		"""
		return self.__tapeSymbols
		
	def getFunctions(self):
		"""
		
		Get the transition functions
		
		:return: list
		"""
		return self.__functions
		
	def getTape(self):
		"""
		
		Get the input tape
		
		:return: list
		"""
		return self.__tape
		
	def startComputation(self, outputFile):
		"""
		
		This method performs the transition functions of the Turing Machine and writes the tape settings to the parameter file.
		
		:param outputFile: The .txt file to be saved
		
		:return:
		"""
		copyTape = self.getTape()
		copyFunctions = self.getFunctions()
		currentState = 'q0'
		pos = 0
		finalTape = '{' + currentState + '}' + copyTape
		transition = True
		
		while transition == True:
			outputFile.write(finalTape+'\n')
			transition = False
			
			for func in copyFunctions:
				state = func[0]
				reading = func[1]
				direction = func[4]
				newChar = func[3]
				
				if state == currentState and reading == copyTape[pos]:
					currentState = func[2]
					transition = True
					
					
					if direction == 'R': #move right
						
						if pos == 0: #first position
							copyTape = newChar + copyTape[pos+1:]
							finalTape = newChar + '{' + currentState + '}' + copyTape[pos+1:]
							
						elif pos == len(copyTape)-1: #last position
							copyTape = copyTape[:pos] + newChar
							finalTape = copyTape[:pos-1] + '{' + currentState + '}' + newChar + copyTape[pos]
							
						else: #any other position
							copyTape = copyTape[:pos] + newChar + copyTape[pos+1:]
							finalTape = copyTape[:pos] + newChar + '{' + currentState + '}' + copyTape[pos+1:]
						pos+= 1
						
					else: #move left
						
						if pos == 1: #second position
							copyTape = copyTape[pos-1] + newChar + copyTape[pos+1:]
							finalTape = '{'+currentState+'}' + copyTape[pos-1:]
							
						elif pos == len(copyTape)-1: #last position
							copyTape = copyTape[:pos] + newChar
							finalTape = copyTape[:pos-1] + '{' + currentState + '}' + copyTape[pos-1] + newChar
							
						else: #any other position
							copyTape = copyTape[:pos] + newChar + copyTape[pos+1:]
							finalTape = copyTape[:pos-1] + '{' + currentState + '}' + copyTape[pos-1] + newChar + copyTape[pos+1:]
						pos-= 1
											
					break

	
	

