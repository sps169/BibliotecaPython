class Usuario :
    dni = ""
    nombre = ""
    email = ""
    telefono = ""
    domicilio = ""
    libros = []

    def __init__ (self, dni, nombre, email, telefono, domicilio) :
        self.dni = dni
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.domicilio = domicilio

    def __repr__(self) -> str:
        return "Usuario{" + \
            "dni: " + self.dni + " "\
            "nombre: " + self.nombre + " "\
            "email: " + self.email + " " \
            "telefono: " + self.telefono + " " \
            "domicilio: " + self.domicilio + " " \
            "libros: " + self.libros + " " \
        "}"

class Libro:
    isbn = ""
    titulo = ""
    autor = ""
    genero = ""
    portada = ""
    sinopsis = ""
    ejemplares = 0
    usuario_prestamo = None
    fecha_prestamo = None

    def __init__ (self, isbn, titulo, autor, genero, portada, sinopsis, ejemplares) :
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.portada = portada
        self.sinopsis = sinopsis
        self.ejemplares = ejemplares
    
    def __repr__(self) -> str:
        return "Libro{ " \
            "isbn: " + self.isbn + " " \
            "titulo: " + self.titulo + " " \
            "autor: " + self.autor + " " \
            "genero: " + self.genero + " " \
            "portada: " + self.portada + " " \
            "sinopsis: " + self.sinopsis + " " \
            "ejemplares: " + self.ejemplares + " " \
            "usuario_prestamo: " + self.usuario_prestamo + " " \
            "fecha_prestamo: " + self.fecha_prestamo + " " \
            "}"
class biblioteca:
    lista_libros = []
    lista_usuarios = []