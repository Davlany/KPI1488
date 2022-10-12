import math
print("Введіть точки вектору А:")

ax = int(input())
ay = int(input())
az = int(input())


print("Введіть точки вектору В:")

bx = int(input())
by = int(input())
bz = int(input())

vector_a = (ax,ay,az)
vector_b = (bx,by,bz)

vectors_sum = (ax+bx, ay+by, az+bz)
vectors_skal_mult = ax*bx + ay*by + az*bz
vectors_vect_mult = (ax*bz - az*by, -(ax*bz - az*bx), ay*bx - ax*by)
vector_a_norm = math.sqrt(ax**2 + ay**2 + az**2)
vector_b_norm = math.sqrt(bx**2 + by**2 + bz**2)
if vector_a_norm*vector_b_norm != 0:
    vectors_cos = vectors_skal_mult/(vector_a_norm*vector_b_norm)
else:
    vectors_cos = 0

print(f"Сума векторів: {vectors_sum}")
print(f"Скалярний добуток: {vectors_skal_mult}")
print(f"Векторний добуток: {vectors_vect_mult}")
print(f"Норма вектора А: {round(vector_a_norm,2)}")
print(f"Норма вектора В: {round(vector_b_norm,2)}")
print(f"Кут між векторами: {round(math.cos(vectors_cos),2)} рад")