m: type[int]
qbitCapacidade: type[float]
qbitQntd: type[int]

m = int(input())

m = (m * (10 ** 6))

qbitCapacidade = 0.0
qbitQntd = 0

while (qbitCapacidade <= m):
    qbitQntd += 1
    qbitCapacidade = (2 ** qbitQntd) / 8.0

print(qbitQntd)
