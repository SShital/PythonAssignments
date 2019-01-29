"""
#Basic list
------------------------------------------------
my_list=[] #empty list
my_list1 = [1, 2, 3]
print my_list1
my_list2 = ["Hello", 1,4, "hiiii"]
print my_list2
--------------------------------
#***Nested list*****
--------------------------------------------
my_list3 = ["mouse", [8, 4, 6], ['a']]
my_list4 = [["cat","dog"], [8, 4, 6], ['a']]
print (my_list4[0][1])
print my_list4[1][0], my_list4[2]
---------------------------------------------------

#Negative index
------------------------------------------------
my_list5 = ['p', 'r', 'o', 'b', 'e']
print my_list5[-1]
print my_list5[-4]
-------------------------------

#Slicing list
my_list6 = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

print my_list6[2:8] , my_list6[-4:-1], my_list6[:4], my_list6[:-1]
print my_list6[:]

#adding elements to the lists
odd = [1,2,3,4]
odd[0] = 5
print odd
odd[1:3] = [11, 12, 13]
print odd

#append and extend

odd = [1, 3, 5]
odd.append(7)
print(odd)
odd.extend([9, 11, 13])
print(odd)

my_words=['s', 'h', 'i', 't','a','l']
my_words.extend("raut")

print my_words
odd = [1, 3, 5]

#Concatination
# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])

#Output: ["re", "re", "re"]
print "**" * 3

#delete or remove elements from a list
my_list7 = ['p','r','o','b','l','e','m']
del my_list7[0]
print my_list7
del my_list7[1:4]
print my_list7

#remove & pop operations:
my_list8 = ['p','r','o','b','l','e','m']
my_list8.remove('p')
print(my_list8)

# Output: 'o'
print(my_list8.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list8)

# Output: 'm'
print(my_list8.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list8)

#List Comprehension
pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)

pow3 =[]
for x in range(10):
    pow2.append(2**x)

Even = sorted([x for x in range(20) if x % 2 == 0] , reverse=True)
print Even

#iterating through list
for fruit in ['apple','banana','mango']:
    print("I like",fruit)

"""
#Handson on slicing

"""
a=[1,2,3,4,5,6,7,8,9]
print(a[::2])

a2=[1,2,3,4,5,6,7,8,9]
a2[::2]=10,20,30,40,50,60

print a2;

#error:ValueError: attempt to assign sequence of size 6 to extended slice of size 5

***************************8
a=[1,2,3,4,5]
print(a[3:0:-1])
*******************888

****************88888
def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])
**********************

-----------------------------------------------------------
arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())

# returns last index
-------------------------------------------
"""



