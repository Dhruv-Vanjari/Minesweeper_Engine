# Minesweeper_Engine
Simplest Minesweeper backend that you can find
-----------------------------------------------
This is the simplest backend for your minesweeper game that you can find. It has a constructor, method to get a list of turnable cells and a method to get neighbour mine count of a specified cell.
Thats it!

Constructor
-----------
```
engine = minesweeper_engine.Engine(size, mine_frequency, first_move_x, first_move_y)
```
All the parameter are integer values
`mine_frequency` ranges from 0 to 10

Turn a cell
-----------
```
engine.get(x, y)
```
returns `MINE` if it has a mine OR
returns a list of two tuples specifying positino turnable cells

Get Neighbour Mine Count
------------------------
```
engine.getNeighbourMineCount((x, y))
```
returns an integer value


