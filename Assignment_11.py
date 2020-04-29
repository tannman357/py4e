import re
total = 0
with open('regex_realsum.txt', 'r') as file:
    for line in file:
        numbers = re.findall('[0-9]+', line)
        numbers = [int(i) for i in numbers]
        for number in numbers:
            total = int(total) + int(number)
print(total)
