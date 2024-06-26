import funciones as fn

libros = []

while True:
    print("Libreria")
    print("1. Registrar libro")
    print("2. Listar todos los libros")
    print("3. Registrar venta")
    print("4. Imprimir reporte de ventas")
    print("5. Generar txt")
    print("6. Salir")
    
    opc = int(input("ingresa una opcion: "))
    
    if opc == 1:
        fn.registrar_libros(libros)
    elif opc == 2:
        fn.listar_todos(libros)
    elif opc == 3:
        fn.registrar_venta(libros)
    elif opc == 4:
        fn.imprimir_reporte(libros)
    elif opc == 5:
        fn.generar_archivo(libros)
    elif opc == 6:
        break
    else:
        print("Ingrese opcion valida!")
        
        
        