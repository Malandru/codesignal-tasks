def circleOfNumbers(n, firstNumber):
    return (n / 2 + firstNumber) % n


n = 10
firstNumber = 2
print(circleOfNumbers(n, firstNumber))