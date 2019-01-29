num = int(input("Enter a number: "))
Add = 0
temp = num

while temp > 0:
   digit = temp % 10
   Add += digit ** 3
   temp //= 10


if num == Add:
   print "is an Armstrong number"
else:
   print "is not an Armstrong number"