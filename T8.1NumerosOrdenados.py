import random
separador = "\n==========================================================="
numRand = [random.randint(1,10) for i in range(10)]
numAsce = sorted(numRand)
numDesc = sorted(numRand, reverse=True)
print(separador, "\nLista de numeros aleatorios", separador)
print(f"Desordenados:", numRand, "\nAscendente:  ", numAsce, "\nDescendente: ", numDesc, separador)
