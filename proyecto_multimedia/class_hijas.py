 
# 2. CLASE HIJA: CANCIÓN (Instanciar, Abstraccion, Herencia, Encapsulamiento y Polimorfismo)

from class_padre_contenid import ContenidoMultimedia



class Cancion(ContenidoMultimedia):
    def __init__(self, titulo: str, duracion: str, artista: str, album: str, letra: str):
        # Hereda los atributos del padre
        super().__init__(titulo, duracion, artista)
        self.album = album
        self.letra = letra
        
        # ENCAPSULAMIENTO: Atributo estrictamente privado
        self.__duracion_privada = duracion 
        
    # Polimorfismo con el método de reproducción
    def reproducir(self):
        print(f"🎧 [...AUDIO...] Sonando en tus audífonos: {self.titulo} - {self.artista} (Álbum: {self.album})")

    # ENCAPSULAMIENTO: Métodos de acceso seguro (Getter & Setter)
    def get_duracion(self):
        return self.__duracion_privada
        
    def set_duracion(self, nueva_duracion: str):
        self.__duracion_privada = nueva_duracion
        self.duracion = nueva_duracion  # Mantiene sincronizado el atributo público
        
    # POLIMORFISMO: Implementación única de visualización para Canciones
    def ver_contenidos(self):  
        print(f"🎵 [...Canción...] '{self.titulo}' | Álbum: {self.album} | Duración Protegida: {self.__duracion_privada}")  



# 3. CLASE HIJA: PODCAST (Herencia y Polimorfismo)

class Podcast(ContenidoMultimedia):
    def __init__(self, titulo: str, duracion: str, artista: str, num_episodios: int, invitados: list):
        # Hereda los atributos del padre
        super().__init__(titulo, duracion, artista)
        self.num_episodios = num_episodios
        self.invitados = invitados
        
    # Polimorfismo sobre el método de reproducción
    def reproducir(self):
        print(f"🎙️ [...PODCAST...] Al aire: {self.titulo} - Episodio N°{self.num_episodios}")
                    
    def mostrar_creditos(self):
        # Transforma la lista de invitados a un texto bonito separado por comas
        texto_invitados = ", ".join(self.invitados) if isinstance(self.invitados, list) else self.invitados
        print(f"👥 Hoy nos acompaña: {texto_invitados}")
        
    # POLIMORFISMO: Implementación única de visualización para Podcasts
    def ver_contenidos(self):
        texto_invitados = ", ".join(self.invitados) if isinstance(self.invitados, list) else self.invitados
        print(f"📻 [...Podcast...] '{self.titulo}' (Ep. {self.num_episodios}) | Invitados: {texto_invitados}")
        