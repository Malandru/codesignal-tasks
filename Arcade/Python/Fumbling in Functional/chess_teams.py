def chessTeams(smarties, cleveries):
    return list(map(lambda s, c: [s, c], smarties, cleveries))

smarties = ["Jane", "Bob", "Peter"]
cleveries = ["Oscar", "Lidia", "Ann"]
print(chessTeams(smarties, cleveries))
