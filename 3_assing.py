#name = input('text.txt')
handle = open ('text.txt', 'r')

counts = dict()
for space in handle:
    words = space.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


quit()
quit()
x=2

