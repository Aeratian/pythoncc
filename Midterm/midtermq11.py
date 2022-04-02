str = input('')
while str != '':
    total = 0
    a = False
    count = 0
    max = None
    min = None
    nums = str.split(',')
    ints = []
    for i in nums:
        try:
            num = float(i)
            total += num
            count += 1
            if(max is None or max < num):
                max = num
            if(min is None or min > num):
                min = num
            ints.append(num)
        except ValueError:
            print('Input is invalid.')
            a = True
        if a:
            break
    if a:
        a = False
    else:
        ints.sort()
        print('Sorted:', ints, 'Max:', max, 'Avg:', total/count, 'Min:', min)
    str = input('')