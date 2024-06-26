import clases
import funciones
import numpy as np
import time
import variables

# Game variables
turn = 'player'
succesful_shot = False
exit_game = False

# Player variables
player_lives = sum(variables.SHIPS.values())
player_board = clases.Board(variables.PLAYER_ID, variables.BOARD_SIZE, variables.SHIPS)

# PC variables
pc_lives = sum(variables.SHIPS.values())
pc_shots = []
pc_board = clases.Board(variables.PC_ID, variables.BOARD_SIZE, variables.SHIPS)


# Game initialization
funciones.welcome()
player_id = funciones.player_name()

if player_id == 'exit':
    exit_game = True

# The game starts. It will end if the player writes 'exit' in any input
while exit_game == False:
    if turn == 'player':
        print('_'*100, '\n')
        print('*** Tu turno ***', '\n')
        print(f'Tu tablero{' '*29}Tablero oponente')
        player_board.print_board(pc_board, reveal_ships = True)
        
        print('')
        coordinates = funciones.get_shot_coordinates()
        if coordinates == ():
            break
        
        shot_result = funciones.shoot(player_board, pc_board, coordinates)
        succesful_shot = shot_result[2]
        # update boards
        
        if succesful_shot == True:
            print('\n¡Has tocado!')
            pc_lives -= 1
            if pc_lives == 0:
                print(f'¡Enhirabuena {player_id}, has ganado!')
                break
            else:
                time.sleep(.5)
                continue
        else:
            print('\n¡Agua!')
            turn = 'pc'
            time.sleep(.5)
            continue
        
    else:
        print('_'*100, '\n')
        print('*** Turno del oponente ***', '\n')
        print(f'Tu tablero{' '*29}Tablero oponente')
        player_board.print_board(pc_board, reveal_ships = False)
        
        pc_shots, coordinates = funciones.generate_shot(pc_shots, variables.BOARD_SIZE)
        shot_result = funciones.shoot(pc_board, player_board, coordinates)
        succesful_shot = shot_result[2]
        # mensaje de si has tocado/hundido
  
        if succesful_shot == True:
            print('\n¡Tocado!')
            player_lives -= 1
            all_player_ships_sunk = sorted(player_board.ship_positions) == sorted(pc_shots) # Confirms all ships_positions have been shot
            if player_lives == 0 and all_player_ships_sunk:
                print('¡Has perdido!')
                break
            else:
                continue
        else:
            print('\n¡Agua!')
            turn = 'player'
            time.sleep(.5)
            continue
        

print('\n¡Hasta pronto!')