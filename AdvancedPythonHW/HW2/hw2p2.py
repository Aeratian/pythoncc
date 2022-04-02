fileName = input('Enter a file name: ')
handle = open(fileName)
for line in handle:
    print(line.upper(), end = '')