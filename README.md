
<P align="center">
# Sistema de Gestión de Contenido Multimedia (POO)
</p>
<p align="center">
  <b>GESTION DE CONTENIDO MULTIMEDIA + Pilares POO</b><br>
  <i>Ivan Gomez</i>
</p>

---

## 📌 Estructura del Proyecto
* 📁 [Estructura del Proyecto](#-estructura-del-proyecto)
*  [CRUD de la Clase Padre]
*  [Los 4 Pilares de la POO Aplicados]

---

## 📁 Breve Explicacion del Proyecto

<details>
<summary>📦 <b>class_padre_contenid.py</b> <i>(Clic para expandir)</i></summary>
<br>

Es el núcleo del software. Define los conocimientos de la aplicación:
* Contiene la **Clase Base** `ContenidoMultimedia`.
* Inicializa los atributos comunes: `titulo`, `duracion` y `artista`.
* Aloja la **lista global en memoria** (`lista_contenido = []`) es una lista que simula una base de datos como si fuera un archivo "JSON".
* Implementa unas funciones de reproducción y pausa.
</details>

<details>
<summary>📦 <b>class_hij_as.py</b> <i>(Clic para expandir)</i></summary>
<br>

Contiene la especialización del negocio mediante la creación de sub-tipos de contenido:
* **Clase `Cancion`**: Añade soporte exclusivo para `album`, `letra` y encapsula la duración.
* **Clase `Podcast`**: Añade soporte para el control de `num_episodios` e `invitados`.
* Importa la clase base usando: `from class_padre_contenid import ContenidoMultimedia`.
</details>

<details>
<summary>📦 <b>testing.py</b> <i>(Clic para expandir)</i></summary>
<br>

El punto de entrada del programa (Orquestador).
* Se encarga de importar los componentes de los otros archivos.
* Instancia los objetos reales en la memoria.
* Ejecuta las pruebas controladas del CRUD, Encapsulamiento y Polimorfismo.
</details>
