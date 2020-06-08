class Prizes(object):
    def __init__(self, purchases, n, d):
        potentialWinner = lambda tp: tp[0] % n == 0 and tp[1] % d == 0
        self.winners = filter(potentialWinner, enumerate(purchases, start=1))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.winners)[0]


def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))


purchases = [12, 43, 13, 465, 1, 13]
n = 2
d = 3
print(superPrize(purchases, n, d))