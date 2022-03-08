from typing import List


class Usuario :

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

    def __repr__(self) -> str:
        return "Usuario{" + \
            "dni: " + self.dni + ", "\
            "nombre: " + self.nombre + ", "\
            "email: " + self.email + ", " \
            "telefono: " + self.telefono + ", " \
            "domicilio: " + self.domicilio + "" \
        "}"

class Libro:

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

    def __repr__(self) -> str:
        return "Libro{ " \
            "isbn: " + self.isbn + ", " \
            "titulo: " + self.titulo + ", " \
            "autor: " + self.autor + ", " \
            "genero: " + self.genero + ", " \
            "portada: " + self.portada + ", " \
            "sinopsis: " + self.sinopsis + ", " \
            "ejemplares: " + str(self.ejemplares) + "" \
            "}"

class Prestamo:
    curr_id = 1

    def __init__(self, libro, usuario, fecha) :
        self.__id = Prestamo.curr_id
        Prestamo.curr_id = Prestamo.curr_id + 1
        self.__libro = libro
        self.__usuario = usuario
        self.__fecha = fecha

    def get_id(self) :
        return self.__id

    def set_id(self, id) :
        self.__id = id

    id = property(get_id, set_id)
    
    def get_libro(self) :
        return self.__libro

    def set_libro(self, libro) :
        self.__libro = libro

    libro = property(get_libro, set_libro)

    def get_usuario(self) :
        return self.__usuario
    
    def set_usuario(self, usuario) :
        self.__usuario = usuario

    usuario = property(get_usuario, set_usuario)

    def get_fecha(self) :
        return self.__fecha

    def set_fecha(self, fecha) :
        self.__fecha = fecha

    fecha = property(get_fecha, set_fecha)

    def __repr__(self) -> str:
        return "Prestamo{ " \
            "id: " + str(self.id) + ", " \
            "libro: " + str(self.libro) + ", " \
            "usuario: " + str(self.usuario) + ", " \
            "fecha: " + str(self.fecha) + "" \
            "}"

class BibliotecaObject:

    def __init__(self) :
        self.__lista_libros = []
        self.__lista_usuarios = []
        self.__lista_prestamos = []

    def get_lista_libros(self) :
        return self.__lista_libros

    def set_lista_libros(self, lista_libros) :
        self.__lista_libros = lista_libros

    lista_libros = property(get_lista_libros, set_lista_libros)

    def get_lista_usuarios(self) :
        return self.__lista_usuarios

    def set_lista_usuarios(self, lista_usuarios) :
        self.__lista_usuarios = lista_usuarios

    lista_usuarios = property(get_lista_usuarios, set_lista_usuarios)
    
    def get_lista_prestamos(self) :
        return self.__lista_prestamos

    def set_lista_prestamos(self, lista_prestamos) :
        self.__lista_prestamos = lista_prestamos

    lista_prestamos = property(get_lista_prestamos, set_lista_prestamos)

    def __repr__(self) -> str:
        return "Biblioteca{" \
            "libros: " + str(self.lista_libros) + ", " \
            "usuarios: " + str(self.lista_usuarios) + ", "\
            "prestamos:" + str(self.lista_prestamos) + ""\
            "}"  
