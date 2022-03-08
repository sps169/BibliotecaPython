from biblioteca.library_handler import remove_usuario, store_usuario
from biblioteca.model import BibliotecaObject, Usuario
from biblioteca.utils import get_input


def add_usuario (biblioteca: BibliotecaObject) :
    dni = get_input("Inserte el dni del nuevo usuario")
    nombre = get_input("Inserte el nombre del nuevo usuario")
    email = get_input("Inserte el email del nuevo usuario")
    telefono = get_input("Inserte el telefono del nuevo usuario")
    domicilio = get_input("Inserte el domicilio del nuevo usuario")
    usuario = Usuario(dni, nombre, email, telefono, domicilio)
    store_usuario(usuario, biblioteca)

def delete_usuario(biblioteca: BibliotecaObject) :
    dni = get_input("Inserte el dni del usuario a eliminar")
    for i in biblioteca.lista_usuarios :
        if(i.dni == dni) :
            remove_usuario(i, biblioteca)
