def ExpBin(base, expp, mod):
    resp = 1

    resp = (base ** expp) % mod

    return resp

base = int(input("Digite a base: "))
expp = int(input("Digite o expoente: "))
mod = int(input("Digite o modulo: "))
print(ExpBin(base,expp,mod))