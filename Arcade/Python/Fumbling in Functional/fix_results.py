def fixResult(result):
    def fix(x):
        return x // 10

    return list(map(fix, result))

print(fixResult([42, 239, 365, 50]))