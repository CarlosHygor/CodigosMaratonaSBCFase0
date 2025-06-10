n = int(input())
entrada = input().split()
numeros = [n]
for i in range(n):
    numeros.append(int(entrada[i]))
q = int(input())
for nsei in range(q):
    qntd = 0
    somaEsperada = int(input())
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if numeros[i]+numeros[j]+numeros[k]+numeros[l] == somaEsperada:
                        qntd += 1
    print(qntd)
