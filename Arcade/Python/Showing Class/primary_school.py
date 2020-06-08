class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return '{} x {} = {}'.format(self.height, self.width, self.area)

    @property
    def area(self):
        return self.height * self.width


def primarySchool(height, width):
    return str(Rectangle(height, width))


height = 7
width = 4
print(primarySchool(height, width))