A = [1,3,5,7,9,10,11,16]
B = [2,4,6,8,10,12,14,15]
n = A.__len__()
ans = []
counta = 0
countb = 0
while (counta < n and countb < n):
    a = A[counta]
    b = B[countb]
    if(a > b):
        countb += 1
        ans.append(b)
    if(b > a):
        counta += 1
        ans.append(a)
    if(a == b):
        counta += 1
        countb += 1
        ans.append(a)
while(counta < n):
    ans.append(A[counta])
    counta += 1
while(countb < n):
    ans.append(B[countb])
    countb += 1
print(ans)