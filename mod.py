def ExpBin(B, exp, mod):
    resp = 1

    resp = (B ** exp) % mod

    return resp

B = int(input("Digite a base:"))
exp = int(input("Digite o expoente:"))
mod = int(input("Digite o modulo:"))
print(ExpBin(B,exp,mod))