import functools

def checkParticipants(participants):
    return functools.reduce(lambda a, p: a + ([p[0]] if p[1] < p[0] else []), enumerate(participants), [])

participants = [0, 1, 1, 5, 4, 8]
print(checkParticipants(participants))