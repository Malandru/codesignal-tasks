def isTestSolvable(ids, k):
    digitSum = lambda id: sum(int(d) for d in str(id))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0

ids = [529665, 909767, 644200] 
k = 3
print(isTestSolvable(ids, k))