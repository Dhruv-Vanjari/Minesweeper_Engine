from minesweeper_engine import Engine
from minesweeper_engine import MINE

class Board:
    def __init__(self, size, mine_frequency):
        self.size = size
        self.mine_frequency = mine_frequency
        self._initializeBuffer()

    def _initializeBuffer(self):
        self.buffer = list()
        for i in range(self.size):
            self.buffer.append(list())
            for j in range(self.size):
                self.buffer[i].append(None)

    def _turnCells(self, cells):
        for cell in cells:
            self.buffer[cell[0]][cell[1]] = str(self.engine.getNeighbourMineCount(cell))

    def firstMove(self, cell):
        self.engine = Engine(self.size, self.mine_frequency, cell[0], cell[1])
        self.move(cell)

    def move(self, cell):
        if cell[0] >= self.size or cell[1] >= self.size:
            return None;

        result = self.engine.get(cell[0], cell[1])
        if result is MINE:
            self.buffer[cell[0]][cell[1]] = "*"
            return MINE
        else:
            self._turnCells(result)

    def draw(self):
        print('    ', end='')
        for i in range(self.size):
            print(i, end=' ')
        print()
        print()
        for i, row in enumerate(self.buffer):
            print(i, end='   ')
            for cell in row:
                if cell is None:
                    print("# ", end='')
                elif cell == '0':
                    print("  ", end='')
                else:
                    print(cell + " ", end='')
            print()

board = Board(10, 5)
y = input("Enter X: ")
x = input("Enter Y: ")

try:
    board.firstMove((int(x), int(y)))
except:
    print("invalid input")
    exit()

board.draw()
print()

while(True):
    y = input("Enter X: ")
    if y.lower() == 'q':
        exit()

    x = input("Enter Y: ")
    if x.lower() == 'q':
        exit()

    try:
        x = int(x)
        y = int(y)
    except:
        print("invalid input")

    if board.move((x, y)) is MINE:
        print("Game Over")
        exit()

    board.draw()
    print()

print("You Win!")
