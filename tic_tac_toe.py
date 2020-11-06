# dictonary as the board
board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for key in board:
    board_keys.append(key)


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


# Now we'll write the main function which has all the gameplay functionality.
def main():
    turn = 'X'
    count = 0
    flag=0
    winner=""
    player1 = input("enter player 1 name: ")
    player2 = input("enter player 2 name: ")
    ### we can enter only 10 values(correct position)
    for i in range(10):

        print(player1, ":X")
        print(player2, ":O")
        printBoard(board)

        if turn == 'X':
            print("It's " + player1 + " turn please enter position: ")
        else:
            print("It's " + player2 + " turn please enter position: ")

        move = input()
        intmove = int(move)
        if   intmove > 0 and intmove <= 9  and board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("place is already filled or incorrect place enter between 1 - 9")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':  # across the top
                flag=1
                winner=turn
            elif board['4'] == board['5'] == board['6'] != ' ':  # across the middle
                flag = 1
                winner = turn


            elif board['1'] == board['2'] == board['3'] != ' ':  # across the bottom
                flag = 1
                winner = turn


            elif board['1'] == board['4'] == board['7'] != ' ':  # down the left side
                flag = 1
                winner = turn

            elif board['2'] == board['5'] == board['8'] != ' ':  # down the middle
                flag = 1
                winner = turn


            elif board['3'] == board['6'] == board['9'] != ' ':  # down the right side
                flag = 1
                winner = turn


            elif board['7'] == board['5'] == board['3'] != ' ':  # diagonal
                flag = 1
                winner = turn

            elif board['1'] == board['5'] == board['9'] != ' ':  # diagonal
                flag = 1
                winner = turn



        if flag==1:
            printBoard(board)
            if winner == 'X':
                print('************************')
                print(player1 + " wins")
                print('************************')
            else:
                print('************************')
                print(player2 + " wins")
                print('************************')

            break


         # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print('************************')
            print("It's a Tie ")
            print('************************')
            break

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    #player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            board[key] = " "

        main()


if __name__ == "__main__":
    main()
