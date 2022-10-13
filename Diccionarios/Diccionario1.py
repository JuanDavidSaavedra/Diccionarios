productos = {1: ["sal", 1200, 5], 2: ["azucar", 3000, 4], 3: ["arroz", 2800, 5]}
#try:
codigo = int(input("Digite el código del producto a buscar: "))
print(productos[codigo][0])

x = int(input("Digite numerador: "))
y = int(input("Digite denominador: "))
while y==0:
    print("Valor incorrecto, no puede ser 0.")
    y = int(input("digite de nuevo el denominador: "))


if y!=0:
    print(x/y)
else:
    print("La división no se pudo realizar, ya que el denominador es 0.")

#except IndexError:
    print("Error")