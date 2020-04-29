name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
mostrepeatedemail = None
numberemailsent = None
for word, email in counts.items():
    if numberemailsent is None or email > numberemailsent:
        numberemailsent = email
        mostrepeatedemail = word
print(mostrepeatedemail, numberemailsent)
