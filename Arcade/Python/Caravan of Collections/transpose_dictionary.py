def transposeDictionary(scriptByExtension):
    return [[k, v] for v, k in sorted(scriptByExtension.items(), key=lambda item: item[1])]

scriptByExtension = {
    "validate": "py",
    "getLimits": "md",
    "generateOutputs": "json"
}
print(transposeDictionary(scriptByExtension))