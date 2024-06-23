# Justin Ventura | Jun 21, 2024
from pysolver import Solver

import os
import sys


# Gets y, n, Y, or N
def get_yn(prompt: str) -> str:
    while True:
        uinput = input(f"{prompt}> ").strip().lower()
        if uinput in "yn":
            return uinput
        print("Please enter 'y' or 'n'\n")


def main_menu() -> str:
    while True:
        print("\nWhat would you like to see?")
        print("  1 -> Demo all possible rook permutations on a blank 8x8 board")
        print("  2 -> Try on a partial board")
        print("  q -> Quit")
        uinput = input("> ").strip().lower()
        if uinput in ("12q"):
            return uinput
        print("Please select from the list.")


def print_solution(rooks, solver: Solver, ith_sol: str = "") -> None:
    board = solver.get_default_board()
    solver.clear_board()
    solver.place_rooks(locations=rooks)

    print(f"> Solution {ith_sol}")
    print(f" {'-'*len(board[0]*2)}")
    for row in board:
        print(f"|{' '.join(row)} |")
    print(f" {'-'*len(board[0]*2)}\n")


def print_solutions(solutions, solver: Solver) -> None:
    for i, sol in enumerate(solutions):
        print_solution(sol, solver, ith_sol=i + 1)


def run_main_demo(file_redirect, rook: str) -> None:
    solver = Solver(rchar=rook)
    solutions = solver.solve_board()
    if file_redirect:
        # Create if it doesnt exist:
        outdir = "data/out.txt"
        os.makedirs(os.path.dirname(outdir), exist_ok=True)
        original_stdout = sys.stdout

        print(f"Printing solution to {outdir}")
        with open(outdir, "w") as f:
            sys.stdout = f
            print_solutions(solutions, solver)
            sys.stdout = original_stdout
    else:
        print_solutions(solutions, solver)


def run_partial_demo(file_redirect, rook: str) -> None:
    solver = Solver(rchar=rook)
    print("\nEnter the rook locations as row, col separated by a space.")
    print("Example: 0 0 1 1 2 2")
    print("Press enter to solve.")
    rooks = []
    while True:
        uinput = input("> ").strip()
        if not uinput:
            break
        rooks.extend([int(x) for x in uinput.split()])

    if len(rooks) % 2 != 0:
        print("Please enter an even number of rook locations.")
        return

    rooks = [(rooks[i], rooks[i + 1]) for i in range(0, len(rooks), 2)]
    solver.set_rooks(set(rooks))
    solutions = solver.solve_board()
    if file_redirect:
        outdir = "data/out.txt"
        os.makedirs(os.path.dirname(outdir), exist_ok=True)
        original_stdout = sys.stdout

        print(f"Printing solution to {outdir}")
        with open(outdir, "w") as f:
            sys.stdout = f
            print_solutions(solutions, solver)
            sys.stdout = original_stdout
    else:
        print_solutions(solutions, solver)


if __name__ == "__main__":
    print("Welcome to Justin's Rook Permutation solver and simulator CLI!")
    print("Press ctrl+c to quit at any time.\n")

    try:
        unicode = get_yn("Do you see a rook -> ♜? y/n\n")
        rook_char = "♜" if unicode == "y" else "R"
        print(f"Got it, using {rook_char}\n")

        while True:
            choice = main_menu()
            if choice == "1":
                file_redirect = (
                    get_yn("\nWould you like to send this to a file?\n") == "y"
                )
                run_main_demo(file_redirect, rook_char)
            elif choice == "2":
                file_redirect = (
                    get_yn("\nWould you like to send this to a file?\n") == "y"
                )
                run_partial_demo(file_redirect, rook_char)
            elif choice == "q":
                print("\nGoodbye :)")
                break
    except KeyboardInterrupt:
        print("\nGoodbye :)")
        sys.exit(0)
