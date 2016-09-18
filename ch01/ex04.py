import re

regex = r'^[a-zA-Z_][0-9a-zA-Z_]*$'

while True:
    name = input('> ')
    if not name:
        break
    result = re.match(regex, name)
    if result:
        print("OK:\t", result.group())
    else :
        print("Not!\t", name)