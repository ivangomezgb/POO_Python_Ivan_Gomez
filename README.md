# 🎬 Sistema de Gestión de Contenido Multimedia (POO)

<p align="center">
  <b>Evidencia de Desempeño: Arquitectura Modular y Pilares POO</b><br>
  <i>Tecnólogo en Desarrollo de Software</i>
</p>

---

## 📌 Menú Interactivo de Navegación
* 📁 [Estructura del Proyecto](#-estructura-del-proyecto
*  [CRUD de la Clase Padre]
*  [Los 4 Pilares de la POO Aplicados]

---

## 📁 Estructura del Proyecto

<details>
<summary>📦 <b>class_padre_contenid.py</b> <i>(Clic para expandir)</i></summary>
<br>

Es el núcleo del software. Define los cimientos de la aplicación:
* Contiene la **Clase Base** `ContenidoMultimedia`.
* Inicializa los atributos comunes: `titulo`, `duracion` y `artista`.
* Aloja la **lista global en memoria** (`lista_contenido = []`) que simula nuestra base de datos.
* Implementa las funciones nativas de reproducción y pausa.
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
<summary>📦 <b>main.py</b> <i>(Clic para expandir)</i></summary>
<br>

El punto de entrada del programa (Orquestador).
* Se encarga de importar los componentes de los otros archivos.
* Instancia los objetos reales en la memoria.
* Ejecuta las pruebas controladas del CRUD, Encapsulamiento y Polimorfismo.
</details>
