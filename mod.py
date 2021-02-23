def ExpBin(B, exp, mod):
    resp = 1

    resp = (B ** exp) % mod

    return resp

base = int(input("Digite a base:"))
expoente = int(input("Digite o expoente:aastesaaaa"))
mod = int(input("Digite o MODULO123456:"))
print(ExpBin(base,expoente,mod))
