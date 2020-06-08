def mergingVines(vines, n):
    def nTimes(n): # return lambda f: lambda x:reduce(lambda x,_:f(x),range(n),x)
        def executer(func):
            def inner(arg):
                for _ in range(n):
                    arg = func(arg)
                return arg # return the func result after n iterations
            return inner # Return this function in EXECUTER
        return executer

    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    # return nTimes(n).executer(sumOnce).inner(vines)
    return sumOnce(vines)

vines = [1,2,3,4,5]
n = 2
print(mergingVines(vines, n))