def ExpBin(base, expoente, mod):
    resp = 1

    resp = (base ** expoente) % mod

    return resp

base = int(input("Digite a base:"))
expoente = int(input("Digite o expoenteeeeee:"))
mod = int(input("Digite o MODULO123456:"))
print(ExpBin(base,expoente,mod))