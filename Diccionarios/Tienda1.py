productos = {1: ["Sal", 1200, 5], 2: ["Azúcar", 3000, 4], 3: ["Arroz", 2800, 5], 4:["Jabón", 10000, 10]}

try:
    opcion = 0
    while opcion == 0:
        acu = 0
        print("Listado de productos: ")
        print(productos)
        cantidad = int(input("Digite catidad de productos a facturar: "))
        while cantidad <=0:
            print("Cantidad incorrecta")
            cantidad = int(input("Digite la cantidad de productos a facturar: "))

        for i in range(cantidad):
            codigo = int(input("Digite el código del producto: "))
            while codigo not in productos.keys():
                print("Código incorrecto")
                codigo=int(input("Digite el código del producto: "))
            can = int(input("Digite la cantidad del producto: "))
            while can <=0:
                print("Cantidad incorrecta")
                can = int(input("Digite la cantidad del producto: "))
            x = productos[codigo][2]
            while can > x:
                print("Cantidad a comprar superior al saldo.")
                print("Saldo disponible: ", x)
                can = int(input("Digite la cantidad del producto: "))
            print("Código: ", codigo, ", Nombre: ", productos[codigo][0], ", Valor unitario: ", productos[codigo][1], ", Total: ", can*productos[codigo][1])

            acu = acu + can*productos[codigo][1]
            productos[codigo][2] = x - can
        print("Total de la factura: $", acu)
        continuar = int(input("Digite 0 para continuar, 1 para salir: "))

except IndexError:
    print("Error") 