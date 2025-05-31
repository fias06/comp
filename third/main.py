#Write you code here-

import random

#Constants
EASY = 0.1  # 10% of cells are mines
MEDIUM = 0.15  # 15% of cells are mines
HARD = 0.2  # 20% of cells are mines

MINE = -1  # A mine on the board
FLAG = '\u2691'  # Unicode flag
UNREVEALED = '?'  # Hidden cell

REVEAL = 0
PLACE_FLAG = 1

#------------------ PART-1 ---------------------
def init_board(nb_rows, nb_cols, value):
    """
    this function takes in the number of rows/columns and
    the value to be inserted and then generates a nested
    list following the given details
    
    
    Examples:
    1) 
    >>> init_board(3,3,0)
    returns [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    2) 
    >>> init_board(5,1,2)
    returns [[2], [2], [2], [2], [2]]
    
    3) 
    >>> init_board(2,3,4)
    returns [[4, 4, 4], [4, 4, 4]]
    """
    
    board = []
    
    for _ in range(nb_rows):  # Corrected the loop to iterate `nb_rows` times
        row = [value] * nb_cols  # Create a row with `nb_cols` elements
        board.append(row)  # Append the row to the board
    
    return board


def count_total(board, value):
    """
    this function counts the number of time a spefific value
    occurs in the board using nested loops
    
    Examples:
    1) 
    >>> count_total([['?','4','?'], ['2','?','?']],'?')
    returns 4
    
    2) 
    >>> count_total([['2','4','1'], ['2','4','22'], ['2','4','6']],'2')
    returns 3
    
    3) 
    >>> count_total([['2','4','6']],'5')
    returns 0
    """
    
    count = 0 #variable keeps track of occurance
    
    for i in board:
        for j in i: #two for loops for nested lists
            if j == value:
                count+=1 #if the value is equal, count increases
    return count


def is_valid_position(board, row, col):
    """ 
    this function checks if the given coordinates actually exist
    in the board or not
    
    Examples:
    for board = init_board(4,5,1)
    
    1) 
    >>> is_valid_position(board,0,0)
    returns True
    
    2) 
    >>> is_valid_position(board,-3,2)
    returns Falso
    
    3) 
    >>> is_valid_position(board,4,5)
    returns False

    """
    #checks position of row/col
    row_count, col_count = len(board), len(board[0]) 
    
    if 0<= row <row_count and 0<= col <col_count: #main condition
        return True
    else:
        return False
    
def get_neighbour_positions(board, row, col):
    """ 
    this function gives the positions of the neighbouring
    elements if they exist
    
    Examples:
    if board = init_board(3,4,0) 
    1) 
    >>> get_neighbour_positions(board,1,2)
    returns [[0, 1],[0, 2],[0, 3],[1, 1],[1, 3],[2, 1],[2, 2],[2, 3]]
    
    2) 
    >>> get_neighbour_positions(board,0,0)
    returns [[0, 1], [1, 0], [1, 1]]
    
    3) 
    get_neighbour_positions(board, 2,3)
    returns [[1, 2], [1, 3], [2, 2]]

    """
    
    neighbours = []
    for i in [-1,0,1]: #for the nieghbouring positions
        for j in [-1,0,1]:
            if not(i==0 and j==0):
                new_row = row+i #gives new row pos
                new_col = col+j #gives new col pos
                
                #checks if position actually exists
                if is_valid_position(board, new_row, new_col) == True: 
                    neighbours.append([new_row,new_col]) #adds to a list
    return neighbours


def count_neighbours(board, row, col, value):
    """
    this function uses the prev function to find the neighbouring
    lists and finds if their value is equal to the one given
    
    Examples:
    if board = [[1, 1, 0, 0], [-1, 2, 1, 1], [1, 3, -1, 2], \
        [0, 2, -1, 2]]

    1)
    >>> count_neighbours(board, 2, 1, -1)
    returns 3
    
    2) 
    >>> count_neighbours(board, 0, 0, 2)
    returns 1
    
    3)
    >>> count_neighbours(board, 3, 1, 1)
    returns 1
    """
    
    
    neighbours = get_neighbour_positions(board, row, col)
    
    count = 0
    #if the value is equal to the one given, the count incrases\
     #   showing the no of times a specific value occurs
    for r, c in neighbours:
        if board[r][c]==value:
            count += 1 
    return count



