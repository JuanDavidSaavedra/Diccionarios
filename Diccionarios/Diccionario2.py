
productos = {1: ["Sal", 1200, 5], 2: ["Azúcar", 3000, 4], 3: ["Arroz", 2800, 5]}

try:
    print("-----  MENÚ DE PRODUCTOS  -------\n")
    n=0
    for x in productos.values(): #productos.values()
        n+=1
        print(n, "=", x)

    codigo = int(input("Digite el código del producto a buscar:\n"))

    while codigo not in productos.keys(): #productos.values()
        print("El código del producto no existe")
        codigo = int(input("\nDigite el código del producto a buscar:"))

    print("Nombre:", productos[codigo][0])
    print("Valor:", productos[codigo][1])
    print("Saldo actual:", productos[codigo][2])

    #else:
        #print("El código del producto no existe")

except IndexError:
    print("Error")