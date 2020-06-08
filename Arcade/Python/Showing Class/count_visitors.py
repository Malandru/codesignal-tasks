class Counter(object):
    def __init__(self, beta):
        self.value = beta

    def inc(self):
        self.value += 1

    def get(self):
        return self.value


def countVisitors(beta, k, visitors):
    counter = Counter(beta)
    for visitor in visitors:
        if visitor >= k:
            counter.inc()
    return counter.get()

beta = 22
k = 5
visitors = [4, 6, 6, 5, 2, 2, 5]
print(countVisitors(beta, k, visitors))