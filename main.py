def _min(a):
    if len(a) == 0:
        return None
    mina = a[0]
    for i in a:
        if i < mina:
            mina = i
    return mina


def _max(a):
    if len(a) == 0:
        return None
    maxa = a[0]
    for i in a:
        if i > maxa:
            maxa = i
    return maxa


def _sum(a):
    suma = 0
    for i in a:
        suma += i
    return suma


def _mult(a):
    multa = 1
    for i in a:
        multa *= i
    return multa


with open("input.txt", "r") as file:
    a0 = file.read().split()
    a = [int(i) for i in a0]
    print("В файле:", " ".join(a0))
    print("Минимальное:", _min(a))
    print("Максимальное:", _max(a))
    print("Сумма:", _sum(a))
    print("Произведение:", _mult(a))
