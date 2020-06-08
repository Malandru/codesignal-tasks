def calkinWilfSequence(number):
    def fractions():
        import queue
        q = queue.deque([(1, 1)])
        while True:
            a, b = q.popleft()
            yield [a, b]
            c = a + b
            q.append((a, c))
            q.append((c, b))

        # n, d = 1, 1
        # while True:
        #     yield [n, d]
        #     n, d = d, 2 * (n // d) * d + d - n


    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res

number = [100, 99]
print(calkinWilfSequence(number))