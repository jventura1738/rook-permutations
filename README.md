# Rook Permutation Simulator

by Justin Ventura

## Features:

1. CLI using my pysolver to solve rook permutations problem
2. Flask API to provide a RESTful interface to the pysolver
3. Serverside caching and pagination of solutions to improve UX
4. React client to interact with the API and display solutions beautifully

## Installation:

Prerequisites:

1. Have Python installed, preferably version >=3.11
2. You can check your version using `python --version`
3. Have pip and npm installed
4. Make sure you also have TypeScript installed

To setup this project:

1. Clone the repo `git clone https://github.com/jventura1738/rook-permutations.git`. Note that you likely don't have access, you can email me at justinventura.tech@gmail.com for access to the repository. Otherwise, you can just skip this step
2. Navigate into the project dir `cd rook-permutations`
3. Create a python virtual environment `python3 -m venv venv`
4. Activate it `source venv/bin/activate`
5. Install the requirements `pip install -r requirements.txt`

## Running the CLI app:

To run the CLI:

```bash
python main.py
```

Example usage:

```
python3 main.py                                                                                                    ─╯
Welcome to Justin's Rook Permutation solver and simulator CLI!
Press ctrl+c to quit at any time.

Do you see a rook -> ♜? y/n
> y
Got it, using ♜


What would you like to see?
  1 -> Demo all possible rook permutations on a blank 8x8 board
  2 -> Try on a partial board
  q -> Quit
> 2

Would you like to send this to a file?
> n

Enter the rook locations as row, col separated by a space.
Example: 0 0 1 1 2 2
Press enter to solve.
> 0 0 1 1 2 2 4 4 7 7

> Solution 1
 ----------------
|♜ . . . . . . . |
|. ♜ . . . . . . |
|. . ♜ . . . . . |
|. . . ♜ . . . . |
|. . . . ♜ . . . |
|. . . . . ♜ . . |
|. . . . . . ♜ . |
|. . . . . . . ♜ |
 ----------------

> Solution 2
 ----------------
|♜ . . . . . . . |
|. ♜ . . . . . . |
|. . ♜ . . . . . |
|. . . ♜ . . . . |
|. . . . ♜ . . . |
|. . . . . . ♜ . |
|. . . . . ♜ . . |
|. . . . . . . ♜ |
 ----------------

> Solution 3
 ----------------
|♜ . . . . . . . |
|. ♜ . . . . . . |
|. . ♜ . . . . . |
|. . . . . ♜ . . |
|. . . . ♜ . . . |
|. . . ♜ . . . . |
|. . . . . . ♜ . |
|. . . . . . . ♜ |
 ----------------

> Solution 4
 ----------------
|♜ . . . . . . . |
|. ♜ . . . . . . |
|. . ♜ . . . . . |
|. . . . . ♜ . . |
|. . . . ♜ . . . |
|. . . . . . ♜ . |
|. . . ♜ . . . . |
|. . . . . . . ♜ |
 ----------------

> Solution 5
 ----------------
|♜ . . . . . . . |
|. ♜ . . . . . . |
|. . ♜ . . . . . |
|. . . . . . ♜ . |
|. . . . ♜ . . . |
|. . . ♜ . . . . |
|. . . . . ♜ . . |
|. . . . . . . ♜ |
 ----------------

> Solution 6
 ----------------
|♜ . . . . . . . |
|. ♜ . . . . . . |
|. . ♜ . . . . . |
|. . . . . . ♜ . |
|. . . . ♜ . . . |
|. . . . . ♜ . . |
|. . . ♜ . . . . |
|. . . . . . . ♜ |
 ----------------


What would you like to see?
  1 -> Demo all possible rook permutations on a blank 8x8 board
  2 -> Try on a partial board
  q -> Quit
> q

Goodbye :)
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

## Running the client:

After starting the Flask API, you can run the client with:

```bash
npm i && npm start
```

Omit the `npm i` if you've already installed the dependencies. This will open a browser window with the client.

You can begin to click on the board to place rooks, and then click the solve button to see the solutions!

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

1. If `python` doesn't work, try `python3`. You can also alias this in your bash/zsh profile
2. Make sure you run each of the above commands from the root directory
3. If you have any issues, please email me at justinventura.tech at gmail

## Future work

1. Having a dockerized container would be nice for portability, hopefully can get to this. If not by the deadline, will be nice to have in general
2. A button to clear the board would be nice
3. (mostly) Hard coded for 8x8 board, would be cool to scale up/down
