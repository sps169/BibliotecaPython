from Biblioteca.biblioteca.model import Biblioteca

def store_usuario(usuario) :
    Biblioteca.lista_usuarios.append(usuario)

def store_libro(libro) :
    Biblioteca.lista_libros.append(libro)

def remove_usuario(usuario) :
    Biblioteca.lista_usuarios.remove(usuario)

def remove_libro(libro) :
    Biblioteca.lista_libros.remove(libro)

def prestar_libro(isbn, dni) :
    Biblioteca