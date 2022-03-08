from datetime import date
from biblioteca.model import BibliotecaObject, Usuario, Libro, Prestamo
from biblioteca.utils import get_input

def store_usuario(biblioteca: BibliotecaObject) :
    dni = get_input("Inserte el dni del nuevo usuario")
    nombre = get_input("Inserte el nombre del nuevo usuario")
    email = get_input("Inserte el email del nuevo usuario")
    telefono = get_input("Inserte el telefono del nuevo usuario")
    domicilio = get_input("Inserte el domicilio del nuevo usuario")
    usuario = Usuario(dni, nombre, email, telefono, domicilio)
    isPresent = False
    for i in biblioteca.lista_usuarios :
        if (i.dni == usuario.dni) :
            isPresent = True
    if (not isPresent) :        
        biblioteca.lista_usuarios.append(usuario)
        print("El usuario con DNI " + str(usuario.dni) + " se ha insertado.")
    else :
        print("ERROR: Ya existe un usuario con ese DNI.")

def store_libro(biblioteca) :
    isbn = get_input("Inserte el isbn del nuevo libro")
    titulo = get_input("Inserte el titulo del nuevo libro")
    autor = get_input("Inserte el autor del nuevo libro")
    genero = get_input("Inserte el genero del nuevo libro")
    portada = get_input("Inserte la portada del nuevo libro")
    sinopsis = get_input("Inserte la sinopsis del nuevo libro")
    ejemplares = int(get_input("Inserte el numero de ejemplares del nuevo libro"))
    libro = Libro(isbn, titulo, autor, genero, portada, sinopsis, ejemplares)
    isPresent = False
    for i in biblioteca.lista_libros :
        if (i.dni == libro.dni) :
            isPresent = True
    if (not isPresent) :        
        biblioteca.lista_libros.append(libro)
        print("El libro con ISBN " + str(libro.isbn) + " se ha insertado.")
    else :
        print("ERROR: Ya existe un libro con ese ISBN.")
        
def store_prestamo(biblioteca) :
    usuarioCorrecto = False
    usuario = None
    while(not usuarioCorrecto) :
        usuarioDNI = get_input("Inserte el DNI del usuario que va a realizar el prestamo.")
        for i in biblioteca.lista_usuarios :
            if (i.dni == usuarioDNI) :
                usuario = i
                usuarioCorrecto = True
        if (not usuarioCorrecto) :
            print("Ese usuario no existe, intentelo de nuevo")

    libroCorrecto = False
    libro = None
    while(not libroCorrecto) :
        libroISBN = get_input("Inserte el ISBN del libro que va ser prestado.")
        for i in biblioteca.lista_libros :
            if (i.isbn == libroISBN) :
                libro = i
                libroCorrecto = True
        if (not libroCorrecto) :
            print("Ese libro no existe, intentelo de nuevo")
    
    prestamo = Prestamo(libro, usuario, date.today())

    isPresent = False
    for i in biblioteca.lista_prestamos :
        if (i.libro.isbn == prestamo.libro.isbn) :
            isPresent = True
    if (not isPresent) :        
        biblioteca.lista_prestamos.append(prestamo)
        print("El prestamo del libro con ISBN " + str(prestamo.libro.isbn) 
        + " al usuario con DNI " + str(prestamo.usuario.dni) 
        + " se ha realizado con fecha " + str(prestamo.fecha) + ".")
    else :
        print("ERROR: Este libro ya está prestado.")

def remove_usuario(biblioteca) :
    hasPrestamo = False
    dni = get_input("Inserte el dni del usuario a eliminar")
    for i in biblioteca.lista_prestamos:
        if (i.usuario.dni == dni) :
            hasPrestamo = True

    if (not hasPrestamo) :
        removed = False
        for i in biblioteca.lista_usuarios :
            if(i.dni == dni) :
                biblioteca.lista_usuarios.remove(i)
                print("Se ha eliminado el usuario con DNI " + str(i.dni))
                removed = True
        if (not removed) : 
            print("No se ha encontrado el usuario con DNI" + str(dni))
    else :
        print("No se puede borrar un usuario que tiene libros prestados!")

