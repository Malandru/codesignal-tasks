def phoneCall(min1, min2_10, min11, s):
    s, minutes = s - min1, 1 * (s > 0)
    middle = s // min2_10
    if middle < 9: s = 0
    else: s, middle = s - 9 * min2_10, 9
    minutes += middle + s // min11
    return minutes

min1 = 1
min2_10 = 2
min11 = 1
s = 6
print(phoneCall(min1, min2_10, min11, s))