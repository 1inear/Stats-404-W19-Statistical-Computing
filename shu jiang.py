import random

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def exitthegame(theBoard):
    if theBoard['top-L'] == 'X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X':
        return True
    if theBoard['mid-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['mid-R'] == 'X':
        return True
    if theBoard['low-L'] == 'X' and theBoard['low-M'] == 'X' and theBoard['low-R'] == 'X':
        return True
    if theBoard['top-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-R'] == 'X':
        return True
    if theBoard['low-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['top-R'] == 'X':
        return True
    if theBoard['top-L'] == 'X' and theBoard['mid-L'] == 'X' and theBoard['low-L'] == 'X':
        return True
    if theBoard['top-M'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-M'] == 'X':
        return True
    if theBoard['top-R'] == 'X' and theBoard['mid-R'] == 'X' and theBoard['low-R'] == 'X':
        return True




def tictactoe():
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    play = list(theBoard.keys())
    # print(play)
    random.shuffle(play)
    # print(play)

    turn = 'X'
    for k in range(9):
        printBoard(theBoard)
        # print('Turn for ' + turn + '. Move on which space?')
        print('\n')
        theBoard[play[k]] = turn

        if exitthegame(theBoard):
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    printBoard(theBoard)


if __name__ == "__main__":
    tictactoe()












