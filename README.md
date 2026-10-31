# test-code

A small test repository for practicing Git and GitHub workflows (branches, commits, pull requests).

## Contents

- `hello_world.py`: a simple Python script with a reusable `greet(name)` function.
- `.gitignore`: ignores the `.idea/` folder created by JetBrains IDEs.

## Usage

Requires Python 3.

```bash
python hello_world.py
```

Expected output:

```
Hello, World!
Hello, Bharath!
```

To reuse the greeting in your own code:

```python
from hello_world import greet

print(greet("Alice"))  # Hello, Alice!
```
