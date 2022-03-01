import user_handler
import book_handler
import library_handler

def print_menu() :
    print("Elija una opción")
    print("1. Dar de alta un usuario")
    print("2. Dar de baja un usuario")
    print("3. Dar de alta un libro")
    print("4. Dar de baja un libro")
    print("5. Prestar un libro")
    print("6. Devolver un libro")
    print("7. Consultar un libro")
    print("8. Consultar un usuario")
    print("9. Consultar un prestamo")
    print("0. Salir")

def get_user_input() :
    return int(input)

def options_switch(user_input) :
    if (user_input == 1) :
        user_handler.add_usuario()
    if (user_input == 2) :
        user_handler.remove_usuario()
    if (user_input == 3) :
        book_handler.add_libro()
    if (user_input == 4) :
        book_handler.remove_libro()
    if (user_input == 5) :
        library_handler.prestar_libro()
    if (user_input == 6) :
        library_handler.devolver_libro()
    if (user_input == 7) :
        book_handler.ver_libro()
    if (user_input == 8) :
        user_handler.ver_usuario()
    if (user_input == 9) :
        library_handler.ver_prestamo()
    if (user_input == 0) :
        print("Hasta pronto!")
        quit()