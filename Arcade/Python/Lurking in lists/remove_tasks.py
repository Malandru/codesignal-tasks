def removeTasks(k, toDo):
    print(toDo[k-1::k])
    del toDo[k::k]
    return toDo


k = 3
toDo = [1237, 2847, 27485, 2947, 1, 247, 374827, 22]
print(removeTasks(k, toDo))