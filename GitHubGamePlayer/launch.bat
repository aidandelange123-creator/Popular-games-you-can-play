@echo off
title GitHub Game Player

echo GitHub Game Player
echo ==================
echo.

REM Check if the executable exists
if exist "GitHubGamePlayer.exe" (
    echo Starting GitHub Game Player...
    GitHubGamePlayer.exe
    goto end
)

REM If executable doesn't exist, try to compile
echo Executable not found. Compiling the application...
echo Checking for g++ compiler...

REM Check if g++ is available
g++ --version >nul 2>&1
if errorlevel 1 (
    echo g++ compiler not found. Installing MinGW-w64...
    echo Please wait...
    
    REM Download and install MinGW-w64 (this is a simplified version)
    REM In a real scenario, you might want to provide instructions for manual installation
    echo Please install MinGW-w64 or TDM-GCC to compile the application.
    echo Visit: https://www.mingw-w64.org/downloads/ or http://tdm-gcc.tdragon.net/
    echo.
    pause
    goto end
)

REM Compile the main application with all game files
echo Compiling GitHub Game Player...
g++ -o GitHubGamePlayer.exe src/main.cpp src/snake.cpp src/tetris.cpp src/minesweeper.cpp src/twenty_forty_eight.cpp src/pong.cpp src/pacman.cpp src/chess.cpp src/sudoku.cpp -lncurses -lSDL2 -lSDL2main -lSDL2_image -lSDL2_mixer -lSDL2_ttf

if errorlevel 1 (
    echo Compilation failed. Please check your compiler setup.
    echo Make sure you have the required libraries installed.
    pause
    goto end
)

echo Compilation successful!
echo Starting GitHub Game Player...
GitHubGamePlayer.exe

:end
pause