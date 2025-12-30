# GitHub Game Player

A multi-language game platform that integrates popular games from GitHub projects.

## Features
- Play popular games for free
- Integrated GitHub project files
- Multi-language support (C++, Python, JavaScript, etc.)
- Easy to use batch file launcher

## Supported Languages
- C++ (main application)
- Python
- JavaScript
- HTML/CSS
- Batch files

## Games Included
- Snake
- Tetris
- Minesweeper
- 2048
- Pong
- Pacman
- Chess
- Sudoku

## How to Run
### Option 1: Auto-Installation (Recommended)
The enhanced launch scripts automatically install required build tools if not present:

- **Windows**: Run `launch_enhanced.bat` - automatically installs MinGW-w64 or TDM-GCC if needed
- **Linux**: Run `launch_enhanced.sh` - automatically installs build-essential if needed

### Option 2: Manual Setup
1. Make sure you have C++ compiler installed
2. Compile the main application: `g++ src/main.cpp -o GitHubGamePlayer`
3. Run the executable: `./GitHubGamePlayer` (Linux/Mac) or `GitHubGamePlayer.exe` (Windows)
4. Or run the original batch file: `launch.bat` (Windows)

## Project Structure
```
GitHubGamePlayer/
├── src/
│   └── main.cpp
├── games/
│   ├── snake/
│   ├── tetris/
│   ├── minesweeper/
│   ├── 2048/
│   ├── pong/
│   ├── pacman/
│   ├── chess/
│   └── sudoku/
├── launch.bat
├── README.md
└── CMakeLists.txt
```