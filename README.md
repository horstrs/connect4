# Connect 4 CLI

A Python implementation of Connect 4 featuring a decoupled MVC architecture and a customizable CLI View.

:dart: **Short term goal of the project was to practice:**

* :building_construction: Architecture skills by creating a decoupled MVC architecture
* :test_tube: Learn testing in python, and validate how decoupled the original architecture was by how many changes I had to make to implementing unit tests

:books: **Mid/Long term goal of the project is to:**

* :robot: Learn/Practice implementation of more complex AI algorithms like minimax and their optimizations
* :scissors: For Alpha-Beta pruning, the creation of a score heuristic will be fun to do
* :brain: Learn implementation of Machine Learning algorithms for AI player, like neural networks
* :globe_with_meridians: Since back-end architecture is decoupled, this can serve as a basis for a future webserver project



## 🚀 Setup

1. **Install UV:**

    https://docs.astral.sh/uv/getting-started/installation/


2. **Clone the repository:**
   ```bash
   git clone <https://github.com/horstrs/connect4>
   cd connect4_project
   ```

3. **Install dependencies:**
    ```bash
    uv sync
    ```

Alternatively, if wnat to just run it once, you can use uvx to replace steps 2 and 3 above with this:

2. **Run using uvx:**
    ```bash
    uvx --from git+https://github.com/horstrs/connect4 play
    ```

## 🎮 How to Play
Run the game from the root directory:

```bash
uv run play
```

## 🧪 Testing & Coverage
Run tests:

``` bash
pytest
```

Check coverage:
```bash
pytest --cov=src --cov-report=term-missing
```

## 🛠 Configuration
You can change player colors and symbols in src/config.py without touching the game logic.

```Python
# Change "red" to "blue" or "X" to "P"
PLAYERS_CONFIG = {
    1: {"COLOR": "red", "SHAPE": "X"},
    2: {"COLOR": "yellow", "SHAPE": "O"}
} 
```

