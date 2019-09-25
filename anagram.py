#%%
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

List1 = list(s1)
List2 = list(s2)
if (len(s2) != len(s1)):
    print("They are not anagrams.")
    
else:
    for i in s1:
        if (i in List1 and i in List2):
            List1.remove(i)
            List2.remove(i)
            anagram = True
        else:
            anagram = False
    
if (anagram == True):
    print("They are anagrams.")
else:
    (anagram == False)
    print("They are not anagrams.")
#%%
