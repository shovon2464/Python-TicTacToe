board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def converter(position):
    if position == 1:
        return 6
    if position == 2:
        return 7
    if position == 3:
        return 8
    if position == 4:
        return 3
    if position == 5:
        return 4
    if position == 6:
        return 5
    if position == 7:
        return 0
    if position == 8:
        return 1
    if position == 9:
        return 2

def displayBoard(board):
    i = 0
    j = 0
    while(i<3):
        print("     |     |     ")
        print("  {}  |  {}  |  {}  ".format(board[j], board[j+1], board[j+2]))
        print("     |     |     ")
        if(i!=2):
            print('------------------')
        i +=1
        j+=3


def selectPlayer():
    player1 = '1'
    player2 = '2'

    def checkInput(player1Input):

        if player1Input in 'xo':
            return player1Input
        else:
            print("Select your symbol in between 'X' and 'O', Please be careful. Player 2 will automatically get the other symbol.")
            player1Input = input().lower()
            return checkInput(player1Input)


    print("Player 1: Select your symbol in between 'X' and 'O', Player 2 will automatically get the other symbol")
    player1Input = input().lower()
    player1 = checkInput(player1Input)

    if player1 in 'x':
        player2 = 'o'
    else:
        player2 = 'x'

    return player1, player2


def checkWinner(position, player):
    global board
    if position == 0:
        if (board[0]==board[1]) and (board[0]==board[2]):
            return True
        elif (board[0] == board[3]) and (board[0] == board[6]):
            return True
        elif (board[0] == board[4]) and (board[0] == board[8]):
            return True
        else:
            return False

    elif position == 1:
        if (board[1]==board[0]) and (board[1]==board[2]):
            return True
        elif (board[1] == board[4]) and (board[1] == board[7]):
            return True
        else:
            return False

    elif position == 2:
        if (board[2]==board[1]) and (board[2]==board[0]):
            return True
        elif (board[2] == board[5]) and (board[2] == board[8]):
            return True
        elif (board[2] == board[4]) and (board[2] == board[6]):
            return True
        else:
            return False

    elif position == 3:
        if (board[3]==board[0]) and (board[3]==board[6]):
            return True
        elif (board[3] == board[4]) and (board[3] == board[5]):
            return True
        else:
            return False
    elif position == 4:
        if (board[4]==board[3]) and (board[4]==board[5]):
            return True
        elif (board[4] == board[1]) and (board[4] == board[7]):
            return True
        else:
            return False

    elif position == 5:
        if (board[5]==board[2]) and (board[5]==board[8]):
            return True
        elif (board[5] == board[4]) and (board[5] == board[3]):
            return True
        else:
            return False

    elif position == 6:
        if (board[6]==board[3]) and (board[6]==board[0]):
            return True
        elif (board[6] == board[7]) and (board[6] == board[8]):
            return True
        elif (board[6] == board[4]) and (board[6] == board[2]):
            return True
        else:
            return False

    elif position == 7:
        if (board[7]==board[6]) and (board[7]==board[8]):
            return True
        elif (board[7] == board[4]) and (board[7] == board[1]):
            return True
        else:
            return False

    elif position == 8:
        if (board[8]==board[7]) and (board[8]==board[6]):
            return True
        elif (board[8] == board[5]) and (board[8] == board[2]):
            return True
        elif (board[8] == board[4]) and (board[8] == board[0]):
            return True
        else:
            return False

    else:
        return False

def checkFull():
    global board
    result = False
    for item in board:
        if item == ' ':
            result = True

    return result

def play():
    global board
    player1 = '1'
    player2 = '2'
    answer = False

    def againCheck(againInput):
        if againInput in 'yes':
            return True
        else:
            return False

    def checkPlay(answerInput):
        if answerInput in 'yes':
            return True
        else:
            print("Please say yes or y if you want to play")
            answerInput = input().lower()
            return checkPlay(answerInput)

    print('Do you want to play the game?')
    answerInput = input().lower()

    answer = checkPlay(answerInput)

    if answer:
        result = selectPlayer()
        player1 = result[0].upper()
        player2 = result[1].upper()

        matchEnd = False
        winner1 = False
        winner2 = False

        counter = 0

        while(matchEnd == False):
            def inputPlayer1(input1):
                global board
                position1 = converter(input1)
                if board[position1] == ' ':
                    board[position1] = player1
                    
                else:
                    print('Player 1: The postion is already taken, Select other Position')
                    inputPlayer1(int(input()))
                return position1

            def inputPlayer2(input2):
                global board
                position2 = converter(input2)
                if board[position2] == ' ':
                    board[position2] = player2
                else:
                    print('Player 2: The postion is already taken, Select other Position')
                    inputPlayer2(int(input()))

                return position2

            if counter<9:
                print("Player 1: Select the positon")
                positionP1 = inputPlayer1(int(input()))
                displayBoard(board)
                matchEnd = checkWinner(positionP1, player1)
                counter += 1

                if matchEnd:
                    winner1 = True
                    print('Match ends, Player 1 is the winner')
                    break

                if counter == 9:

                    continue

                print("Player 2: Select the positon")
                positionP2 = inputPlayer2(int(input()))
                displayBoard(board)
                matchEnd = checkWinner(positionP2, player2)
                counter += 1
                if matchEnd:
                    winner2 = True
                    print('Match ends, Player 2 is the winner')
                    break
            else:
                matchEnd = True
                print("Match Drawn")

        playAgain = False
        playAgain = againCheck(input("Do you want to play again?").lower())

        if playAgain:
            board = board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            play()
        else:
            board = board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            player1 = '1'
            player2 = '2'
            answer = False
            exit()





play()