# Use the file name mbox-short.txt as the file name
filename = input("Enter file name: ")
filehandle = open(filename)
count = 0
totalconfidence = 0
for line in filehandle:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    if line.startswith("X-DSPAM-Confidence:") :
        confidence = line[19:]
        count = count + 1
        totalconfidence = float(totalconfidence) + float(confidence)
avgconfidence = totalconfidence / count
print("Average spam confidence:", float(avgconfidence))
# print(count)


