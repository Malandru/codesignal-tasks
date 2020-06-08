class User(object):
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp
        self.name = name

    def __getattr__(self, name): # Executed only on failed
        return f'{name} attribute is not defined'


def userAttribute(attribute):
    user = User("annymaster", "1234567", "1500", "anny")
    return getattr(user, attribute)

attribute = "_id"
print(userAttribute(attribute))