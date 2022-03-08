from biblioteca import menu, model


def main() :
    biblioteca = model.BibliotecaObject()
    while(True) :
        menu.print_menu()
        menu.options_switch(menu.get_user_input(), biblioteca)

if (__name__ == "__main__"):
    main()