#Menghitung faktorial
def faktorial(n):
    if (n > 1):
        return n * (faktorial(n - 1))
    else:
        return 1

#Menghitung Kombinasi
def C(a, b):
    return faktorial(a)/(faktorial(b)*faktorial(a-b))

#Menghitung Permutasi
def P(a, b):
    return faktorial(a)/faktorial(a-b)


print(C(5, 3))
print(P(10, 7))