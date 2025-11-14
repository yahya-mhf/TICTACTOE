import os 

class Board:
    def __init__(self, size = 3):
        self.size = size
        self.table = [['.'] * size for _ in range(size)]

    def play(self, player: str, coordinate: tuple):
        x, y = coordinate
        if x >= self.size or y >= self.size or self.table[x][y] != '.':
            raise ValueError("MOVE OUT OF BOARD SIZE!")
        self.table[x][y] = player

    def display(self):
        header = "   " + "  ".join(f"{i}" for i in range(self.size))
        print(header)
        for i, row in enumerate(self.table):
            print(i, end='  ')
            for case in row:
                print(case, end='  ')
            print()

    def is_game_over(self, player): # retrun False, tie, (X win, O win)
        # check is X win
        # check all rows and colomns
        for i, row in enumerate(self.table):
            for j, case in enumerate(row):
                if self.table[i][j] != player and self.table[j][i] != player:
                    break
            else:
                return f"WIN {player}"
        # Check diagonals
        for i in range(self.size):
            if self.table[i][i] != player and self.table[i][self.size - 1 - i] != player:
                break
        else:
            return f"WIN {player}"

        # check if tie means the board is full
        for row in self.table:
            for case in row:
                if case == '.':
                    return False # game is not over
        # This will RUN if game is TIE
        return "TIE"

def main():
    B = Board() # 
    B.display()
    # Game Loop
    player = 'X' # first player to play
    running = True
    while running:   
        # player to move
        print(f"{player} To Play")
        
        while True:
            # get the play (c)
            try: # check the play (c)
                x, y = list(map(int ,input("MOVE eg(0 2): ").split()))
                B.play(player, (x, y)) # do the move (c)
            except KeyboardInterrupt:
                print("\nexiting...")
                exit()
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print() # temp
                B.display()
            else:
                break
        
        B.display()
        # check for game status
        
        if B.is_game_over(player):
            print(B.is_game_over(player))
            running = False

        player = 'X' if player == 'O' else 'O'
    
    
if __name__=="__main__":
    main()
