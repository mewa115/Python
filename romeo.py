x = open("text.txt", "r")

count = 1
for line in x:
    print(line.strip())
    count = count + 1
print(count,"Lines")


