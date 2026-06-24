#Gestion de Peliculas
 
peliculas = [
{"titulo", "Oppenheimer"},{"duracion", 180}, {"calificacion", 8.5}, {"estado", "Disponible"}
] 
salir = False
#menu

while salir == False:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")
    eleccion = input("seleccione la accion a tomar: ")

    if eleccion.isdigit():
        elecN = int(eleccion)
    else:
        print("elija una opcion valida")
    
    if elecN == 1:
        titulo = input("ingrese el titulo de la pelicula a agregar: ")
        if titulo == " " or "":
            print("titulo no valido")
        else:
            peliculas;{"titulo", titulo}
            titulo = ""
        try:
            duracion = int(input("ingrese la duracion de la pelicula: "))
            if duracion <= 0 or duracion == float:
                print("duracion no valida")
            else:
                peliculas;{"duracion", duracion}
        except:
            print("duracion no valida")
        calificacion = float(input("ingrese la calificacion de la pelicula(entre 0.0 y 10.0): "))
        if calificacion > 10.0 or calificacion < 0:
            print("calificacion no valida")
        else:
            peliculas;{"calificacion", calificacion}
        print(peliculas)
    
