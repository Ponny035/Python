import re
r = re.compile("r[ea]d") # character class in a square bracket
x = r.findall("read rad rattle red")
print(x)

r = re.compile("[0-9]") # any of the digit
x = r.findall("02-470-9892")
print(x)

r = re.compile("[^0-9]") # negation of the above; non-digit
x = r.findall("02-470-9892")
print(x)

r = re.compile("\d") # any of the digit; or use [\d]
x = r.findall("02-470-9892")
print(x)

r = re.compile(".") # match anything except newlines
x = r.findall("BKK-470-9892")
print(x)

r = re.compile("[a-i]") # from a to i
x = r.findall("Let's start it over.")
print(x)

r = re.compile("\w")  # any alphanumeric character plus underscore; or use [\w]
x = r.findall("Let's start it over_.")
print(x)

r = re.compile("[a-zA-Z0-9_]") # same as [\w]
x = r.findall("Let's start it over_.")
print(x)

r = re.compile("e{1,3}") # quantifier; min = 1 to max = 3
x = r.findall("Eel... don't reel out and kneel ... eeeew")
print(x)

r = re.compile("e{2}") # quantifier; min = 2 to max = 2
x = r.findall("Eel... don't reel out and kneel ... eeeew")
print(x)

r = re.compile("travel{1,2}ed") # quantifier;
x = r.findall("Travel ... travelled  .... traveled .. travellllledd")
print(x)

print()
print("{0,1}")
r = re.compile("travell?ed") # {0,1}
x = r.findall("Travel ... travelled  .... traveled .. travellllledd")
print(x)

print()
print("{0,n}")
r = re.compile("travell*ed") # {0,n}
x = r.findall("Travel ... travelled  .... traveled .. travellllledd")
print(x)

print()
print("{1,n}")
r = re.compile("travell+ed") # {1,n}
x = r.findall("Travel ... travelled  .... traveled .. travellllledd")
print(x)

print()
print("{1,n}")
r = re.compile("\d+") # {1,n}
x = r.findall("432.59e4")
print(x)

# Parentheses have two uses:
# - grouping expressions
# - capturing the texts that match an expression

r = re.compile("travel(?:ed)*") # Using (?: to switch off captures
x = r.findall("Travel ... travelled  .... traveled .. travellllledd")
print(x)

r = re.compile("trav(eled)") # Parentheses are used for captures
x = r.findall("Traveled ... traveleddd  ..trs.. traveled .. travellllledd")
print(x)

r = re.compile("(?:t|T)ravel") # | is used for selection; logical OR
x = r.findall("Travel ... travelled  .... traveled .. travellllledd")
print(x)


print()
txt = "\w+ = .+"  # "." matches any character except a newline
r = re.compile(txt)
myAreaCode = [ "BKK = 02", "Suphanburi = 035", "Chiang Mai = 053"]
for i in myAreaCode:
    x = r.findall(i)
    print(x)

print()
txt = "(\w+) = (.+)"  # Captures
r = re.compile(txt)
myAreaCode = [ "BKK = 02", "Suphanburi = 035", "Chiang Mai = 053"]
for i in myAreaCode:
    x = r.findall(i)
    print(x)

print()
txt = "(?:\w+(?: )?\w+) = .+"  # Handle a space
r = re.compile(txt)
myAreaCode = [ "BKK = 02", "Suphanburi = 035", "Chiang Mai = 053"]
for i in myAreaCode:
    x = r.findall(i)
    print(x)


print()
txt = "aircraft|airplane|jet"
r = re.compile(txt)
# Split the string into a list, splitting it wherever there are matches
m = r.split("a jet ski or aircraft is not a jet airplane or jetliner")
print(m)

# Find all substrings where there are matches,
# and replace them with a different string
print()
m = r.sub("air", "a jet ski is not a jet plane or jetliner")
print(m)
