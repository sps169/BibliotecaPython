from user_handler import add_usuario

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
        add_usuario()
    