#------------------ PART-2 ---------------------

def new_mine_position(board):
    """
    This function chooses two random numbers as thr row 
    and column and continues the same until the value is -1
    
    

    Example:
    random.seed(202) 

    1)
    >>> new_mine_position([[0, 1, 1], [0, 1, -1], [0, 1, 1]])
    returns (1,1)
    
    2)
    >>> new_mine_position([[0, 0, 0], [0, 1, 1], [0, 1, 1]])
    returns (1,2)
    
    3)
    >>> new_mine_position([[-1, 0, 0], [0, 1, 1], [0, 1, 1],\
        [2,1,0]])
    (3,2)
    
    """
    
    row_count, col_count = len(board), len(board[0]) #for row/col pos
    
    #generates random numbers in range
    rowno, colno = random.randint(0,row_count -1), \
        random.randint(0,col_count-1)
    
    while board[rowno][colno] == -1:
        rowno, colno = random.randint(0,row_count -1), \
            random.randint(0,col_count-1)
    return rowno,colno

def new_mine(board):
    """ 
    this function sets the position of the random row/col = -1
    and increases the value of the surrounding number by +1 to
    show that there is an extra mine nearby
    
    Examples:
    >>> random.seed(202)
    >>> board = init_board([4,4,0])
    >>> board
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    >>> new_mine(board)
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]]
    
    >>> new_mine(board)
    [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 2, 1], [1, -1, 2, -1]]
    
    >>> new_mine(board)
    [[0, 0, 1, 1], [0, 0, 1, -1], [1, 1, 3, 2], [1, -1, 2, -1]]
    
    """

    rowno,colno = new_mine_position(board)
    
    #changes the value to -1
    board[rowno][colno] = -1

    neighbours = get_neighbour_positions(board, rowno, colno)
    
    #increases the value of nearby by +1
    for a, b in neighbours:
        if board[a][b] != -1:
            board[a][b] +=1 
    return None

def generate_helper_board(nb_rows, nb_cols, nb_mines):
    """
    this function adds new mines equal to the nb_mines given 
    and it increases the value of the number surrouding
    
    Examples:
    1)
    >>> generate_helper_board(5,5,7)
    [[0, 0, 2, -1, 2], [0, 0, 2, -1, 2], [1, 1, 3, 2, 2], \
        [1, -1, 2, -1, 1], [1, 1, 2, 1, 1]]
    
    2)
    >>> generate_helper_board(3,4,6)
    [[1, 1, 3, -1], [1, -1, 3, -1], [1, 1, 2, 1]]
    
    3) 
    >>> generate_helper_board(5,3,7)
    [[1, 1, 0], [-1, 1, 0], [3, 4, 2], [-1, -1, -1], [2, 3, 2]]
    """
    """board = init_board(nb_rows, nb_cols, 0)

    count = 0
    while count < nb_mines:
        new_mine(board)
        for i in board:
            for j in i:
                if j== -1:
                    count+=1
    return board"""
    
    
    board = init_board(nb_rows, nb_cols, 0)

    count = 0
    while count < nb_mines:
        prev_board = [row[:] for row in board]  # Create a copy to check changes
        new_mine(board)
        
        # Only increment count if a new mine was actually added
        if board != prev_board:
            count += 1

    return board

    

#------------------ PART-3 -------------------

