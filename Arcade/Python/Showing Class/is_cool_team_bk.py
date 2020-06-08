import time


def take_time(func):
    def inner(*args, **kwargs):
        begin = time.time()
        ret = func(*args, **kwargs)
        taken = time.time() - begin
        print('Total time taken in {}: {}ms'.format(func.__name__, taken))
        return ret
    return inner


class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        self.graph = self.build_path()
        print(self.graph)
        print(self.used)
        print(self.allowed)
        self.finish = False
        self.backtrack([], None)
        return self.finish
        # return False

    def build_path(self):
        self.setup()
        graph = dict(map(lambda name: (name, []), self.names))
        nodes = graph.keys()
        for node in nodes:
            following = [name for name in nodes if can_follow(name, node)]
            graph[node].extend(following)
            self.allowed[node] = self.names.count(node)
        return graph

    def setup(self):
        self.used = dict(map(lambda name: (name, 0), self.names))
        self.allowed = dict(self.used)

    def backtrack(self, team, last):
        if len(self.names) == len(team):
            self.finish = True
        else:
            if last is None: candidates = self.graph.keys()
            else: candidates = self.graph[last]
            for c in candidates:
                if self.used[c] == self.allowed[c]: continue
                team.append(c)
                self.used[c] += 1
                self.backtrack(team, c)
                if self.finish: return
                team.pop()
                self.used[c] -= 1


def can_follow(name, current):
    return current.lower().endswith(name[0].lower())

@take_time
def isCoolTeam(team):
    return bool(Team(team))

team = ["Mark", "Kelly", "Kurt", "Terk"]
# team = ["Sophie", "Boris", "EriC", "Charlotte"]
# team = ["Sophie", "Edward", "Deb", "Boris", "Stephanie", "Eric", "Charlotte", "Eric", "Charlie"]
print(isCoolTeam(team))