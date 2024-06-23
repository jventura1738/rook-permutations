# Rook Permutation Simulator

by Justin Ventura

## Installation:

Prerequisites:
1. Have Python installed, preferably version >=3.11
2. You can check your version using `python --version`

To setup this project:

1. Clone the repo `git clone https://github.com/jventura1738/rook-permutations.git`. Note that you likely don't have access, you can email me at justinventura.tech@gmail.com for access to the repository. Otherwise, you can just skip this step
2. Navigate into the project dir `cd rook-permutations`
3. Create a python virtual environment `python -m venv venv`
4. Activate it `source venv/bin/activate`
5. Install the requirements `pip install -r requirements.txt`

## Running the CLI app:

To run the CLI:

```bash
python main.py
```

## Running the Flask API:

You should open this in another terminal. Assuming you have successfully completed installation, run:

```bash
python app.py
```

You can try a request with curl:

```bash
curl -X POST http://127.0.0.1:5000/solve -H "Content-Type: application/json" -d '{"rooks": [[0, 0]]}'
```

This output is probably huge, so you can try a smaller one:

```bash
curl -X POST http://127.0.0.1:5000/solve -H "Content-Type: application/json" -d '{"rooks": [[0, 0], [1,1], [2,2], [3,3], [4,4], [5,5], [6,6]]}'
```

Which should output:

```bash
[
  {
    "number_of_solutions": 1,
    "solutions": [
      [
        [
          4,
          4
        ],
        [
          5,
          5
        ],
        [
          7,
          7
        ],
        [
          0,
          0
        ],
        [
          1,
          1
        ],
        [
          3,
          3
        ],
        [
          2,
          2
        ],
        [
          6,
          6
        ]
      ]
    ]
  },
  200
]
```

### Dev:

**Testing:** To run verification of the pysolver, ensure you've been able to successfully install, then run:

```bash
pytest
```

**Formatting:** This should happen on commit, but you can also force it by running:

```bash
pre-commit run --all-files
```

### Troubleshooting:

1. If `python` doesn't work, try `python3`.  You can also alias this in your bash/zsh profile
2. Make sure you run each of the above commands from the root directory

## Future work

Having a dockerized container would be nice for portability, hopefully can get to this. If not by the deadline, will be nice to have in general
