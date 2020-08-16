# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the
# messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# The main logic is to split the file into lines --> words --> hours
# Create a dictionary with hours and its count
# From the dictionary create the list of tuples
# From the list of tuples print the key and value of each tuple

email_file = open('mbox-short.txt', 'r')
opened = email_file.read()
split_by_lines = opened.splitlines()
counts = dict()
for line in split_by_lines:
    if line.startswith("From "):
        words_in_line = line.split()
        full_time = words_in_line[5]
        hour = full_time.split(':')
#  Higher 3 lines could be just as -->
#        hour = line.split()[5].split(":")
# create a dictionary of hours and its counts. if the key, which hour is missing, then add new hour to the dict
        counts[hour[0]] = counts.get(hour[0], 0) + 1
#  comment --> print sorted( [ (v,k) for k,v in counts.items()] )
group_by_hour = list()
for hour, number_of_email_in_hour in counts.items():  # split the dictionary into tuples
    group_by_hour.append((hour, number_of_email_in_hour))  # create a list of tuples
print(group_by_hour)
group_by_hour.sort()
for hour, number_of_email_in_hour in group_by_hour:  # print each element in the list
    print(hour, number_of_email_in_hour)
#  Another way to show the list of sorted tuples by value is the line below
#lists = sorted([(hours, number_of_email_in_hour) for hours, number_of_email_in_hour in counts.items()])
#for i, k in lists:  # print the key and value of each tuple, which the element in the list
#    print(i, k)
