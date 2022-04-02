import re
dictionary_days = dict() 
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    if(re.search('^From', line)):
        words = line.split()
        ind = 0
        day = '' 
        for word in words:
            if(ind == 2):
                day = word
                if(day in dictionary_days):
                    dictionary_days[day] = dictionary_days[day] + 1;
                else:
                    dictionary_days[day] = 1;
            ind = ind + 1
print(dictionary_days)