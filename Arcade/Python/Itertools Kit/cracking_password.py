from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(filter(lambda x: int(x) % d == 0, map(createNumber, product(digits, repeat=k))))

digits = [4, 6, 0, 3]
k = 4
d = 13
print(crackingPassword(digits, k, d))