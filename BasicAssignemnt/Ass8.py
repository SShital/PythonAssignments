n=int(input('Enter the number: '))
i=1
sum=0
while i< n:
    if i%2 != 0:
        sum=sum+i
    i=i+1
print 'Sum of odd numbers',sum