def flag(board, row, col):
    """
    this function replaces ? with a flag or vice
    versa in the board
    
    Examples:
    1)
    >>> board = [[1,2,0,1],[1,"?","?",2],[0,1,0,0]]
    >>> flag(board, 1,1)
    >>> print(board)
    [[1, 2, 0, 1], [1, '⚑', '?', 2], [0, 1, 0, 0]]
    
    2)
    >>> board = [['⚑',0,1],[1,0,"?",2],[1,1,0,4]]
    >>> flag(board, 0,0)
    >>> print(board)
    [['?', 0, 1], [1, 0, '?', 2], [1, 1, 0, 4]]
    
    3) 
    >>> board = [['⚑',0,0],[1,0,"?",2],[1,"?",0,0]]
    >>> flag(board, 2,1)
    >>> print(board)
    [['⚑', 0, 0], [1, 0, '?', 2], [1, '⚑', 0, 0]]
    
    
    """
    # Unicode character for the flag
    FLAG = '\u2691'

    # Check if the cell is already revealed (a number), then do nothing
    if isinstance(board[row][col], int):
        return  

    # If cell is '?', place a flag
    if board[row][col] == '?':
        board[row][col] = FLAG
    
    # If cell is already a flag, revert back to '?'
    elif board[row][col] == FLAG:
        board[row][col] = '?'


def reveal(helper_board, game_board, row, col):
    """
    this function checks if the value is -1 (game breaks)
    or else  the number is subsitited with the str form
    
    Examples:
    >>> helper_board = [[2, -1, 1], [-1, 4, 3], [2, -1, -1]]
    1) 
    >>> game_board = init_board(3, 3,'?')
    >>> print(game_board)
    [['?', '?', '?'], ['?', '?', '?'], ['?', '?', '?']]
    
    2)
    >>> reveal(helper_board, game_board, 3, 0)
    [['?', '?', '?'], ['?', '?', '?'], ['2', '?', '?']]
    
    3)
    >>> reveal(helper_board, game_board, 0, 1)
    Traceback (most recent call last):
    File "/Users/saifshaikh/Desktop/comp 202/Assignment \
        3/trial.py", line 326, in <module>
        reveal(helper_board, game_board, 0, 1)
    File "/Users/saifshaikh/Desktop/comp 202/Assignment \
        3/trial.py", line 319, in reveal
        raise AssertionError("BOOM! You lost.") #raises error
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError: BOOM! You lost.

    """
    if helper_board[row][col] == -1:
        raise AssertionError('BOOM! You lost.') #raises error
    else:
        game_board[row][col] = str(helper_board[row][col])
    return None

def print_board(board):
    """
    This function displays the board in a proper
    organized manner
    
    Examples:
    1)
    >>> board = [list('002\u2691?'), list('113\u2691?'),\
        list('??4??'), list('?'*5), list('?'*5)]
    0 0 2 ⚑ ?
    1 1 3 ⚑ ?
    ? ? 4 ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    
    2) 
    >>> board = [list('-101\u2691'), list('1?3\u2691?'), \
        list('??\u2691\u2691?'), list('?22??'), list('?1?23')]
    1 2 0 1 ⚑
    1 ? 3 ⚑ ?
    ? ? ⚑ ⚑ ?
    ? 2 ? ? ?
    ? 1 2 ? 3
        
        
    3)
    >>> board = [list('\u2691201\u2691'), list('1\u2691\u2691\u2691?'), \
        list('??\u2691?1'), list('?2??\u2691'), list('?12?3')]
    ⚑ 2 0 1 ⚑
    1 ⚑ ⚑ ⚑ ?
    ? ? ⚑ ? 1
    ? 2 ? ? ⚑
    ? 1 2 ? 3
    
    
    """
    #for row in board:
     #   print(" ".join("⚑" if cell == -1 else str(cell) for cell in row))
    for row in board:
        print(" ".join(row))



#------------------ PART-4 -------------------

