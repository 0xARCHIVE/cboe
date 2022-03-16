# Cboe Coding Test

![Python >= 3.10.2](https://img.shields.io/badge/python-%3E%3D%203.10.2-blue?style=flat-square) ![Testing TBD%](https://img.shields.io/badge/coverage-TBD%25-red?style=flat-square)

## Installation

I have chosen to use `poetry` and `pyenv`. To setup and use the environment:

```shell
poetry install
poetry shell
```

This will automatically create a virtual environment and install the required dependencies.

## Usage

Supply PITCH messages to STDIN separated by newline characters (e.g. using the supplied file `data`):

```shell
python main.py < ./data
```

The output will be the top 10 symbols by execution volume:

```
OIH 5000
SPY 2000
DRYS 1209
ZVZZT 577
AAPL 495
PTR 400
UYG 400
FXP 320
DIA 229
BAC 210
```


## Development

### Pre-commit Checks

To run them manually:

```shell
pre-commit run --all-files
```

This will run a series of linting and type-checking (`flake8`, `black`, `mypy`) and tell you what needs to be fixed. You may need to run it more than once. It will be automatically run when attempting to commit a change.

### Testing

To run tests:

```shell
pytest
```

For test coverage:

```shell
pytest --cov=keypad tests/
```
