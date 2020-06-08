def fixTree(tree):
    return [t.strip().center(len(t)) for t in tree]

tree = [
  "      *  ", 
  "    *    ", 
  "***      ", 
  "    *****", 
  "  *******", 
  "*********", 
  " ***     "
]
print(fixTree(tree))