def play():
    """
    this function runs all the above condition allowing the user
    to rplay the game. if firstly gives an option of difficulty which 
    determines the number of mines
    
    Examples:
    random.seed(202)
    1)
    Enter the number of rows for the board: 3
    Enter the number of columns for the board:3
    Choose a difficulty from [EASY, MEDIUM, HARD]: EASY
    Current board: ( 1 remaining)
    ? ? ?
    ? ? ?
    ? ? ?
    Choose 0 to reveal or 1 to flag: 0
    Which row? 0
    Which column? 0
    Current board:
    0 ? ?
    ? ? ?
    ? ? ?
    Choose 0 to reveal or 1 to flag: 0
    Which row? 1
    Which column? 1
    Current board:
    0 ? ?
    ? 1 ?
    ? ? ?
    Choose 0 to reveal or 1 to flag: 0
    Which row? 2
    Which column? 2
    Current board:
    0 ? ?
    ? 1 ?
    ? ? 1
    Choose 0 to reveal or 1 to flag: 1
    Which row? 1
    Which column? 2
    Current board:
    0 ? ?
    ? 1 ⚑
    ? ? 1
    Congrats! You won!
    

    2) 
    Enter the number of rows for the board: 3
    Enter the number of columns for the board:3
    Choose a difficulty from [EASY, MEDIUM, HARD]: EASY
    Current board: ( 1 remaining)
    ? ? ?
    ? ? ?
    ? ? ?
    Choose 0 to reveal or 1 to flag: 0
    Which row? 1
    Which column? 2
    Traceback (most recent call last):
    File "/Users/saifshaikh/Desktop/comp 202/Assignment 3/
        main.py", line 506, in <module>
        play()
    File "/Users/saifshaikh/Desktop/comp 202/Assignment 3/
        main.py", line 482, in play
        reveal(helper_board, game_board, chosen_row, chosen_col)
    File "/Users/saifshaikh/Desktop/comp 202/Assignment 3/m 
        ain.py", line 355, in reveal
        raise AssertionError("BOOM! You lost.") #raises error
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError: BOOM! You lost.
    

    3)
    Enter the number of rows for the board: 3
    Enter the number of columns for the board:3
    Choose a difficulty from [EASY, MEDIUM, HARD]: EASY
    Current board: ( 1 remaining)
    ? ? ?
    ? ? ?
    ? ? ?
    Choose 0 to reveal or 1 to flag: 1
    Which row? 1
    Which column? 2
    Current board:
    ? ? ?
    ? ? ⚑
    ? ? ?
    Congrats! You won!
        
    """
    
    #random.seed(202)
    import random

# Constants
EASY = 0.1  # 10% of cells are mines
MEDIUM = 0.15  # 15% of cells are mines
HARD = 0.2  # 20% of cells are mines

MINE = -1  # A mine on the board
FLAG = '\u2691'  # Unicode flag
UNREVEALED = '?'  # Hidden cell

REVEAL = 0
PLACE_FLAG = 1

# ... (rest of your functions: init_board, count_total, is_valid_position, etc.) ...

