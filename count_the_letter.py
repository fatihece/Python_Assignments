sentence = input("Enter a sentence that you wanna count its characters: ")
chardict = {}
for char in sentence:
    if char not in chardict:
        chardict[char] = 1
    else:
        chardict[char] += 1
print(chardict) 