from itertools import dropwhile

def memoryPills(pills):
    gen = dropwhile(lambda p: len(p) % 2 == 1, pills + [""] * 3)
    next(gen)
    return [next(gen) for _ in range(3)]

pills = ["Notforgetan", "Antimoron", "Rememberin", "Bestmedicen", "Superpillsus"]
print(memoryPills(pills))