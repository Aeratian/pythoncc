maximum = None
minimum = None
while True:
    inp = input('Enter a number: ')
    try:
        if maximum is None or int(inp) > maximum:
            maximum = int(inp)
        if minimum is None or int(inp) < minimum:
            minimum = int(inp)
    except ValueError:
        if inp == 'done':
            break
        print('Invalid Input')
print(maximum, minimum)
