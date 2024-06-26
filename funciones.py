import numpy as np

def welcome():
    # Prints welcome message with game instructions.
    
    print(f'{'_'*100}\n\n¡Bienvenido a Battleship: Golden Hind Edition!\n\n' \
        'Cómo jugar:\n'\
        '   1. Introduce tu nombre de jugador para iniciar la partida.\n'\
        '   2. El juego posiciona de forma aleatoria todos los barcos. \n'\
        '   3. El primer turno es tuyo, introduce las coordenadas de disparo. Si aciertas, continúas jugando, si no el turno pasa a la máquina.\n'\
        '   4. El juego finaliza cuando todos los barcos de un jugador están hundidos.\n\n'\
        'Puedes salir del juego escribiendo "exit" en cualquier input.\n\n'\
        f'¡Buena suerte!\n{'_'*100}\n')


def player_name():
    # Requests the player's name. If none is provided, 'human_player' is asigned as default.
    
    name = input('Introduce tu nombre: ').strip()
    return name if name != '' else False

    
def get_shot_coordinates(size):
    '''
    Requests shot coordinates to the player. The player can repeat coordinates from a previous shot.
    Ensures the provided input is of type int for both row and column (col) coordinates by removing accidental blank spaces and replacing ',' with '.'.
    Ensures the provided input is within the limits of the game board.
    '''
    try:
        coordinates = []
        for i in range(2):
            input_value = (input(f'{'Fila' if i == 0 else 'Columna'} del disparo (1-{size}): ')).replace(' ', '').replace(',', '.')
            if input_value == 'exit':
                break
            else:
                coordinate = int(float(input_value)) - 1
                if coordinate < 0:
                    print('¡El valor introducido no es válido (número negativo)!')
                    return get_shot_coordinates(size)
                elif coordinate > size - 1:
                    print('¡La coordenada introducida está fuera del tablero!')
                    return get_shot_coordinates(size)
                else:
                    coordinates.append(coordinate)
        return tuple(coordinates)
    except ValueError:
        print('¡El valor introducido no es válido (texto)!')
        get_shot_coordinates(size)
        

def generate_shot(pc_shots, size):
    # Generates random shot coordinates for the PC, ensuring said coordinates are within the limits of the game board and have not been used before.

    shot = tuple(np.random.randint(0, size - 1, (2,)))
    if shot in pc_shots:
        generate_shot(pc_shots, size)
    else:
        pc_shots.append(shot)
    return pc_shots, shot


def shoot(player_board, oponent_board, coordinate):
    # Updates current player board and oponent board after a shot is made

    if oponent_board.board[coordinate] == 'O':
        oponent_board.board[coordinate] = 'X'
        player_board.shots_board[coordinate] = 'X'
        successful_shot = True
    else:
        oponent_board.board[coordinate] = '~'
        player_board.shots_board[coordinate] = '~'
        successful_shot = False
    
    return player_board, oponent_board, successful_shot