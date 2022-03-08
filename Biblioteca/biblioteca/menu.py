from biblioteca import library_handler
from biblioteca.model import BibliotecaObject


def print_menu() :
    print("Elija una opción")
    print("1. Dar de alta un usuario")
    print("2. Dar de baja un usuario")
    print("3. Dar de alta un libro")
    print("4. Dar de baja un libro")
    print("5. Prestar un libro")
    print("6. Devolver un libro")
    print("7. Consultar un usuario")
    print("8. Consultar un libro")
    print("9. Consultar un prestamo")
    print("0. Salir")

def get_user_input() :
    return int(input())

def options_switch(user_input, biblioteca: BibliotecaObject) :
    if (user_input == 1) :
        library_handler.store_usuario(biblioteca)

    if (user_input == 2) :
        library_handler.remove_usuario(biblioteca)

    if (user_input == 3) :
        library_handler.store_libro(biblioteca)

    if (user_input == 4) :
        library_handler.remove_libro(biblioteca)

    if (user_input == 5) :
        library_handler.store_prestamo(biblioteca)

    if (user_input == 6) :
        library_handler.remove_prestamo(biblioteca)

    if (user_input == 7) :
        library_handler.ver_usuario(biblioteca)

    if (user_input == 8) :
        library_handler.ver_libro(biblioteca)

    if (user_input == 9) :
        library_handler.ver_prestamo(biblioteca)

    if (user_input == 0) :
        print("Hasta pronto!")
        quit()
