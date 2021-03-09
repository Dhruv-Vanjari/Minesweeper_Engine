from minesweeper_engine import Engine
from minesweeper_engine import MINE

def printBuffer(this_engine):
    for i, row in enumerate(this_engine.getBuffer()):
        for j, cell in enumerate(row):
            if cell is MINE:
                print("* ", end='')
            else:
                print(str(this_engine.getNeighbourMineCount((i, j))) + " ", end='')
        print()

engine = Engine(10, 5, 2, 2)
buffer = engine.getBuffer();
print("----------------------------")
print("         Engine(size, mine_frequency, first move")
print("engine = Engine( 10,         5,          2, 2  )")
print("----------------------------")
printBuffer(engine)
print()
print("-----------------------")
print("print(engine.get(9, 9))")
print("-----------------------")
print(engine.get(9, 9))
print()
print("-------------------------------------------")
print("print(engine.getNeighbourMineCount((9, 9)))")
print("-------------------------------------------")
print(engine.getNeighbourMineCount((9, 9)))
