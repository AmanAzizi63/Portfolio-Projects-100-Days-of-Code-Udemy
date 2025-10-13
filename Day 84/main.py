import random
import time

field = [['', '', ''],
         ['', '', ''],
         ['', '', '']]


def showField():
    print(f'{field[0]}\n{field[1]}\n{field[2]}')

showField()

def check_winner():
    # Zeilen prüfen
    for row in field:
        if row[0] == row[1] == row[2] != '':
            if row[0] == 'X':
                print('You won')
            else:
                print('You lost')
            return True

    # Spalten prüfen
    for col in range(3):
        if field[0][col] == field[1][col] == field[2][col] != '':
            if field[0][col] == 'X':
                print('You won')
            else:
                print('You lost')
            return True

    # Hauptdiagonale prüfen
    if field[0][0] == field[1][1] == field[2][2] != '':
        if field[0][0] == 'X':
            print('You won')
        else:
            print('You lost')
        return True

    # Gegendiagonale prüfen
    if field[0][2] == field[1][1] == field[2][0] != '':
        if field[0][2] == 'X':
            print('You won')
        else:
            print('You lost')
        return True

    return False

print("You're Player 1, your symbol is X")
game_is_on = True
while game_is_on:
    column_player = int(input('Sag in welcher Spalte du dein X setzen möchtest! '))
    row_player = int(input('Sag in welcher Zeile du dein X setzen möchtest! '))

    if column_player <= 3 and row_player <=3 and  field[row_player-1][column_player-1] != 'X' and field[row_player-1][column_player-1] != '0':
        field[row_player-1][column_player-1] = 'X'
        showField()
    else:
        print('Diese Spalte/Zeile gibt es nicht oder wurde schon verwendet versuche es nochmal')
        column_player = int(input('Sag in welcher Spalte du dein X setzen möchtest! '))
        row_player = int(input('Sag in welcher Zeile du dein X setzen möchtest! '))
        field[row_player-1][column_player-1] = 'X'
        showField()
    
    if check_winner():
        game_is_on = False

    print('Die KI hat sich für diese Position entschieden! ')
    column_AI = random.randint(0,3)
    row_AI = random.randint(0,3)

    time.sleep(2)
    
    if field[row_AI-1][column_AI-1] != '0' and field[row_AI-1][column_AI-1] != 'X':
        field[row_AI-1][column_AI-1] = '0'
    else:
        column_AI = random.randint(0,3)
        row_AI = random.randint(0,3)
        time.sleep(2)
        if field[row_AI-1][column_AI-1] != '0' and field[row_AI-1][column_AI-1] != 'X':
            field[row_AI-1][column_AI-1] = '0'




    showField()

    if check_winner():
        game_is_on = False









    
  
