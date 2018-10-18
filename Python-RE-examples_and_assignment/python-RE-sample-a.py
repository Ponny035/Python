import re
pattern = "[a-zA-Z]red"
regexp = re.compile(pattern, re.IGNORECASE)
file = open("names.txt")
print("Open the file " + file.name + " ...\n")

print("Match(es) is/are:\n")
count = 0
for line in file:
    match = regexp.search(line)
    if match:
        count += 1
        print(line, end ="")

print("\n\nTotal matched lines = ",count)
print("All substrings that match are:")
file.seek(0,0) # reposition to the beginning of the file

for line in file:
    x = regexp.findall(line)
    print(x)

file.close()