def play():
    """
    this function runs all the above condition allowing the user
    to rplay the game. if firstly gives an option of difficulty which
    determines the number of mines
    """

    # random.seed(202)
    # asks for no of rows and cols
    nb_rows = int(input("Enter the number of rows for the board: "))
    nb_cols = int(input("Enter the number of columns for the board: "))

    # Difficulty level selection
    diff = input("Choose a difficulty from [EASY, MEDIUM, HARD]: ")

    # Sets the number of mines based on difficulty
    if diff == "EASY":
        nb_mines = int(0.10 * (nb_rows * nb_cols))
    elif diff == "MEDIUM":
        nb_mines = int(0.30 * (nb_rows * nb_cols))
    elif diff == "HARD":
        nb_mines = int(0.50 * (nb_rows * nb_cols))

    # Initialize boards
    helper_board = generate_helper_board(nb_rows, nb_cols, nb_mines)
    game_board = init_board(nb_rows, nb_cols, "?")

    # Initial board display
    print("Current Board: (" + str(nb_mines) + " mines remaining)")
    print_board(game_board)

    revealed_cells = 0
    total_cells = nb_rows * nb_cols
    safe_cells = total_cells - nb_mines
    flagged_mines = 0

    while revealed_cells < safe_cells:
        flag_dec = int(input("Choose 0 to reveal or 1 to flag: "))
        chosen_row = int(input("Which row? "))
        chosen_col = int(input("Which column? "))

        if flag_dec == 0:
            if helper_board[chosen_row][chosen_col] == -1:
                reveal(helper_board, game_board, chosen_row, chosen_col)
                return  # Game over (lost)
            elif game_board[chosen_row][chosen_col] == "?":
                reveal(helper_board, game_board, chosen_row, chosen_col)
                revealed_cells += 1

        elif flag_dec == 1:
            if game_board[chosen_row][chosen_col] == "?":
                flag(game_board, chosen_row, chosen_col)
                if helper_board[chosen_row][chosen_col] == -1:
                    flagged_mines += 1
            elif game_board[chosen_row][chosen_col] == FLAG:
                flag(game_board, chosen_row, chosen_col)
                if helper_board[chosen_row][chosen_col] == -1:
                    flagged_mines -= 1

        # If the player has revealed all safe cells, they win
        if revealed_cells == safe_cells:
            print("Congratulations! You won!")

            # Reveal the full board correctly before exiting
            for i in range(len(game_board)):
                for j in range(len(game_board[0])):
                    if game_board[i][j] == "?":
                        if helper_board[i][j] == -1:
                            game_board[i][j] = FLAG  # Display mine as flag after winning
                        else:
                            game_board[i][j] = str(helper_board[i][j])

            print("Final Board:")
            print_board(game_board)
            return  # Exit after printing the final board

        # Print board update only if the game is still running
        print("Current Board: (" + str(nb_mines - flagged_mines) + " mines remaining)")
        print_board(game_board)
#play()
#------------------ PART-5 -------------------


def solve_cell(board, row, col, left_click, right_click):
    """ 
    this function helps in solving the game by itself my setting
    certain conditions and giving the neighbouring items (whether 
    it is a flag/mine/unknown etc)
    """

    #condition if chosen cell is flag or ?
    if board[row][col] == "\u2691" or board[row][col] == "?":
        return

    if board[row][col] in ["?", "\u2691"]:
        return
    
    #gets all the neighbours
    adj_neigh = get_neighbour_positions(board, row, col)
    
    #checks which of the neigbour is a flag
    adj_flag = count_neighbours(board, row, col, "\u2691")
    
    #takes theh total mines near the cell
    adj_mines = int(board[row][col])

    reveal_neigh = 0
    for i, j in adj_neigh:
        if board[i][j] not in ["?", "\u2691"]:  
            reveal_neigh += 1 #which cells are unflagged

    #cells which are not mines (all - flagged ones)
    non_mines = len(adj_neigh) - adj_mines

    if adj_flag == adj_mines:
        for a, b in adj_neigh:
            if board[a][b] == "?":
                left_click(a, b)
    elif reveal_neigh == non_mines:
        for c, d in adj_neigh:
            if board[c][d] == "?":
                right_click(c, d)


def solve(board, left_click, right_click):
    """ 
    this is calls the previous function with a condition
    """
    while any('?' in row for row in board):  
        for row in range(len(board)):
            for col in range(len(board[0])):
                #calls the functions
                solve_cell(board, row, col, left_click, right_click)

    

