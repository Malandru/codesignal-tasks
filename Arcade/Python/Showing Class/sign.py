class Functions(object):
    @staticmethod
    def sign(x):
        return (x < 0) * -1 + (x > 0) * 1

def sign(x):
    return Functions.sign(x)

x = -35
print(sign(x))