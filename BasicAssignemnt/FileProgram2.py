infile = open("fileprog2.txt",'r')

text=infile.readline()
print text
lines = 1
words = 1
characters = 1
for line in infile:
    print line
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    characters = characters + len(line)

print(lines)
print(words)
print(characters)