def test_bot(helper_board, game_board):
    """ 
    this function call the above two functions to use them 
    depending on the situation. it also declares lefft_click
    and right_click functions and solves the game automatically
    
    Example:
    Current Board:
    1 ? ? ? ?
    1 1 ? ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ ? ? ?
    1 1 ? ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ ? ? ?
    1 1 ? ? ?
    1 ? ? ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ ? ? ?
    1 1 ? ? ?
    1 2 ? ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 ? ?
    1 1 ? ? ?
    1 2 ? ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 ? ?
    1 1 1 ? ?
    1 2 ? ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 ? ?
    1 1 1 ? ?
    1 2 3 ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 1 ?
    1 1 1 ? ?
    1 2 3 ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 1 ?
    1 1 1 2 ?
    1 2 3 ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 1 ?
    1 1 1 2 ?
    1 2 3 5 ?
    ? ? ? ? ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 1 ?
    1 1 1 2 ?
    1 2 3 5 ?
    ? ⚑ ? ? ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 1 ?
    1 1 1 2 ?
    1 2 3 5 ?
    ? ⚑ ⚑ ? ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 1 ?
    1 1 1 2 ?
    1 2 3 5 ?
    ? ⚑ ⚑ ⚑ ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 1 ?
    1 1 1 2 ⚑
    1 2 3 5 ?
    ? ⚑ ⚑ ⚑ ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 1 ?
    1 1 1 2 ⚑
    1 2 3 5 ⚑
    ? ⚑ ⚑ ⚑ ?
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 1 ?
    1 1 1 2 ⚑
    1 2 3 5 ⚑
    ? ⚑ ⚑ ⚑ ⚑
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 1 1
    1 1 1 2 ⚑
    1 2 3 5 ⚑
    ? ⚑ ⚑ ⚑ ⚑
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 1 1
    1 1 1 2 ⚑
    1 2 3 5 ⚑
    1 ⚑ ⚑ ⚑ ⚑
    ? ? ? ? ?
    Current Board:
    1 ⚑ 1 1 1
    1 1 1 2 ⚑
    1 2 3 5 ⚑
    1 ⚑ ⚑ ⚑ ⚑
    1 ? ? ? ?
    Current Board:
    1 ⚑ 1 1 1
    1 1 1 2 ⚑
    1 2 3 5 ⚑
    1 ⚑ ⚑ ⚑ ⚑
    1 2 ? ? ?
    Current Board:
    1 ⚑ 1 1 1
    1 1 1 2 ⚑
    1 2 3 5 ⚑
    1 ⚑ ⚑ ⚑ ⚑
    1 2 3 ? ?
    Current Board:
    1 ⚑ 1 1 1
    1 1 1 2 ⚑
    1 2 3 5 ⚑
    1 ⚑ ⚑ ⚑ ⚑
    1 2 3 3 ?
    Current Board:
    1 ⚑ 1 1 1
    1 1 1 2 ⚑
    1 2 3 5 ⚑
    1 ⚑ ⚑ ⚑ ⚑
    1 2 3 3 2
    Congratulations! You won!
    """
    total_mines = count_total(helper_board, -1)
    private_board = [] #cheat prevention
    for row in game_board: #deep copy
        tmp = []
        for value in row:
            tmp.append(value)
        private_board.append(tmp)
        
    def left_click(row, col):
        #tip: consider raising an error here if (row, col) is not a valid cell
        reveal(helper_board, private_board, row, col) #for verification
        reveal(helper_board, game_board, row, col) #for the bot
        print('Current Board:')
        print_board(game_board)
        
    def right_click(row, col):
        #tip: consider raising an error here if (row, col) is not a valid cell
        flag(private_board, row, col) #for verification
        flag(game_board, row, col) #for the bot
        print('Current Board:')
        print_board(game_board)
    
    print('Current Board:')
    print_board(game_board)
    solve(game_board, left_click, right_click)
    
    if count_total(private_board, '?') == 0 and \
       count_total(private_board, '⚑') == total_mines:
        #IMPORTANT: in play(), we do not need all mines to be flagged to win,
        #but we do when testing the bot,
        #so you will need to modify this condition for play()
        print('Congratulations! You won!')
    else:
        print('Bad Bot :(')
        
BOT_TEST_1 = [[[1, -1, 1, 1, 1],
               [1, 1, 1, 2, -1],
               [1, 2, 3, 5, -1],
               [1, -1, -1, -1, -1],
               [1, 2, 3, 3, 2]],
              [['1', '?', '?', '?', '?'],
               ['1', '1', '?', '?', '?'],
               ['?', '?', '?', '?', '?'],
               ['?', '?', '?', '?', '?'],
               ['?', '?', '?', '?', '?']]]

#test_bot(BOT_TEST_1[0], BOT_TEST_1[1])
    
    
    
        