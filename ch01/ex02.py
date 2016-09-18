import re

regex = r'^[a-zA-Z]+\s[a-zA-Z]+$'

while True:
    name = input('> ')
    if not name:
        break
    result = re.match(regex, name)
    if result:
        print(result.group())