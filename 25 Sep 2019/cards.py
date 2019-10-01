#%%
from random import randint
def cards():
    shape = ["Spade","Heart","Diamond","Club"]
    numbers = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    card_list = [shape,numbers]
    for i in card_list[0]:
        for j in card_list[1]:
            print(card_list[0][randint(0,3)],card_list[1][randint(0,12)])
            
cards()