#!/bin/bash

echo "GitHub Game Player"
echo "=================="
echo

# Check if the executable exists
if [ -f "GitHubGamePlayer" ]; then
    echo "Starting GitHub Game Player..."
    ./GitHubGamePlayer
    exit 0
fi

# If executable doesn't exist, try to compile
echo "Executable not found. Compiling the application..."
echo "Checking for g++ compiler..."

# Check if g++ is available
if ! command -v g++ &> /dev/null; then
    echo "g++ compiler not found. Installing g++..."
    sudo apt-get update
    sudo apt-get install -y build-essential
    
    if ! command -v g++ &> /dev/null; then
        echo "Failed to install g++ compiler."
        echo "Please install g++ manually."
        exit 1
    fi
fi

echo "g++ compiler found. Compiling GitHub Game Player..."
g++ -o GitHubGamePlayer src/main.cpp src/snake.cpp src/tetris.cpp src/minesweeper.cpp src/twenty_forty_eight.cpp src/pong.cpp src/pacman.cpp src/chess.cpp src/sudoku.cpp

if [ $? -ne 0 ]; then
    echo "Compilation failed. Please check your compiler setup."
    exit 1
fi

echo "Compilation successful!"
echo "Starting GitHub Game Player..."
./GitHubGamePlayer