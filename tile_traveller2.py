# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row ):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        # if onetwo_count:
        #     coins_amount = coins(coins_amount)
        #     onetwo_count = False
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        # if twotwo_count:
        #     coins_amount = coins(coins_amount)
        #     twotwo_count = False
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        # if twothree_count:
        #     coins_amount = coins(coins_amount)
        #     twothree_count = False
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        # if threetwo_count:
        #     coins_amount = coins(coins_amount)
        #     threetwo_count = False
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def coins(coins_amount,col,row):
    if (col == 1 and row ==2) or (col==2 and row ==2) or (col==2 and row ==3) or (col == 3 and row == 2):
        pull_lever = input('Pull a lever (y/n): ')
        if not pull_lever.lower() in 'yn':
            print('Invalid input')
        
        if pull_lever.lower() == 'y':
            coins_amount = coins_amount + 1
            print('You received 1 coin, your total is now {}.'.format(coins_amount))
        elif pull_lever.lower() == 'n':
            pass
        
    return coins_amount

     
def play_one_move(col, row, valid_directions,coins_amount):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        coins_amount = coins(coins_amount,col,row)
        victory = is_victory(col, row)
    return victory, col, row, coins_amount






# The main program starts here
victory = False
row = 1
col = 1
coins_amount = 0
# onetwo_count = True
# twotwo_count = True
# twothree_count = True
# threetwo_count = True

while not victory:
    valid_directions = find_directions(col, row)
    print_directions(valid_directions)
    victory, col, row,coins_amount = play_one_move(col, row, valid_directions,coins_amount)
print("Victory! Total coins {}.".format(coins_amount))




