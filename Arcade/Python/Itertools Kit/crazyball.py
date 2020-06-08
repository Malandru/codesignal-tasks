from itertools import combinations

def crazyball(players, k):
    return sorted(map(lambda p: sorted(p), combinations(players, k)))

players = ["Ninja", "Warrior", "Trainee", "Newbie"]
k = 3
print(crazyball(players, k))