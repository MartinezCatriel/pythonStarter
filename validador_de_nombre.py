#validador de nombre
class Nombre(object): #nombre de clases en singular, siempre que no se herede de ninguna clase por defecto implementar object
	
	@staticmethod
	def ValidarElNombre(nombre, validaciones):
		print(nombre)
		for f in validaciones:
			print(f)
			

			
#si el nombre de usuario tiene menos de 6 caracteres retorna el mensaje tal
#si el nombre de usuario tiene mas de 12 caracteres retorna el mensaje tal
#si el nombre de usuario no es alfanumerico devuelve tal mensaje
#si el nombre es valido devuelve true
nombre = "koplankoplan"
if len(nombre) < 6:
	print("“El nombre de usuario debe contener al menos 6 caracteres")
if len(nombre) > 12:
	print("El nombre de usuario no puede contener más de 12 caracteres")
if not nombre.isalnum():
	print("El nombre de usuario puede contener solo letras y números")

	
ValidarNombre.ValidarElNombre("nombreavalidar",["hola", "chau"])

nombre_de_la_funcion = "ValidarElNombre"
if nombre_de_la_funcion in locals():
	print(str(True))
else :
	print(str(False))
