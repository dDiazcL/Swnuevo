GENEROS = ['ficcion','aventura','ciencia']

def registrar_libros(libros):
    titulo = input("Ingrese titulo del libro: ")
    autor = input("Ingrese autor del libro: ")
    genero = input("Ingrese genero del libro: (Ficcion/Aventura/Ciencia)").lower()
    while genero not in GENEROS:
        genero = input("Ingrese genero del libro: (Ficcion/Aventura/Ciencia)").lower()
        print("Genero invalida, intente nuevamente!")
    precio = int(input("Ingrese precio del libro: "))
    
    libros.append({
        'Titulo': titulo,
        'Autor' : autor,
        'Genero' : genero,
        'Precio' :precio
    })
    
def listar_todos(libros):
    for libro in libros:
        print(libro)
        
def registrar_venta(libros):
    cantidadvendida = int(input("Ingrese cantidad: "))
    precioxunidad = int(input("Ingrese precio x unidad: "))
    precio_final = cantidadvendida * precioxunidad
    while cantidadvendida > 10:
        print("Esta exediente la cantidad maxima de libros a comprar!")
        
    libros.append({
        'Cantidad Vendida' : cantidadvendida,
        'Precio x Unidad' :precioxunidad,
        'Precio Final' :precio_final
    })
    
def mostrar_boleta(ventas,libros):
    for ventas in libros:
        print(ventas)

def imprimir_reporte(libros):
    generoseleccionado = input("ingrese genero para imprimir o presione ENTER para imprimir todos").lower()
    if generoseleccionado == "":
        libros_a_imprimir = libros
        nombreArchivo = 'reporte_todos.txt'
    elif generoseleccionado in GENEROS:
        libros_a_imprimir = []
        for libro in libros:
            if libro['genero'] == libros_a_imprimir:
                libros_a_imprimir.append(libros)
        nombreArchivo = f'reporte_{generoseleccionado}.txt'
    else:
        print("Genero no valido!")
        return
    
    with open(nombreArchivo, 'w') as archivo:
        for libro in libros_a_imprimir:
            archivo.write(f"Titulo: {libros['Titulo']}\n")
            archivo.write(f"Autor: {libros['Autor']}\n")
            archivo.write(f"Genero: {libros['Genero']}\n")
            archivo.write(f"Precio: {libros['Precio']}\n")
            archivo.write(f"Cantidad Vendida: {libros['Cantidad Vendida']}\n")
            archivo.write(f"Precio Final: {libros['Precio Final']}\n\n")