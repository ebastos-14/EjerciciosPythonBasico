valAlza = []
valDolar = []
separador = "\n==========================================================="
numDias = int(input(f"{separador}\nIngrese el numero de dias a registrar: "))
print(f"{separador}\nIngrese el valor del dolar para los", numDias, "dias")
for i in range(1, numDias + 1):
    numDolar = float(input(f"Dia {i} => "))
    valDolar.append(numDolar)

for i in range(numDias - 1):
    numAlza0 = valDolar[i + 1] - valDolar[i]
    valAlza.append(numAlza0)

alza = max(valAlza)
print(f"El valor mayor del alza fue:", alza, separador)