#This program is to simulate the popular game TicTacToe on Python
board = ['-' for x in range(10)]    #Initializing the blank values in the board

print("Welcome")
#Function to make a move in the board by computer/player
def InsertLetter(letter, pos):
    board[pos] = letter

#Function to check if a space is free in the board to make a move
def SpaceIsFree(pos):
    return board[pos] == '-'

#Function to print the board
def PrintBoard(board):
    print(board[1] + board[2] + board[3])
    print(board[4] + board[5] + board[6])
    print(board[7] + board[8] + board[9])

#Function to check if the board is full so that further moves are not possible
def BoardFull(board):
    if(board.count('-') > 1):
        return False
    else:
        return True

#Function to check if we have found a winner based on the position of adjacent similar letters
def IsWinner(board, letter):
    return (
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter)
    )

#Function that will take input from the player and play the move
def PlayerMove():
    run = True
    while run:
        move = input("Please select a position between 1 to 9 to place X")
        try:
            move = (int)(move)
            if(move > 0 and move < 10):
                if(SpaceIsFree(move)):
                    run = False
                    InsertLetter('X', move)
                else:
                    print("Sorry, this place is occupied")
            else:
                print("Please type a number between 1 and 9")
        except:
            print("Please type a number")

#Function that will calculate the computer move
def ComputerMove():
    possibleMoves = [x for x,letter in enumerate(board) if letter == '-' and x != 0]
    move = 0

    for let in ['0','X']:   #Checking whether a move will result in the computer being the winner
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if(IsWinner(boardcopy, let)):
                move = i
                return move


        cornersOpen = []    #If move does not result in a winner, computer will try the best move
        for i in possibleMoves:
            if i in[1,3,7,9]:
                cornersOpen.append(i)

        if(len(cornersOpen) > 0):
            move = SelectRandom(cornersOpen)
            return move

        if 5 in possibleMoves:
            move = 5
            return move

        edgesOpen = []
        for i in possibleMoves:
            if i in [2,4,6,8]:
                edgesOpen.append(i)

        if(len(edgesOpen) > 0):
            move = SelectRandom(edgesOpen)
            return move

#Function to select a random value from a list
def SelectRandom(li):
    import random
    ln = len(li)
    r=random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the game")
    PrintBoard(board)

    while not(BoardFull(board)):
        if not(IsWinner(board, 0)):
            PlayerMove()
            PrintBoard(board)
        else:
            print("Sorry You Lose !!!")
            break

        if not(IsWinner(board, 'X')):
            move = ComputerMove()
            if(move == 0):
                print(" ")
            else:
                InsertLetter('0', move)
                print('computer placed an 0 on position' , move , ':')
                PrintBoard(board)
        else:
            print("You Win !!!")
            break

    if(BoardFull(board)):
        print("Game is tied")

while(True):
    x = input("Do you want to play again ?(y/n)")
    if x.lower() == 'y':
        board = ['-' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
