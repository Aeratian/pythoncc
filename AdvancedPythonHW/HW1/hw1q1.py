count = 0;
sum = 0;
while True:
    inp = input('Enter a number: ')
    try:
        sum = sum + int(inp)
        count = count + 1
    except ValueError:
        if inp == 'done':
            break
        print('Invalid Input')
avg = sum / count
print(sum, count, avg)

