import re
file = open('numbers.txt')
read = file.read()
num_list = list()
refined_num_list = list()
words = read.split()
number_of_words = 0
for word in words:
    word = word.rstrip('/t')
    number = re.findall('[0-9]+', word)
    if len(number) > 0:
        for i in range(len(number)):
            num = int(number[i])
            refined_num_list.append(num)
    else:
        number_of_words = number_of_words + 1
print(sum(refined_num_list))
print(number_of_words)


#for word in words:
#    word = word.rstrip('/t')  # make words out of text
#    numbers = re.findall('[0-9]+', word)  # from list word finds only numbers.
#    if len(numbers) < 1:  # if not number then it is just and empty under index, which contains word and not number
#        continue
#    for i in range(len(numbers)):  # for each element in numbers
#        num = int(numbers[i])  # make the integer out of each value in the list
#        num_list.append(num)  # add the number in the list
#print(sum(num_list))
