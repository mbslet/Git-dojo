def ExpBin(base, expoente, mod):
    resp = 1

    resp = (base ** expoente) % mod

    return resp

base = int(input("Digite a base:"))
expoente = int(input("Digite o expoente, por favor:"))
mod = int(input("Digite o modulo:"))
print(ExpBin(base,expoente,mod))