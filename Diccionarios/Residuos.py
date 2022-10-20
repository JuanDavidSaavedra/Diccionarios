Tabla = {"Servilletas": "NEGRO", "Cartón": "BLANCO", "Vidrio": "BLANCO", "Restos de pollo": "VERDE"}
lista = []

try:
    x = int(input("Digite el número de participantes: "))
    while x<2 or x>100:
        print("Número incorrecto, mínimo 2, máximo 100: ")
        x = int(input("Digite el número de participantes: "))
    for i in range(x):
        puntaje=0
        print("Inicio de la ronda, para cada residuo digite el color de caneca correspondiente: ")
        for x in Tabla.keys():
            print("Color de",x,": ")
            color = str(input("Escriba el color de la caneca para el residuo: "))
            color = color.upper()
            while color not in Tabla.values(): #productos.values()
                print("Color de caneca inválido, por favor escriba de nuevo el color:")
                color = str(input("Escriba el color de la caneca para el residuo: "))
                color = color.upper()
            if color == Tabla[x]:
                puntaje = puntaje + 10
                print("Respuesta correcta. ")
            else:
                print("Respuesta incorrecta. ")
        print(puntaje)
        lista.append(puntaje)
    lista.sort(reverse=True)
    print("Los 2 puntuajes más altos fueron: " + str(lista[0]) + " y " + str(lista[1]))
except IndexError:
    print("Error") 