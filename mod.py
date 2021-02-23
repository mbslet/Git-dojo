def ExpBin(base, expoente, moda):
    resp = 1

    resp = (base ** expoente) % mod

    return resp

base = int(input("Digite a base:"))
expoente = int(input("Digite o expoente, por favorgi:"))
mod = int(input("Digite o modulo:"))
print(ExpBin(base,expoente,mod))