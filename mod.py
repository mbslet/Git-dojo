def ExpBin(base, expoente, mod):
    resp = 1

    resp = (base ** expoente) % mod

    return resp

base = int(input("Base:"))
expoente = int(input("Expoente:"))
algumaCoisa = int(input("Módulo:"))
print(ExpBin(base,expoente,mod))