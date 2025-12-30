#!/bin/bash

echo "GitHub Game Player - Auto Installer"
echo "==================================="
echo

# Function to detect the Linux distribution
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        DISTRO=$NAME
        DISTRO_ID=$ID
    elif type lsb_release >/dev/null 2>&1; then
        DISTRO=$(lsb_release -d | cut -f2)
        DISTRO_ID=$(lsb_release -i | cut -f2 | tr '[:upper:]' '[:lower:]')
    else
        DISTRO="Unknown"
        DISTRO_ID="unknown"
    fi
}

# Function to install build tools based on distribution
install_build_tools() {
    detect_distro
    echo "Detected distribution: $DISTRO ($DISTRO_ID)"
    
    case $DISTRO_ID in
        ubuntu|debian|linuxmint|pop|zorin)
            echo "Installing build tools for Debian/Ubuntu-based system..."
            sudo apt-get update
            sudo apt-get install -y build-essential g++ cmake
            ;;
        fedora|centos|rhel|rocky|almalinux)
            echo "Installing build tools for Red Hat-based system..."
            if command -v dnf &> /dev/null; then
                sudo dnf install -y gcc gcc-c++ make cmake
            else
                sudo yum install -y gcc gcc-c++ make cmake
            fi
            ;;
        arch|manjaro)
            echo "Installing build tools for Arch-based system..."
            sudo pacman -Syu --noconfirm
            sudo pacman -S --noconfirm gcc gcc-libs make cmake
            ;;
        opensuse*|sles)
            echo "Installing build tools for openSUSE-based system..."
            sudo zypper refresh
            sudo zypper install -y gcc gcc-c++ make cmake
            ;;
        *)
            echo "Unsupported distribution: $DISTRO_ID"
            echo "Please install build-essential, g++, and cmake manually."
            echo "For Debian/Ubuntu: sudo apt-get install build-essential g++ cmake"
            echo "For Fedora/CentOS/RHEL: sudo dnf install gcc gcc-c++ cmake (or yum on older systems)"
            echo "For Arch: sudo pacman -S gcc gcc-libs make cmake"
            echo "For openSUSE: sudo zypper install gcc gcc-c++ cmake"
            return 1
            ;;
    esac
}

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
    echo "g++ compiler not found. Installing build tools..."
    
    if command -v apt-get &> /dev/null; then
        # Debian/Ubuntu
        sudo apt-get update
        sudo apt-get install -y build-essential g++
    elif command -v dnf &> /dev/null; then
        # Fedora
        sudo dnf install -y gcc gcc-c++ make
    elif command -v yum &> /dev/null; then
        # CentOS/RHEL
        sudo yum install -y gcc gcc-c++ make
    elif command -v pacman &> /dev/null; then
        # Arch Linux
        sudo pacman -Syu --noconfirm gcc gcc-libs make
    elif command -v zypper &> /dev/null; then
        # openSUSE
        sudo zypper install -y gcc gcc-c++ make
    else
        echo "No supported package manager found."
        install_build_tools
    fi
    
    # Check again if g++ is now available
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