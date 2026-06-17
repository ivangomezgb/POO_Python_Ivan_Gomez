"""
class Usuario:  #define clase
    id_usuario = 1
    documento = 1057581995
    nombre = "Leito"
    apellido = "Gomez"
    correo = "leito@gmail.com"
    telefono = "312367890"
    direccion = "Carrera 22"
    
    
# Creando una instancia de la clase Usuario

usuario_1 = Usuario()

usuario_1.nombre = "Ivan" # se cambia el nombre
print(usuario_1.nombre)
"""


lista_usuarios = [] # Lista global para almacenar los usuarios creados


class Usuario:
    def __init__(self,id_usuario: int,documento,nombre:str,apellido:str,correo,telefono,direccion):
        self.id_usuario = id_usuario
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y apellido es {self.apellido}")
    
    
#Metodos BASE CRUD

#CREATE
    def crear_usuario(self):
        lista_usuarios.append(self)
        print(f"✅ Exito: El usuario {self.nombre} ha sido registrado en el sistema.")
    
# READ
    def ver_usuario(self):
        print(f"ID: {self.id_usuario} NOMBRE: {self.nombre} APELLIDO: {self.apellido}")
    
# UPDATE
    def actualizar_usuario(self, nuevo_nombre, nuevo_apellido):
        self.nombre = nuevo_nombre
        self.apellido = nuevo_apellido
        print(f"Exito: El usuario ha sido actualizado a {self.nombre} {self.apellido}.")

# DELETE
    def eliminar_usuario(self):
        if self in lista_usuarios:
            lista_usuarios.remove(self)
            print(f"Exito el usuario {self.nombre} ha sido eliminado")
        else:
            print(f"Advertencia El usuario {self.nombre} no se encuentra en el sistema")
        

   
# Vamos a crear una instancia de la clase Usuario
usuario_1 = Usuario(1,1057581995,"IvanStiwar","Gomez","LEITO@hotmail.com",12345678,"cra 28 11 b-62")
print(usuario_1.nombre)

usuario_2 = Usuario(2,1057597995,"Messi","Michuca","messirve@hotmail.com",12367899678,"cra 26")

print("\n")

# Llama a los metodos de la clase Usuario
usuario_1.saludar()
usuario_2.saludar()

print("\n")

#Llamar a los atributos de la clase Usuario
print(usuario_1.nombre)
print(usuario_2.nombre)

print("\n")

print(f"Esta es la lista de usuarios {lista_usuarios}")#lista vacia
# Metodo CREATE
usuario_1.crear_usuario()
usuario_2.crear_usuario()

print("\n")

#metodos READ
print(f"Esta es la lista de usuarios {lista_usuarios}")# Lista con usuario 1 agregado el objeto poo
print(f"Lista de usuarios agregados {lista_usuarios[0].nombre}")# Lista con un usuario_1: IvanStiwar
print(f"Lista de usuarios agregados {lista_usuarios[1].nombre}")# Lista con un usuario_2: Messi
usuario_1.ver_usuario()
usuario_2.ver_usuario()

print("\n")

# METODOS UPDATE
usuario_1.actualizar_usuario("Cristiano","Ronaldo")
usuario_1.ver_usuario()

print("\n")

# METODOS DELETE
#llama metodos delete
usuario_1.eliminar_usuario("Cristiano","Ronaldo")
# llama atributos 
print(usuario_1.nombre)
usuario_1.ver_usuario()

