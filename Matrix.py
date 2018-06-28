from copy import deepcopy

class SimpleMatrix:
    def __init__(self, rows, form="row"):
#       assert len(set([len(row) for row in rows])) == 1, \
#               "all rows/columns in the list must be the same length"
        self._matrix = [[]]
        if "row" in form:
            self._matrix = deepcopy(rows)
        elif "col" in form:
            self._matrix = [list(col) for col in zip(rows)]

    def __setitem__(self, *args):
        assert isinstance(args[1], list), "must replace row with list"
        if len(args) == 2:
            assert isinstance(args[0], int), "invalid row ID"
            self._matrix[args[0]] = list(args[1])

    def __getitem__(self, *args):
        if len(args) == 1:
            return self._matrix[args[0]]
        elif len(args) == 2:
            return self._matrix[args[0]][args[1]]
        else:
            raise IndexError

    def __len__(self):
        return len(self._matrix)

    def getRows(self):
        return deepcopy(self._matrix)

    def getCols(self):
        a = []
        for col in range(len(self._matrix)):
            a.append([row[col] for row in self._matrix])
        return a

    def getRow(self, row : int):
        return list(self.matrix[row])

    def getCol(self, col : int):
        return self.getCols()[col]
