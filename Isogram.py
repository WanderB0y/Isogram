# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    string = list(string)

    for i in range(len(string)):
        for j in range(len(string)):
           print(string[i], string[j])
           if i != j:
               return string[i].casefold() == string[j].casefold()
    return True

print(is_isogram("Nelson"))
print(is_isogram("Nena"))