from pprint import pprint
from jsonmerge import merge

f1 = open("project/target/bom.json", "r")


f2 = open("project/target/bom.json", "r")

result = merge(f1.read(), f2.read())

with open('bom.json', 'w') as f:
    f.write(result)
