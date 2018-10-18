import re
pattern = "Visa"
regexp = re.compile(pattern, re.IGNORECASE)
file = open("news.txt")
print("Open the file: " + file.name + " ....\n")
count = 0
lineCount = 0
for line in file:
    lineCount += 1
    print("\n" + str(lineCount) + ": " + line)
    match = regexp.search(line)
    if match:
        print("Matched ------")
        print(line)
        print("-------------")
        count += 1

print("\nTotal number of lines = " + str(lineCount))
print("\nTotal number of matched lines having the word = " + str(count))

print("\nAll substrings that match are:")

file.seek(0,0) # reposition to the beginning of the file

count = 0
for line in file:
    x = regexp.findall(line)
    count += len(x)
    print(x)
file.close()

print("\nTotal number of the matchd words is = " + str(count))
