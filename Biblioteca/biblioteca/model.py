class Usuario :
    __dni = ""
    __nombre = ""
    __email = ""
    __telefono = ""
    __domicilio = ""
    __libros = []

    def __init__ (self, dni, nombre, email, telefono, domicilio) :
        self.__dni = dni
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
        self.__domicilio = domicilio

    def get_dni(self) :
        return self.__dni

    def set_dni(self, dni) :
        self.__dni = dni
        
    dni = property(get_dni, set_dni)

    def get_nombre(self) :
        return self.__nombre

    def set_nombre(self, nombre) :
        self.__nombre = nombre

    nombre = property(get_nombre, set_nombre)

    def get_email(self) :
        return self.__email

    def set_email(self, email) :
        self.__email = email

    email = property(get_email, set_email)

    def get_telefono(self) :
        return self.__telefono

    def set_telefono(self, telefono) :
        self.__telefono = telefono
        
    telefono = property(get_telefono, set_telefono)

    def get_domicilio(self) :
        return self.__domicilio

    def set_domicilio(self, domicilio) :
        self.__domicilio = domicilio
        
    domicilio = property(get_domicilio, set_domicilio)

    def get_libros(self) :
        return self.__libros

    def set_libros(self, libros) :
        self.__libros = libros
        
    libros = property(get_libros, set_libros)

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
    __isbn = ""
    __titulo = ""
    __autor = ""
    __genero = ""
    __portada = ""
    __sinopsis = ""
    __ejemplares = 0
    __usuario_prestamo = None
    __fecha_prestamo = None

    def __init__ (self, isbn, titulo, autor, genero, portada, sinopsis, ejemplares) :
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__portada = portada
        self.__sinopsis = sinopsis
        self.__ejemplares = ejemplares
    
    def get_isbn(self) :
        return self.__isbn

    def set_isbn(self,isbn) :
        self.__isbn = isbn
        
    isbn = property(get_isbn, set_isbn)

    def get_titulo(self) :
        return self.__titulo

    def set_titulo(self, titulo) :
        self.__titulo = titulo

    titulo = property(get_titulo, set_titulo)

    def get_autor(self) :
        return self.__autor

    def set_autor(self, autor) :
        self.__autor = autor

    autor = property(get_autor, set_autor)

    def get_genero(self) :
        return self.__genero

    def set_genero(self, genero) :
        self.__genero = genero
        
    genero = property(get_genero, set_genero)

    def get_portada(self) :
        return self.__portada

    def set_portada(self, portada) :
        self.__portada = portada
        
    portada = property(get_portada, set_portada)

    def get_sinopsis(self) :
        return self.__sinopsis

    def set_sinopsis(self, sinopsis) :
        self.__sinopsis = sinopsis
        
    sinopsis = property(get_sinopsis, set_sinopsis)

    def get_ejemplares(self) :
        return self.__ejemplares

    def set_ejemplares(self, ejemplares) :
        self.__ejemplares = ejemplares
        
    ejemplares = property(get_ejemplares, set_ejemplares)
    
    def get_usuario_prestamo(self) :
        return self.__usuario_prestamo

    def set_usuario_prestamo(self, usuario_prestamo) :
        self.__usuario_prestamo = usuario_prestamo
        
    usuario_prestamo = property(get_usuario_prestamo, set_usuario_prestamo)    

    def get_fecha_prestamo(self) :
        return self.__fecha_prestamo

    def set_fecha_prestamo(self, fecha_prestamo) :
        self.__fecha_prestamo = fecha_prestamo
        
    fecha_prestamo = property(get_fecha_prestamo, set_fecha_prestamo)    

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
<<<<<<< HEAD

=======
>>>>>>> 5e4e4be99e416923b61b8f9ca2a9d2a0b106e523
class Biblioteca:
    lista_libros = []
    lista_usuarios = []