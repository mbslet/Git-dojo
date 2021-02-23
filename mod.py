def ExpBin(base, expoente, mod):
    resp = 1

    resp = (base ** expoente) % mod

    return resp

expoente = int(input("Expoente:"))
base = int(input("Base:"))
algumaCoisa = int(input("Módulo:"))
print(ExpBin(base,expoente,algumaCoisa))