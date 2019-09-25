def findinlist(x, list_input):
    for i in range(len(list_input)):
        if (x == list_input[i]):
            return i
def countletter(string):
    a = []
    b = []
    for i in string:
        if i not in a:
            a.append(i)
            b.append(1)
        else:
            x = findinlist(i,a)
            b[x] += 1
    for i in range(len(a)):
        print(a[i], " = ", b[i])
        
string = input("Enter string: ")
string = countletter(string)
#%%