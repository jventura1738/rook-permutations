# Justin Ventura | Jun 22, 2024
import pytest
from pysolver.solver import Solver


@pytest.fixture()
def solver():
    return Solver(bsize=8)


def test_get_default_board(solver):
    board = solver.get_default_board()
    assert len(board) == 8
    assert all(len(row) == 8 for row in board)
    assert all(cell == "." for row in board for cell in row)


def test_place_rooks(solver):
    locations = [(0, 0), (1, 1), (2, 2)]
    solver.place_rooks(locations)
    board = solver.get_default_board()
    assert board[0][0] == solver.rchar
    assert board[1][1] == solver.rchar
    assert board[2][2] == solver.rchar


def test_clear_board(solver):
    locations = [(0, 0), (1, 1), (2, 2)]
    solver.place_rooks(locations)
    solver.clear_board()
    board = solver.get_default_board()
    assert all(cell == "." for row in board for cell in row)


def test_is_valid(solver):
    solver.set_rooks({(0, 0), (1, 1)})
    assert not solver.is_valid(0, 0)
    assert not solver.is_valid(1, 1)
    assert not solver.is_valid(0, 1)
    assert solver.is_valid(2, 2)


def test_is_valid_placement(solver):
    locations = [(0, 0), (1, 1), (2, 2)]
    solver.place_rooks(locations)
    assert not solver.is_valid_placement(0, 0)
    assert not solver.is_valid_placement(0, 1)
    assert not solver.is_valid_placement(1, 0)
    assert solver.is_valid_placement(3, 3)


def test_set_rooks(solver):
    rooks = {(0, 0), (1, 1), (2, 2)}
    success = solver.set_rooks(rooks)
    assert success == True
    assert solver.get_rooks() == rooks


def test_set_rooks_invalid(solver):
    rooks = {(0, 0), (0, 1)}
    success = solver.set_rooks(rooks)
    assert success == False
    assert solver.get_rooks() == set()


def test_solve_board_empty_8x8(solver):
    solutions = solver.solve_board()
    assert len(solutions) == 40320  # factorial(8)
    for solution in solutions:
        assert len(solution) == 8
        rows = [r for r, c in solution]
        cols = [c for r, c in solution]
        assert len(set(rows)) == 8
        assert len(set(cols)) == 8


def test_solve_board_unsolvable(solver):
    success = solver.set_rooks({(0, 0), (0, 5)})
    assert success == False, "Attacking rooks should have failed"


def test_solver_board_partial(solver):
    success = solver.set_rooks(set([(i, i) for i in range(7)]))
    assert success == True, "Non-attacking rooks should succeed"
    solutions = solver.solve_board()
    assert len(solutions) == 1, "Partial board should have 1 solution"
    assert (7, 7) in solutions[0], "Bottom right corner should be filled"


def test_solve_board_partial_solution(solver):
    solver.set_rooks({(0, 0), (1, 2), (2, 4)})
    solutions = solver.solve_board()
    assert len(solutions) > 0, "Partially filled board should have solutions"
    for solution in solutions:
        assert len(solution) == 8
        rows = [r for r, _ in solution]
        cols = [c for _, c in solution]
        assert len(set(rows)) == 8
        assert len(set(cols)) == 8


def test_place_rooks_invalid(solver):
    locations = {(0, 0), (0, 1)}
    success = solver.place_rooks(locations)
    assert success == False
    board = solver.get_default_board()
    assert all(
        cell == "." for row in board for cell in row
    ), "Board should be cleared after invalid placement"


def test_missing_rook_middle(solver):
    locations = {(i, i) for i in range(8)}
    locations.remove((1, 1))
    success = solver.set_rooks(locations)
    assert success == True, "Non-attacking rooks should succeed"
    solutions = solver.solve_board()
    print(solutions)
    assert len(solutions) == 1, "Partial board should have 1 solution"
    assert (1, 1) in solutions[0], "Middle rook should be placed"


def test_missing_rooks(solver):
    locations = {(0, 0), (7, 1), (6, 2), (3, 3), (5, 5), (4, 7)}
    success = solver.set_rooks(locations)
    assert success == True, "Non-attacking rooks should succeed"
    solutions = solver.solve_board()
    assert len(solutions) == 2, "Partial board should have 2 solutions"
