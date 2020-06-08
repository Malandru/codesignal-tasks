def pressureGauges(morning, evening):
    return list(zip(*map(sorted, zip(morning, evening))))

morning = [0, 12, 478, 23, 1000]
evening = [48, 23, 56, 23, 88]
print(pressureGauges(morning, evening))