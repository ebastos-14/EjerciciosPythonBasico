precios = {'A': 270, 'B': 340, 'C': 390}
separador = "\n==========================================================="

monedas = []

while True:
    print(separador, "\n Seleccione el producto", separador, "\n A - Producto 1  --  $270\n C - Producto 2  --  $340\n C - Producto 3  --  $390", separador)
    producto = input("\nSeleccione una opcion: ")
    if producto in precios:
        precio = precios[producto]
        break
    else:
        print("Este producto no esta")

print(separador, "Valor de monedas\n $10  |  $50  |  $100", separador)
while True:
    moneda = int(input("$"))
    if moneda in [10, 50, 100]:
        monedas.append(moneda)
        total = sum(monedas)
        if total >= precio:
            break
    else:
        print("\n Valor no valido")

monedasdeVuelto = sorted([100, 50, 10], reverse=True)

print(separador, "\n Vueltos")
total -= precio
for moneda in monedasdeVuelto:
    while total >= moneda:
        print(f"${moneda}")
        total -= moneda