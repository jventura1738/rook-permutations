# Justin Ventura | Jun 21, 2024
from typing import List, Set, Tuple


ROOK = "♜"
FALLBACK_ROOK = "R"
BLANK = "."


def get_default_board(bsize: int = 8) -> List[List[str]]:
    return [[BLANK] * bsize for _ in range(bsize)]


def place_rooks(
    board: List[List[str]], locations: List[Tuple[int, int]], bsize: int = 8
) -> None:
    for r, c in locations:
        try:
            board[r][c] = ROOK
        except IndexError:
            print(f"IndexError: Cannot place rook at {r}, {c}")


def print_solution(rooks: List[Tuple[int, int]], ith_sol: str = "", bsize: int = 8):
    board = get_default_board(bsize)
    place_rooks(board, rooks)

    print(f">Solution {ith_sol}")
    print(f" {'-'*len(board[0]*2)}")
    for row in board:
        print(f"|{' '.join(row)} |")
    print(f" {'-'*len(board[0]*2)}\n")


def is_valid(rooks: Set[Tuple[int, int]], row: int, col: int, bsize: int = 8) -> bool:
    for r, c in rooks:
        if r == row or c == col:
            return False
    return True


def solve_board(
    rooks: Set[Tuple[int, int]], bsize: int = 8
) -> List[Set[Tuple[int, int]]]:
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


if __name__ == "__main__":
    bsize = 8
    rook_locations = set([])
    solutions = solve_board(rook_locations)
    print(len(solutions))

    for i, sol in enumerate(solutions):
        print_solution(sol, ith_sol=i + 1)
