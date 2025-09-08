# Sistema de Gestión de Biblioteca Digital

class Libro:
    """
    Clase que representa un libro en la biblioteca.
    El título y el autor se almacenan como una tupla inmutable, ya que no cambian.
    """
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)  # Tupla inmutable con (título, autor)
        self.categoria = categoria    # Categoría del libro (por ejemplo: novela, ciencia, etc)
        self.isbn = isbn              # Código ISBN único del libro
        self.prestado = False         # Indica si el libro está prestado o no

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"'{self.datos[0]}' de {self.datos[1]} [{self.categoria}] - {estado}"


class Usuario:
    """
    Clase que representa a un usuario de la biblioteca.
    Guarda el nombre, el ID único y la lista de libros que tiene prestados.
    """
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre                  # Nombre del usuario
        self.id_usuario = id_usuario          # ID único del usuario
        self.libros_prestados = []            # Lista de libros que tiene prestados actualmente

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"

    def prestar_libro(self, libro):
        """
        Permite al usuario tomar prestado un libro si está disponible.
        """
        if not libro.prestado:
            libro.prestado = True
            self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        """
        Permite al usuario devolver un libro que tenía prestado.
        """
        if libro in self.libros_prestados:
            libro.prestado = False
            self.libros_prestados.remove(libro)


class Biblioteca:
    """
    Clase que gestiona la colección de libros, usuarios y préstamos.
    Usa un diccionario para los libros (clave: ISBN) y un set para los IDs de usuario únicos.
    """
    def __init__(self):
        self.libros = {}           # Diccionario: ISBN -> Libro
        self.usuarios = {}         # Diccionario: ID usuario -> Usuario
        self.ids_usuarios = set()  # Set para asegurar que los IDs de usuario sean únicos

    def añadir_libro(self, libro):
        """
        Añade un libro a la biblioteca.
        """
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        """
        Elimina un libro de la biblioteca por su ISBN.
        """
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario en la biblioteca si su ID no existe.
        """
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
        else:
            print(f"El ID de usuario '{usuario.id_usuario}' ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        """
        Elimina un usuario de la biblioteca por su ID.
        """
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.discard(id_usuario)

    def prestar_libro(self, id_usuario, isbn):
        """
        Permite a un usuario tomar prestado un libro si está disponible.
        """
        usuario = self.usuarios.get(id_usuario)
        libro = self.libros.get(isbn)
        if usuario and libro:
            if libro.prestado:
                print(f"El libro '{libro.datos[0]}' ya está prestado.")
            else:
                usuario.prestar_libro(libro)
                print(f"{usuario.nombre} ha prestado el libro '{libro.datos[0]}'.")
        else:
            print("No se pudo realizar el préstamo. Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        """
        Permite a un usuario devolver un libro que tenía prestado.
        """
        usuario = self.usuarios.get(id_usuario)
        libro = self.libros.get(isbn)
        if usuario and libro:
            if libro in usuario.libros_prestados:
                usuario.devolver_libro(libro)
                print(f"{usuario.nombre} devolvió el libro '{libro.datos[0]}'.")
            else:
                print(f"El usuario {usuario.nombre} no tenía prestado el libro '{libro.datos[0]}'.")
        else:
            print("No se pudo realizar la devolución. Usuario o libro no encontrado.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        """
        Busca libros por título, autor o categoría.
        """
        resultados = []
        for libro in self.libros.values():
            coincide_titulo = titulo is None or titulo.lower() in libro.datos[0].lower()
            coincide_autor = autor is None or autor.lower() in libro.datos[1].lower()
            coincide_categoria = categoria is None or categoria.lower() in libro.categoria.lower()
            if coincide_titulo and coincide_autor and coincide_categoria:
                resultados.append(libro)

        if resultados:
            print("Resultados de la búsqueda:")
            for l in resultados:
                print(f"   - {l}")
        else:
            print("No se encontraron libros que coincidan.")

    def listar_libros_prestados(self, id_usuario):
        """
        Muestra los libros que un usuario tiene prestados.
        """
        usuario = self.usuarios.get(id_usuario)
        if usuario:
            if usuario.libros_prestados:
                print(f"Libros prestados por {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(f"   - {libro}")
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


if __name__ == "__main__":
    # Pruebas del sistema de biblioteca digital

    # Crear libros (título, autor, categoría, ISBN)
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "123456789")
    libro2 = Libro("El Quijote", "Miguel de Cervantes", "Novela", "987654321")
    libro3 = Libro("Breve historia del tiempo", "Stephen Hawking", "Ciencia", "111213141")

    # Crear usuarios
    usuario1 = Usuario("Juan Pérez", "001")
    usuario2 = Usuario("María Gómez", "002")

    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Añadir libros
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Préstamos y devoluciones
    biblioteca.prestar_libro("001", "123456789")
    biblioteca.prestar_libro("002", "987654321")
    biblioteca.devolver_libro("001", "123456789")

    # Buscar libros
    biblioteca.buscar_libro(titulo="Quijote")
    biblioteca.buscar_libro(autor="Hawking")
    biblioteca.buscar_libro(categoria="Novela")

    # Listar libros prestados
    biblioteca.listar_libros_prestados("001")
    biblioteca.listar_libros_prestados("002")
