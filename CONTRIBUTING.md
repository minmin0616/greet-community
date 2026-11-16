# Contributing to greet-community

## Set up for development

From the project root, activate a Python 3.11+ virtual environment and run:

```sh
python -m pip install -e .
```

## Run the tests

```sh
python -c "from greet_community import greet; print(greet('Hee'))"
```

Expected output: `Hello, Hee!`

## Send a change

Start from `main` and create a branch with `git switch -c your-branch`.
Make your change, stage it with `git add`, and commit it with `git commit`.
Push with `git push -u origin your-branch` and open a pull request into `main`.
