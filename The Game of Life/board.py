from typing import List


class Board:
    board: List[list]
    cell_symbol: str
    height: int
    wight: int

    _CELL = True
    _NO_CELL = False

    def __init__(self, matrix: List[list], cell_symbol: str, height: int, wight: int):
        self.__board = matrix
        self.cell_symbol = cell_symbol
        self.__height = height
        self.__wight = wight

    @classmethod
    def from_string(cls, text: str) -> 'Board':
        cell_symbol = 'X'
        not_allowed_symbols = ['.', '\n', ' ']

        for elem in text.strip():
            if elem not in not_allowed_symbols:
                cell_symbol = elem
                break

        matrix = [
            [cls._CELL if elem != '.' else cls._NO_CELL for elem in list(row.strip())]
            for row in text.strip().split('\n')
        ]

        height = len(matrix)
        wight = len(matrix[0])

        return cls(matrix, cell_symbol, height, wight)

    def __kill_cell(self, row: int, column: int) -> None:
        self.__board[row][column] = False

    def __born_cell(self, row: int, column: int) -> None:
        self.__board[row][column] = True

    @staticmethod
    def __validate_presence(length, number) -> bool:
        if -1 < number < length:
            return True
        return False

    def __modify_status(self, row, column) -> bool:
        current_state = self.__board[row][column]

        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        ]

        neighbor_count = 0
        for direction in directions:
            new_row, new_col = row+direction[0], column+direction[1]
            if self.__validate_presence(self.__height, new_row) and self.__validate_presence(self.__wight, new_col):
                if self.__board[new_row][new_col]:
                    neighbor_count += 1

        status_alive = current_state and neighbor_count == 2 or neighbor_count == 3
        if status_alive:
            # self.__bord_cell(row, column)
            return True
        else:
            # self.__kill_cell(row, column)
            return False

    def change_generations(self) -> None:
        positions_to_change = {
            'born': [],
            'kill': []
        }

        for r in range(self.__height):
            for c in range(self.__wight):
                if self.__modify_status(r, c):
                    positions_to_change['born'].append((r, c))
                    continue
                positions_to_change['kill'].append((r, c))

        for position in positions_to_change['born']:
            r, c = position
            self.__born_cell(r, c)
        for position in positions_to_change['kill']:
            r, c = position
            self.__kill_cell(r, c)

    def print_board(self) -> None:
        board = [
            ' '.join([self.cell_symbol if elem else '.' for elem in row])
            for row in self.__board
        ]
        print('\n'.join([row for row in board]))

