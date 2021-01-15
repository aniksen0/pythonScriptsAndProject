import csv
name = input('Enter file: ')
handle = open(name, 'r')
wordlist = list()
for line in handle:
    words = line.split()
    for word in words:
        if word in wordlist: continue
        wordlist.append(word)
        with open("list.csv","w",newline='') as file:
            writer=csv.writer(file)
            writer.writerows(word)

wordlist.sort()
print(wordlist)
with open("list.csv","w",newline='') as file:
    writer=csv.writer(file)
    writer.writerows(wordlist)
