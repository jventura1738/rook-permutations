# Rook Permutation Simulator

by Justin Ventura

## Installation:

Prerequisites:
1. Have Python installed, preferably version >=3.11
2. You can check your version using `python --version`

To setup this project:

1. Clone the repo `git clone https://github.com/jventura1738/rook-permutations.git`. Note that you likely don't have access, you can email me at justinventura.tech@gmail.com for access to the repository. Otherwise, you can just skip this step.
2. Navigate into the project dir `cd rook-permutations`
3. Create a python virtual environment `python -m venv venv`
4. Activate it `source venv/bin/activate`
5. Install the requirements `pip install -r requirements.txt`

## Running:

To run the project:

```bash
python main.py
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

## Future work

Having a dockerized container would be nice for portability, hopefully can get to this. If not by the deadline, will be nice to have in general.
