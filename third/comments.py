# if board[row][col] is a flag or a ?, return 
    
if board[row][col] == "\u2691" or "?":
    return

# count the number of mines relative to row col



# list the neighbor positions relative to row,col

total_mines = get_neighbour_positions(board, row, col)

# count the number of flags relative to row,col

neig_pos = count_neighbours(board, row, col, "\u2691")

# check if flag count equals mine count, then left click if its ?

# check how many cells have not been flagged, if unknown + flags equals mine count, then right click
