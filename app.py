from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_caching import Cache
from pysolver.solver import Solver

app = Flask(__name__)
CORS(app)
cache = Cache(app, config={"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 300})


@app.route("/")
def home():
    return "Welcome to Justin's Rook Permutation solver API!"


@cache.memoize(timeout=300)  # 5min
def get_solutions(rooks):
    solver = Solver()
    solver.set_rooks(set(tuple(r) for r in rooks))
    return solver.solve_board()


@app.route("/solve", methods=["POST"])
def solve():
    data = request.json
    if not data:
        return (
            jsonify(
                {"ierror": "POST /solve bad request", "error": "Missing 'rooks' data"}
            ),
            400,
        )

    rooks = data.get("rooks", [])
    page = data.get("page", 1)
    per_page = data.get("per_page", 10)

    rooks_set = frozenset(tuple(r) for r in rooks)

    try:
        solutions = get_solutions(rooks_set)
    except ValueError as e:
        return jsonify(
            {
                "ierror": "POST /solve bad request",
                "error": str(e),
                "solutions": [],
                "number_of_solutions": 0,
            },
            400,
        )

    total_solutions = len(solutions)
    start = (page - 1) * per_page
    end = start + per_page
    page_solutions = solutions[start:end]
    solutions_list = [list(sol) for sol in page_solutions]

    return jsonify(
        {"solutions": solutions_list, "number_of_solutions": total_solutions}, 200
    )


if __name__ == "__main__":
    app.run(debug=True)
