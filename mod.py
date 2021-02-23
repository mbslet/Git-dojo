def ExpBin(base, expoente, mod):
    resp = 1

    resp = (base ** expoente) % mod

    return resp

base = int(input("Digite a bas:"))
expoente = int(input("Digite o exp:"))
mod = int(input("Digite o mod:"))
print(ExpBin(base,expoente,mod))