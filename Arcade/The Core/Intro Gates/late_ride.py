def lateRide(n):
    hh, mm = n // 60, n % 60
    return add(hh) + add(mm)


def add(n):
    return n // 10 + n % 10


n = 808
print(lateRide(n))