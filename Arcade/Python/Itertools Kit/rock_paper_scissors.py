from itertools import permutations

def rockPaperScissors(players):
    return sorted(permutations(players, 2))

players = ["trainee", "warrior", "ninja"]
print(rockPaperScissors(players))
