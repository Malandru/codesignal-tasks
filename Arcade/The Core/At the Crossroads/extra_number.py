def extraNumber(a, b, c):
    """
    You're given three integers, a, b and c.
    It is guaranteed that two of these integers are equal to each other.
    What is the value of the third integer?

    Let n and m two equal numbers, then n xor m = 0.
    Let n any integer, then n xor 0 = n.

    :return: int
    """
    return a ^ b ^ c


a, b, c = 2, 7, 2
print(extraNumber(a, b, c))