def ExpBin(base, expoente, modo):
    resp = 1

    resp = (base ** expoente) % modo

    return resp

base = int(input("Digite a bas:"))
expoente = int(input("Digite o exp:"))
modo = int(input("Digite o mod:"))
print(ExpBin(base,expoente,modo))