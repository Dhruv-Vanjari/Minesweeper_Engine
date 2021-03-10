#    Minesweeper Engine to provide backend for your minesweeper game
#    Copyright (C) 2021 Dhruv Vanjari
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random
import copy

MINE = True
NO_MINE = False
NEIGHBOURS = [-1, 0, 1]

class Engine:
    def __init__(self, size, mine_frequency, row, column):
        self._size = size
        self._frequency = mine_frequency
        self._buffer = list()
        self._placeMines()
        self._buffer[row][column] = NO_MINE

    def getBuffer(self):
        return copy.deepcopy(self._buffer)

    def _placeMines(self):
        for row in range(self._size):
            self._buffer.append(list())
            for column in range(self._size):
                if random.randint(0, 11 - self._frequency) == 1:
                    self._buffer[row].append(MINE)
                else:
                    self._buffer[row].append(NO_MINE)

    def _getNeighbours(self, cell):
        row, column = cell
        neighbours = list()
        for del_row in NEIGHBOURS:
            for del_col in NEIGHBOURS:
                if (del_row == 0 and del_col == 0):
                    continue
                if row + del_row >= self._size or column + del_col >= self._size:
                    continue
                if row + del_row == -1 or column + del_col == -1:
                    continue
                neighbours.append((row + del_row, column + del_col))
        return neighbours

    def _get(self, cell):
        return self._buffer[cell[0]][cell[1]]

    def getNeighbourMineCount(self, cell):
        count = 0
        for cell in self._getNeighbours(cell):
            if self._get(cell) == MINE:
                count += 1
        return count

    def _cascade_get(self, row, column):
        queue = [(row, column)]

        for cell in queue:
            if self.getNeighbourMineCount(cell) == 0:
                for neighbour in self._getNeighbours(cell):
                    if neighbour in queue or self._get(cell) is MINE:
                        continue
                    queue.append(neighbour)
        return queue

    def get(self, row, column):
        if self._get((row, column)) is MINE:
            return MINE

        return self._cascade_get(row, column)
