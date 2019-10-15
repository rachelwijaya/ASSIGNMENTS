#%%
import matplotlib.pyplot as plt
import string

path = "E:/python practice/IndonesiaRaya.txt"
with open(path, 'r') as f:
    content = f.read()   
    string_list = ""
    string_dict = {}
for char in content:
    if char not in string.punctuation:
        string_list += char
string_list = string_list.lower().split()

for word in string_list:
    if word in string_dict:
        string_dict[word] = string_dict[word] + 1
    else:
        string_dict[word] = 1
#convert dictionary to bar chart
count_list = string_dict.values()
fig = plt.figure(dpi = 80, figsize = (16,5))
indentation = list(range(1,len(count_list)+1))
bar_width = 0.85
b1 = plt.barh(sorted(indentation), sorted(count_list), bar_width, facecolor = "purple", alpha = 0.3 )
plt.ylabel("WORDS", fontsize = 12)
plt.yticks(indentation, string_dict.keys())
plt.show()
       
#%%