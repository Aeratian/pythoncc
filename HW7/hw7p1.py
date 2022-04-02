import urllib.request
import urllib.parse
import urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
characters = 0

for line in fhand:
    dec = line.decode()
    if(3000 < characters + dec.__len__()):
        if(characters < 3000):
            print(dec[0: 3000 - characters], end='')
    else:
        print(dec, end = '')
    characters += dec.__len__()
print('\nCharacters:', characters)
    