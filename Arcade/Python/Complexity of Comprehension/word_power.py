def wordPower(word):
    num = dict([(ch, ord(ch) - 96) for ch in word])
    return sum([num[ch] for ch in word])

print(wordPower("hello"))