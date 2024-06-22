# Justin Ventura | Jun 21, 2024
from pysolver import solve_board, print_solution


if __name__ == "__main__":
    rook_locations = set([])
    solutions = solve_board(rook_locations)
    print(len(solutions))

    for i, sol in enumerate(solutions):
        print_solution(sol, ith_sol=i + 1)
