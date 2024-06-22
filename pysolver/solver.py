# Justin Ventura | Jun 21, 2024
from typing import List, Set, Tuple, TypeAlias


Board: TypeAlias = List[List[str]]
Location: TypeAlias = Tuple[int, int]


ROOK = "♜"
FALLBACK_ROOK = "R"
BLANK = "."


_board_instance: Board = None


def get_default_board(bsize: int = 8) -> Board:
    global _board_instance
    if _board_instance is None:
        return [[BLANK] * bsize for _ in range(bsize)]
    return _board_instance


def clear_board(board: Board, bsize: int = 8) -> None:
    for r in range(bsize):
        for c in range(bsize):
            board[r][c] = BLANK


def place_rooks(board: Board, locations: List[Location], bsize: int = 8) -> None:
    for r, c in locations:
        board[r][c] = ROOK


def print_solution(rooks: List[Location], ith_sol: str = "", bsize: int = 8):
    board = get_default_board(bsize)
    place_rooks(board, rooks)

    print(f"> Solution {ith_sol}")
    print(f" {'-'*len(board[0]*2)}")
    for row in board:
        print(f"|{' '.join(row)} |")
    print(f" {'-'*len(board[0]*2)}\n")


def is_valid(rooks: Set[Location], row: int, col: int, bsize: int = 8) -> bool:
    for r, c in rooks:
        if r == row or c == col:
            return False
    return True


def solve_board(rooks: Set[Location], bsize: int = 8) -> List[Set[Location]]:
    if len(rooks) == bsize:
        return [rooks.copy()]

    solutions = []
    start_row = len(rooks)

    for c in range(bsize):
        if is_valid(rooks, start_row, c, bsize):
            rooks.add((start_row, c))
            solutions.extend(solve_board(rooks, bsize))
            rooks.remove((start_row, c))

    return solutions
