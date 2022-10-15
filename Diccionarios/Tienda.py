productos = {1: ["Sal", 1200], 2: ["Azúcar", 3000], 3: ["Arroz", 2800], 4:["Jabón", 10000]}

try:
    print("-----  MENÚ DE PRODUCTOS  -------\n")
    n=0
    for x in productos.values(): #productos.values()
        n+=1
        print(n, "=", x)

    codigo = int(input("Digite el código del producto que quiere comprar:\n"))

    while codigo not in productos.keys(): #productos.values()
        print("El código del producto no existe")
        codigo = int(input("\nDigite el código del producto a buscar:"))

    print("Nombre:", productos[codigo][0])
    print("Valor:", productos[codigo][1])

    #else:
        #print("El código del producto no existe")

    cantidad = int(input("Digite el número de unidades que desea comprar de este producto"))
    factura = productos[codigo][1]*cantidad
    print("Su factura es: ", factura)
    print("¿Desea comprar algo más? Digite s si sí y n si no")
    

except IndexError:
    print("Error")