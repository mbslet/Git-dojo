def ExpBin(base, expp, mod):
    resp = 1

    resp = (base ** expp) % mod

    return resp

base = int(input("Digite a base:"))
expoente = int(input("Digite o expoenteeeeee:"))
mod = int(input("Digite o MODULO123456:"))
print(ExpBin(base,expoente,mod))
