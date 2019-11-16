import re

sample_file = open('A.2.2 - regex text data.txt')

text = sample_file.read() #With read, we read the entire text and not line by line
number_regex = '[0-9]+'
numbers = re.findall(number_regex, text) #Match any combination of one or more digits

total = sum(int(num) for num in numbers)

print(total)
sample_file.close()
