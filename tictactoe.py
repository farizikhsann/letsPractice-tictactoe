
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def mulai():
    player = 'X'
    jml_input = 0

    while jml_input < 9:
        printBoard(board)

        angkaKotak = input("Player "+ player+ ", pilih kotak (1-9): ")

        if angkaKotak not in board.keys() or board[angkaKotak] != ' ':
            print("Angka kotak tidak benar atau pilih kotak yang belum terisi!. Try again.")
            continue

        board[angkaKotak] = player
        jml_input += 1
 
        if player == 'X':
            player = 'O'
        elif player =='O':
            player = 'X'
    else:
        printBoard(board)

if __name__ == '__main__':
    
    board = {
        '7': ' ', '8': ' ', '9': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '1': ' ', '2': ' ', '3': ' '
    }

    mulai()
