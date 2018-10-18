import re

pattern = "(?:aa|b)*ab(?:bb)*"
r = re.compile(pattern)
flag = True
while(flag):
    print("Here is the pattern we are looking for: ", "(aa|b)*ab(bb)*")
    txt = input("Enter a string for a pattern matching: ")
    x = r.findall(txt)
    print("Matched substring(s) is/are")
    print(x)
    while(True):
        answer = input("Continue? (y/n): ")
        if(answer == 'n' or answer == 'N'):
            flag = False
            break
        elif(answer == 'y' or answer == 'Y'):
            break
