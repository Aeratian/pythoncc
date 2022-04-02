import re
count = 0
sum = 0
fileName = input('Enter a file name: ')
try:
    handle = open(fileName)
except FileNotFoundError:
    print('File cannot be opened: ', fileName)
    quit()
for line in handle:
    if(re.search('^X-DSPAM-Confidence:', line)):
        count = count + 1
        pos = line.find(':')
        num = float(line[pos + 1:len(line)])  
        sum = sum + num
print('Average spam confidence:', sum / count)
