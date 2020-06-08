def knapsackLight(value1, weight1, value2, weight2, maxW):
    return max((value1 + value2) * (weight1 + weight2 <= maxW), value1 * (weight1 <= maxW), value2 * (weight2 <= maxW))


value1 = 10
weight1 = 5
value2 = 6
weight2 = 4
maxW = 8
print(knapsackLight(value1, weight1, value2, weight2, maxW))
