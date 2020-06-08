def uniqueCharacters(document):
    return sorted({ch for ch in document})


document = "Todd told Tom to trot to the timber"
print(uniqueCharacters(document))
