def ExpBin(base, expp, mod):
    resp = 1

    resp = (base ** expp) % mod

    return resp

base = int(input("Digite a base:"))
expoente = int(input("Digite o expoente:"))
mod = int(input("Digite o MODULO1234567:"))
print(ExpBin(base,expoente,mod))
