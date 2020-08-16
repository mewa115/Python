file = 'test1.txt'
file = open(file)
total = 0
count = 0
for line in file:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    index = line.find(':')
    value = line[index+1:]
    value = float(value)
    total = total + value
    count = count + 1
    print(count, value, total)
print(total/count)
#index = line.find(":")
#index = float(index)
#print(index)
# print("Average spam confidence:", avg)