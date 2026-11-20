# 🐍 Snake Game (Python & Pygame)

A classic grid-based **Snake** game built with **Python** and **Pygame**, playable on a 15×15 checkerboard arena (maximum score: **224**).

## Prerequisites

- **Python 3.8+**
- **Pygame** (`pygame` or `pygame-ce`)
- The apple sprite file **`Pomme 1.png`** placed in the same directory as the script.

## Installation & Running

1. **Clone the repository and navigate to the project folder:**
   ```bash
   git clone [https://github.com/npautrat/my-python-begginer-program.git](https://github.com/npautrat/my-python-begginer-program.git)
   cd my-python-begginer-program
   ```

2. **Create a virtual environment and install Pygame:**
   - **Linux / macOS:**
     ```bash
     python3 -m venv .venv
     .venv/bin/python -m pip install pygame
     .venv/bin/python snake.py
     ```
   - **Windows:**
     ```powershell
     python -m venv .venv
     .venv\Scripts\python -m pip install pygame
     .venv\Scripts\python snake.py
     ```

## Controls & Rules

- **Arrow Keys (`↑`, `↓`, `←`, `→`)**: Start moving and change direction.
- **`Esc`**: Quit the game.
- Eat apples to grow longer and increase your score (`+1` per apple). Hitting the border or your own tail ends the game.
