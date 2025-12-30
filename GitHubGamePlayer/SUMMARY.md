# GitHub Game Player - Summary

## Overview
This is a multi-language game platform that integrates popular games from GitHub projects. The application is built primarily in C++ with support for games written in multiple languages. The enhanced launchers now include automatic installation of required build tools.

## Languages Used
1. **C++** - Main application
2. **Python** - Snake, Pong, Chess games
3. **JavaScript** - Tetris, Pacman, Sudoku games
4. **HTML/CSS** - 2048 game
5. **Batch** - Launcher script
6. **CMake** - Build system
7. **Shell** - Test script

## Games Integrated
1. **Snake** - Python implementation
2. **Tetris** - JavaScript implementation
3. **Minesweeper** - C++ implementation
4. **2048** - HTML/JavaScript implementation
5. **Pong** - Python implementation
6. **Pacman** - JavaScript implementation
7. **Chess** - Python implementation
8. **Sudoku** - JavaScript implementation

## Launch Scripts
The project includes several launch scripts to make it easy to run the application:

### Basic Launchers
- `launch.bat` - Basic Windows launcher
- `launch.sh` - Basic Linux launcher

### Enhanced Launchers (Recommended)
- `launch_enhanced.bat` - Enhanced Windows launcher with auto-installation
- `launch_enhanced.sh` - Enhanced Linux launcher with auto-installation

## Auto-Installation Features
The enhanced launchers automatically handle the installation of required build tools if they're not already installed:

### Windows Auto-Installation
- Checks if `GitHubGamePlayer.exe` exists
- If not, checks if g++ compiler is available
- If g++ is not found, attempts to install via:
  - Chocolatey (if available) - installs mingw or tdm-gcc
  - Winget (if available) - installs winlibs.mingw-w64
  - Scoop (if available) - installs mingw
  - Offline installer download and extraction (using PowerShell and 7-Zip)
  - Provides manual installation instructions if all automatic methods fail
- Compiles the application
- Runs the executable

### Linux Auto-Installation
- Checks if `GitHubGamePlayer` executable exists
- If not, checks if g++ compiler is available
- If g++ is not found, detects the Linux distribution and installs appropriate build tools:
  - Debian/Ubuntu: build-essential, g++, cmake
  - Fedora/CentOS/RHEL: gcc, gcc-c++, make, cmake
  - Arch Linux: gcc, gcc-libs, make, cmake
  - openSUSE: gcc, gcc-c++, make, cmake
- Compiles the application
- Runs the executable

## Project Structure
```
GitHubGamePlayer/
├── src/
│   └── main.cpp (C++ main application)
├── games/
│   ├── snake/ (Python)
│   ├── tetris/ (JavaScript)
│   ├── minesweeper/ (C++)
│   ├── 2048/ (HTML/JS)
│   ├── pong/ (Python)
│   ├── pacman/ (JavaScript)
│   ├── chess/ (Python)
│   └── sudoku/ (JavaScript)
├── launch.bat (Windows launcher)
├── launch.sh (Linux launcher)
├── launch_enhanced.bat (Enhanced Windows launcher with auto-installation)
├── launch_enhanced.sh (Enhanced Linux launcher with auto-installation)
├── CMakeLists.txt (Build configuration)
├── README.md (Project documentation)
├── AUTOINSTALL_README.md (Auto-installation documentation)
├── GitHubGamePlayer (Compiled executable)
└── test_games.sh (Test script)
```

## How to Run
1. **Auto-Installation (Recommended)**: Use `launch_enhanced.bat` (Windows) or `launch_enhanced.sh` (Linux)
2. **Basic**: Double-click `launch.bat` (Windows) or run `launch.sh` (Linux)
3. **Direct**: Run the executable directly

## Features
- Play popular games for free
- Integrated GitHub project files
- Multi-language support
- Easy to use launcher
- Auto-installation of required build tools
- Cross-platform compatibility

## Build Instructions
1. Compile with: `g++ src/main.cpp -o GitHubGamePlayer`
2. Or use CMake: `cmake . && make`
3. Run the executable to start the game player

This application demonstrates integration of multiple game projects from GitHub into a single player application with automatic build tool installation.