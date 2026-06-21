from class_padre_contenid import ContenidoMultimedia, lista_contenido
from class_hijas import Cancion, Podcast

if __name__ == "__main__":
    print("===  CRUD BASE ===")
    
    # Instanciación de objetos de la clase base
    contenido_1 = ContenidoMultimedia("Get Lucky", "4:00", "Daft Punk")
    contenido_2 = ContenidoMultimedia("Yo no sé qué hacer contigo", "3:00", "Juan Pérez")

    # Create
    contenido_1.crear_contenido()
    contenido_2.crear_contenido()

    # Read
    print(f"\n Verificando títulos en la lista global:........")
    print(f"   Posición 0: {lista_contenido[0].titulo}")
    print(f"   Posición 1: {lista_contenido[1].titulo}\n")
    contenido_1.ver_contenido()

    # Update
    contenido_1.actualizar_contenido("Get Lucky (Remix)", "5:00", "Daft Punk ft. Pharrell")
    contenido_1.ver_contenido()

    # Delete
    print("")
    contenido_2.eliminar_contenido()


    print("\n=== 🔒 ENCAPSULAMIENTO (Manejo de Datos de Forma Segura) ===")
    cancion_1 = Cancion("Blinding Lights", "3:20", "The Weeknd", "After Hours", "I've been on my own...")
    
    # Uso correcto del Getter
    print(f"🔓 Consulta inicial vía GETTER: {cancion_1.get_duracion()}")
    
    # Uso correcto del Setter
    cancion_1.set_duracion("3:45")
    print(f"🔐 Modificación exitosa vía SETTER: {cancion_1.get_duracion()}")


    print("\n=== 🔄 POLIMORFISMO podcast ===")
    podcast_1 = Podcast("El Podcast de la Vida", "60:00", "Juan Pérez", 10, ["María Gómez", "Carlos López"])

    # Agrupamos las instancias de diferentes clases en una sola colección
    playlist_mix = [cancion_1, podcast_1]

    # El bucle invoca la misma firma de método, pero la salida se adapta al objeto ejecutor
    for elemento in playlist_mix:
        elemento.ver_contenidos()
        elemento.reproducir()
        print("-" * 60)