import csv

with open('Emp.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)




#print sorted(emplist, key=lambda x:x[0] if x[1]=='IT' else 0,  reverse=True)[0][0]

"""max_age = None
oldest_person = None
for row in input_file:
    age = int(row["age"])
    if max_age == None or max_age < age:
        max_age = age
        oldest_person = row["name"]

if max_age != None:
    print "The oldest person is %s, who is %d years old." % (oldest_person, max_age)
else:
    print "The file does not contain any people."
"""

