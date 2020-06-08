"""
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

There is also the step value, which can be used with any of the above:
""" # a[start:stop:step] # start through not past stop, by step

def twoTeams(students):
    return sum(students[::2]) - sum(students[1::2])

students = [1, 11, 13, 6, 14]
print(twoTeams(students))