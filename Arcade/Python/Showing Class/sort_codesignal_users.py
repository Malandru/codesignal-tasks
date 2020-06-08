class CodeSignalUser(object):
    def __init__(self, username, id, xp):
        self.username = username
        self._id = int(id)
        self.xp = int(xp)

    def __lt__(self, other):
        if self.xp == other.xp:
            return self._id > other._id
        return self.xp < other.xp

    def __str__(self):
        return self.username


def sortCodesignalUsers(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))


users = [["warrior", "1", "1050"],
         ["Ninja!",  "21", "995"],
         ["recruit", "3", "995"]]
print(sortCodesignalUsers(users))