import collections
BOARD_COLUMNS = 9
BOARD_ROWS = 8
NONE = ' '
RED = 'R'
YELLOW = 'Y'

ConnectFourGameState = collections.namedtuple(
    'ConnectFourGameState', ['board', 'turn'])

def new_game_state():
    '''Returns a ConnectFourGameState representing a brand new game
    in which no moves have been made yet.'''
    return (ConnectFourGameState(board=_new_game_board(), turn=RED))

def _new_game_board():
    '''Creates a new game board.  Initially, a game board has the size
    BOARD_COLUMNS x BOARD_ROWS and is comprised only of strings with the
    value NONE'''
    board = []

    for col in range(BOARD_COLUMNS):
        board.append([])
        for row in range(BOARD_ROWS):
            board[-1].append(NONE)

    return board
new_game_state()

def board(state):
    
    for i in range(len(state.board)):
        for a in state.board:
            
        print(state.board[i])

board(new_game_state())
"""
def print_board(board:list):
    number=''
    for i in range(len(board)):
        number+=str(i)+'  '
    print(number)
    
    for num in range(len(board)-1):
        result=''
        for lst in board:
            if lst[num] == ' ':
                result+='.  '
            else:
                result+=lst[num]+'  '
        print(result)



def display_board(gamestate):
    print('0  1  2  3  4  5  6  7  8')
    display_list = []
    for row in gamestate:
        sub_list = []
        for col in row:
            if col == ' ':
                sub_list.append('.')
            else:
                sub_list.append(col)
        display_list.append(sub_list)
    for a in ['A','B','C','D','E','F','G','H']:
        
        for i in range(0,8):
            print('{}  {}  {}  {}  {}  {}  {}  {}  {}'.format(display_list[0][a],
                                          display_list[1][i],
                                          display_list[2][i],
                                          display_list[3][i],
                                          display_list[4][i],
                                          display_list[5][i],
                                          display_list[6][i],
                                          display_list[7][i],
                                          display_list[8][i],))
        
display_board(((new_game_state().board)))

"""
