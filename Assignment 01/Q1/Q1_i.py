#Sum of even numbers in L
L= [11,12,13,14,50,60]
sum =0
for i in range(0, len(L)):
    if (L[i]%2==0):
        sum =sum + L[i]

print(sum)