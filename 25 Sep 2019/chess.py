#%%
num = [8,7,6,5,4,3,2,1]
alpha = ['A','B','C','D','E','F','G','H']
board_pos = [alpha,num]
board = [['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-']]

def board_display():
    for i in range(len(board)):
        print(" ".join(board[i]))
    
board_display()
def knight_moves():
    position_input = str(input("Enter position: "))
    if (len(position_input) == 2):
        post_list = list(position_input)
        y = post_list[0]
        x = post_list[1]
        y = board_pos[0].index(str(y.upper()))
        x = board_pos[1].index(int(x))
    else:
        print("Invalid input. Try again.")
        board_display()
        knight_moves()
        
    moves = [[x + 1, y + 2], [x - 1, y + 2], [x + 2, y + 1], [x + 2, y - 1],
             [x + 1, y - 2], [x - 1, y - 2], [x - 2, y + 1], [x - 2, y + 1]]
    board[x][y] = "o"
    for i, j in moves:
        try:
            board[i][j] = "*"
            
            board_display()
            knight_moves()
        except:
            continue
    
knight_moves()
#%%