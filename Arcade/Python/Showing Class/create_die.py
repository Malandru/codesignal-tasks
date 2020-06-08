import random
import json


def createDie(seed, n):
    class Die(object):
        def __new__(cls, seed, n):
            print('Creating instance')
            random.seed(seed)
            result = int(random.random() * n) + 1
            return result

    class Game(object):
        die = Die(seed, n)

    return Game.die


seed = 37237
n = 5
result = createDie(seed, n)

data = json.dumps(result, indent=4)
print('JSON data:', data)
print(json.loads(data))
