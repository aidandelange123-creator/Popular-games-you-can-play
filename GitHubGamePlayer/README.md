# GitHub Game Player

A multi-language game platform that integrates popular games from GitHub projects.
Now available in both C++ and .NET versions!

## Features
- Play popular games for free
- Integrated GitHub project files
- Multi-language support (C++, Python, JavaScript, etc.)
- Easy to use batch file launcher
- .NET version available for better cross-platform compatibility

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
- Tic Tac Toe
- Space Invaders
- Breakout

## How to Run
### Option 1: .NET Version (New Recommended)
The .NET version provides better cross-platform compatibility and easier setup:

- **Windows**: Run `launch_dotnet.bat` - automatically installs .NET if needed
- **Linux**: Run `launch_dotnet.sh` - automatically installs .NET if needed

### Option 2: Auto-Installation (C++ Version)
The enhanced launch scripts automatically install required build tools if not present:

- **Windows**: Run `launch_enhanced.bat` - automatically installs MinGW-w64 or TDM-GCC if needed
- **Linux**: Run `launch_enhanced.sh` - automatically installs build-essential if needed

### Option 3: Manual Setup
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
│   ├── sudoku/
│   ├── tictactoe/
│   ├── spaceinvaders/
│   └── breakout/
├── launch.bat
├── README.md
└── CMakeLists.txt
```