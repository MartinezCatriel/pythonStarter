import unittest

class TestCass:
	a = 0
	def __init__(self):
		a = 82
	@classmethod
	#como si fuera estatico pero recibe a su propia clase(tipo), NO una instancia de su clase
	def pito(self):
		a = a - 1 
		palabra = "blabla" #un string es a su vez un array de caracteres
		letra = palabra[0] #letra = b
		return a
	@staticmethod
	def pito2():
		a = a - 2
		return a
	
class TestSQL:
	def pito():
		a = 1 
		
class TestOpenFile:
	def pito():
		a = 1 
			
class TestCustomRequest:
	def pito():
		a = 1 
				
print ("NO MOLESTAR")
print (TestCass.pito())
print (TestCass.pito2())
