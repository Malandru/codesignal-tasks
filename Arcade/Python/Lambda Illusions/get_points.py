def getPoints(answers, p):
    questionPoints = lambda i, ok: i + 1 if ok else -p

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res


answers = [True, True, False, True]
p = 2
print(getPoints(answers, p))