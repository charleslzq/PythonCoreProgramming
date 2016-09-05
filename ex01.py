import re

test = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']
regex = r'[bh][aiu]t'

for name in test:
    print(re.match(regex, name).group())
