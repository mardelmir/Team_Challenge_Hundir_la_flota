import numpy as np
import random

class Board:
    '''
    Defines the class as Board
    
        Argument (constructor):
                player_id (str): string received from input, default value if left empty
                board_size (int)
                ships (dict)
            
        Attributes:
            player_id (str): A way to store the ID of player or computer
            size (int): Sets the board size.
            ships (dict): Ship lengths stored as values in a dictionary, also in variables script
            board (NDArray): Creates the actual board in whatever size is stores in 'size' variable (10)
            shots_board (NDArray): Creates the second board for tracking where you have fired
            ships_positions (list): Stores the positions of the ships as tuples in a list
    '''
    
    def __init__(self, player_id, board_size, ships):
        '''
        Initializes an instance of 'Board' class
        It generates all attributes and calls Board.generate_ship() method which chain calls the others to place ships on the board
        '''
        self.player_id = player_id 
        self.size = board_size  
        self.ships = ships  
        self.board = np.full((self.size, self.size), '·')
        self.shots_board = np.full((self.size, self.size), '·')
        self.ship_positions = []
        self.generate_ships()
        

    def generate_ships(self):
        '''
        Randomly generates an (x, y) set of coordinates using random based on the length of the ships (values from ships dictionary).
        It randomly selects if the orientation will be horizontal or vertical and calls check_position method to check if ship can be placed on the board.
        If check_position doesn't return False, it calls place_ships to place the ships on the board.
        '''
        for length in self.ships.values():
            placed = False 
            while not placed:
                x, y = random.randint(0, self.size -1), random.randint(0, self.size -1)
                orientation = random.choice(['H', 'V']) 
                
                if self.check_position(x, y, length, orientation):
                    self.place_ships(x, y, length, orientation)
                    placed = True
    

    def check_position(self, x, y, length, orientation):
        '''
        Checks for both horizontal and vertical orientation if:
            - The length of the ship is valid and fits within the board.
            - That all spaces within the ship's length are empty (e.g. contain '·'), aka it's not already occupied by another ship.
        '''
        if orientation == 'H':
            if y + length > self.size:  
                return False
            return all(self.board[x, y + i] == '·' for i in range(length))  
        else:
            if x + length > self.size: 
                return False
            return all(self.board[x + i, y] == '·' for i in range(length))
        
    
    def place_ships(self, x, y, length, orientation):
        # Places the ship on the board and updates coordinates of the ship in the ship_positions list
      
        if orientation =='H':
            for i in range(length):
                self.board[x, y + i] = 'O'
                self.ship_positions.append((x, y, + i))
        else:
            for i in range(length):
                self.board[x + i, y] = 'O'
                self.ship_positions.append((x + i, y))
        
    def add_index(self, board):
        # Generates axis for boards
        size = board.shape[0]
        row_index = np.arange(size) + 1   
        col_index = np.concatenate([[' '], row_index]).reshape(size + 1, 1)
        stack_row = np.vstack([row_index, board])
        final_board = np.hstack([col_index, stack_row])
        return final_board
    
    def print_board(self, oponent_board, reveal_ships = False):
        # Prints player's board and oponent board with or whitout ships
        
        if reveal_ships: 
            for row_b1, row_b2 in zip(self.add_index(self.board), self.add_index(oponent_board.board)):
                str_b1 = ' '.join(f'{num:2}' for num in row_b1)
                str_b2 = ' '.join(f'{num:2}' for num in row_b2)
        
                print(f'{str_b1}{' '*10}{str_b2}')
        else:
            for row_b1, row_b2 in zip(self.add_index(self.board), self.add_index(self.shots_board)):
                str_b1 = ' '.join(f'{num:2}' for num in row_b1)
                str_b2 = ' '.join(f'{num:2}' for num in row_b2)
            
                print(f'{str_b1}{' '*10}{str_b2}')