#validador de nombre
class ValidarNombre(object):
	
	@staticmethod
	def ValidarElNombre(nombre, validaciones):
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
	
	
ValidarNombre.ValidarElNombre("", ["hola", "chau"])