def remove_libro(biblioteca) :
    hasPrestamo = False
    isbn = get_input("Inserte el isbn del usuario a eliminar")
    for i in biblioteca.lista_prestamos:
        if (i.libro.isbn == isbn) :
            hasPrestamo = True

    if (not hasPrestamo) :
        removed = False
        for i in biblioteca.lista_libros :
            if(i.isbn == isbn) :
                biblioteca.lista_libros.remove(i)
                print("Se ha eliminado el libro con ISBN " + str(i.isbn))
                removed = True
        if (not removed) : 
            print("No se ha encontrado el libro con ISBN" + str(isbn))
    else :
        print("No se puede borrar un libro que está prestado!")

def remove_prestamo(biblioteca) :
    usuarioCorrecto = False
    usuario = None
    while(not usuarioCorrecto) :
        usuarioDNI = get_input("Inserte el DNI del usuario que va a devolver el libro.")
        for i in biblioteca.lista_usuarios :
            if (i.dni == usuarioDNI) :
                usuario = i
                usuarioCorrecto = True
        if (not usuarioCorrecto) :
            print("Ese usuario no existe, intentelo de nuevo")

    libroCorrecto = False
    libro = None
    while(not libroCorrecto) :
        libroISBN = get_input("Inserte el ISBN del libro que fue prestado.")
        for i in biblioteca.lista_libros :
            if (i.isbn == libroISBN) :
                libro = i
                libroCorrecto = True
        if (not libroCorrecto) :
            print("Ese libro no existe, intentelo de nuevo")

    isPresent = False
    for i in biblioteca.lista_prestamos :
        if ((i.libro.isbn == libro.isbn) & (i.usuario.dni == usuario.dni)) :
            isPresent = True
            biblioteca.lista_prestamos.remove(i)
            print("El prestamo del libro con ISBN " + str(libro.isbn) 
            + " al usuario con DNI " + str(usuario.dni) 
            + " se ha devuelto con fecha " + str(date.today()) + ".")
    if (not isPresent) :        
        print("ERROR: Este usuario no ha prestado este libro.")
        

def ver_usuario(biblioteca) :
    dni = get_input("Inserte el dni del usuario que desea consultar")
    found = False
    for usuario in biblioteca.lista_usuarios :
        if (usuario.dni == dni) :
            print(usuario)
            found = True
    if (not found) :
        print("No se ha encontrado el usuario que desea consultar")

def ver_libro(biblioteca) :
    isbn = get_input("Inserte el isbn del libro que desea consultar")
    found = False
    for libro in biblioteca.lista_libros :
        if (libro.isbn == isbn) :
            print(libro)
            found = True
    if (not found) :
        print("No se ha encontrado el libro que desea consultar")        

def ver_prestamo(biblioteca) :
    userOrBook = ""
    while((userOrBook != "usuario") & (userOrBook != "libro")) :
        userOrBook = get_input(""""Escriba 'usuario' si conoce el DNI del usuario del prestamo o 'libro' si conoce el ISBN del libro prestado.""")
        if ((userOrBook != "usuario") & (userOrBook !="libro")) :
            print("Intentelo de nuevo")
    
    if(userOrBook == "usuario"):
        dni = get_input("Inserte el dni del usuario del prestamo a consultar")
        found = False
        for prestamo in biblioteca.lista_prestamos :
            if (prestamo.usuario.dni == dni) :
                print(prestamo)
                found = True
        if (not found) :
            print("El dni especificado no esta asociado a ningun prestamo existente")
    else :
        isbn = get_input("Inserte el isbn del libro del prestamo a consultar")
        found = False
        for prestamo in biblioteca.lista_prestamos :
            if (prestamo.libro.isbn == isbn) :
                print(prestamo)
                found = True
        if (not found) :
            print("El isbn especificado no esta asociado a ningun prestamo existente")