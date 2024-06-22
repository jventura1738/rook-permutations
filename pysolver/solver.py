# Justin Ventura | Jun 21, 2024
from typing import List, Set, Tuple


Board = List[List[str]]
Location = Tuple[int, int]


ROOK = "♜"
FALLBACK_ROOK = "R"
BLANK = "."


class Solver:
    def __init__(self, bsize: int = 8, rchar: str = ROOK):
        self.bsize = bsize
        self.rchar = rchar
        self.rooks = set([])

        # NOTE: mostly just for CLI visualization purposes
        self._board_instance: Board = None
        self._board_instance = self.get_default_board()

    def set_rooks(self, rooks: Set[Location]) -> bool:
        for r, c in rooks:
            if not self.is_valid(r, c):
                self.rooks = set()
                return False
            self.rooks.add((r, c))
        return True

    def get_rooks(self) -> List[Location]:
        return self.rooks

    def get_default_board(self) -> Board:
        if self._board_instance is None:
            self._board_instance = [[BLANK] * self.bsize for _ in range(self.bsize)]
        return self._board_instance

    def clear_board(self) -> None:
        for r in range(self.bsize):
            for c in range(self.bsize):
                self._board_instance[r][c] = BLANK

    # NOTE: does not set rooks, just for visualization
    def place_rooks(self, locations: List[Location]) -> bool:
        for r, c in locations:
            if not self.is_valid_placement(r, c):
                self.clear_board()
                return False
            self._board_instance[r][c] = self.rchar
        return True

    # NOTE: checks against board
    def is_valid_placement(self, row: int, col: int) -> bool:
        for r in range(self.bsize):
            if (
                self._board_instance[row][r] == self.rchar
                or self._board_instance[r][col] == self.rchar
            ):
                return False
        return True

    # NOTE: checks against current rooks
    def is_valid(self, row: int, col: int) -> bool:
        for r, c in self.rooks:
            if r == row or c == col:
                return False
        return True

    def solve_board(self) -> List[Set[Location]]:
        if len(self.rooks) == self.bsize:
            return [self.rooks.copy()]

        solutions = []
        start_row = len(self.rooks)

        for c in range(self.bsize):
            if self.is_valid(start_row, c):
                self.rooks.add((start_row, c))
                solutions.extend(self.solve_board())
                self.rooks.remove((start_row, c))

        return solutions
