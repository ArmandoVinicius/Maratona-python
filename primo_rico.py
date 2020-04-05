num_ini = 2
num_fim = 10

while num_ini <= num_fim:
    num = 2
    testes = 0
    while num < num_ini:
        if num_ini % num == 0 and num_ini % num_ini == 0:
            testes+= 1
        else:
            pass
        num += 1

    if testes == 0:
        print(num_ini, " é primo")
    else:
        print(num_ini, " não é primo")

    num_ini += 1