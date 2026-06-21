# SYSTEMA DE GESTIÓN DE CONTENIDO MULTIMEDIA (POO)



# Lista global para almacenar el contenido multimedia creado(Lista de Contenidos)
lista_contenido = [] 



# 1. CLASE PADRE (Estructura Base del Sistema)

class ContenidoMultimedia:
    def __init__(self, titulo: str, duracion: str, artista: str):
        self.titulo = titulo
        self.duracion = duracion
        self.artista = artista
        
    # --- Métodos del CRUD ---
    # Create
    def crear_contenido(self):
        # Agrega la instancia actual a la lista global del sistema.
        lista_contenido.append(self)
        print(f"✅ Éxito: El contenido '{self.titulo}' ha sido creado y registrado.") 
    # Read
    def ver_contenido(self):
        # Muestra en consola la información básica del objeto.
        print(f"🎵 [Multimedia] Título: {self.titulo} | Duración: {self.duracion} | Artista: {self.artista}")
    # Update    
    def actualizar_contenido(self, nuevo_titulo: str, nueva_duracion: str, nuevo_artista: str):
        # Modifica los atributos públicos principales.
        self.titulo = nuevo_titulo
        self.duracion = nueva_duracion
        self.artista = nuevo_artista
        print(f"🔄 Éxito: Actualizado a -> '{self.titulo}' por {self.artista}")
    # Delete 
    def eliminar_contenido(self):
        # Remueve la instancia de la lista global si existe.
        if self in lista_contenido:
            lista_contenido.remove(self)
            print(f"🗑️ Éxito: '{self.titulo}' ha sido eliminado del sistema.")
        else:
            print(f"❌ Advertencia: '{self.titulo}' no se encuentra en el sistema.")
            
    # --- Método de Control reproduccion ---
    def reproducir(self):
        print(f"\n[▶️ PLAY] Iniciando: {self.titulo} - {self.artista}")
    # --- Método de Control Pausar ---
    def pausar(self):
        print(f"[⏸️ PAUSE] Se ha pausado: {self.titulo}")
    
    # --- Base para el Polimorfismo ---
    def ver_contenidos(self):  
        # Método base para ser sobreescrito por las clases hijas.
        print(f"Contenido Multimedia General: {self.titulo}")