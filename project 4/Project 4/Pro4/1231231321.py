cloumn0=[' ','A','B','C','D','E','F']
cloumn1=['1',' ',' ',' ',' ',' ',' ']
cloumn2=['2',' ',' ',' ',' ',' ',' ']
cloumn3=['3',' ',' ','B','W',' ',' ']
cloumn4=['4',' ',' ','W','B',' ',' ']
cloumn5=['5',' ',' ',' ',' ',' ',' ']
cloumn6=['6',' ',' ',' ',' ',' ',' ']

def board():
    for i in range(7):
        print('{} | {} | {} | {} | {} | {} | {} |'.format(cloumn0[i],cloumn1[i],cloumn2[i],cloumn3[i],cloumn4[i],cloumn5[i],cloumn6[i]))
board()


def _opposite_turn(turn):
    '''Given the player whose turn it is now, returns the opposite player'''
    if turn == RED:
        return YELLOW
    else:
        return RED
