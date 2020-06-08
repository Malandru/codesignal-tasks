def reachNextLevel(experience, threshold, reward):
    return experience + reward >= threshold


experience = 10
threshold = 15
reward = 5
print(reachNextLevel(experience, threshold, reward))