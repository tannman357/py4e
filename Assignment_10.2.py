name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dictionary = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        date = words[5]
        hour = date.split(":")
        hours = hour[0]
        dictionary[hours] = dictionary.get(hours, 0) + 1
list_of_words = list()
for key, value in dictionary.items():
    new_tuple = (key, value)
    list_of_words.append(new_tuple)
list_of_words = sorted(list_of_words)
for key, value in list_of_words:
    print(key, value)
