from flask import Flask, jsonify, request
from pysolver.solver import Solver

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Justin's Rook Permutation solver API!"


@app.route("/solve", methods=["POST"])
def solve():
    data = request.json
    if not data:
        return jsonify({"error": "POST /solve bad request; missing 'rooks'"}), 400

    rooks = data.get("rooks", [])

    solver = Solver()
    success = solver.set_rooks(set(tuple(r) for r in rooks))
    if not success:
        return jsonify(
            {"error": "POST /solve bad request; rooks must not be attacked"}, 400
        )

    solutions = solver.solve_board()
    solutions_list = [list(sol) for sol in solutions]

    return jsonify(
        {"solutions": solutions_list, "number_of_solutions": len(solutions_list)}, 200
    )


if __name__ == "__main__":
    app.run(debug=True)
