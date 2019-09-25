#%%
def factorial(n):
    if (n > 1):
        for i in range(n):
           return n * factorial(n-1)
    else:
        return n
            
factorial(4)
    