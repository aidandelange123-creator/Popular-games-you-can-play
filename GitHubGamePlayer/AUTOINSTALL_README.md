# Auto-Installer Scripts for GitHub Game Player

## Overview
This directory contains enhanced launch scripts that automatically handle the installation of required build tools (MinGW-w64 or TDM-GCC on Windows, build-essential on Linux) if they're not already installed on your system.

## Features
- **Automatic Detection**: Checks if the required compiler (g++) is already installed
- **Auto Installation**: If not installed, automatically installs MinGW-w64, TDM-GCC (Windows) or build-essential (Linux)
- **Cross-Platform**: Works on both Windows and Linux systems
- **Smart Compilation**: Compiles the application only if needed
- **Auto Execution**: Runs the application after successful compilation

## Files Included
- `launch_enhanced.bat` - Enhanced Windows batch script with auto-installation
- `launch_enhanced.sh` - Enhanced Linux bash script with auto-installation

## How It Works

### Windows (launch_enhanced.bat)
1. Checks if `GitHubGamePlayer.exe` exists
2. If not, checks if g++ compiler is available
3. If g++ is not found, attempts to install via:
   - Chocolatey (if available) - installs mingw or tdm-gcc
   - Winget (if available) - installs winlibs.mingw-w64
   - Provides manual installation instructions if automatic methods fail
4. Compiles the application
5. Runs the executable

### Linux (launch_enhanced.sh)
1. Checks if `GitHubGamePlayer` executable exists
2. If not, checks if g++ compiler is available
3. If g++ is not found, detects the Linux distribution and installs appropriate build tools:
   - Debian/Ubuntu: build-essential, g++, cmake
   - Fedora/CentOS/RHEL: gcc, gcc-c++, make, cmake
   - Arch Linux: gcc, gcc-libs, make, cmake
   - openSUSE: gcc, gcc-c++, make, cmake
4. Compiles the application
5. Runs the executable

## Supported Package Managers
### Windows
- Chocolatey
- Winget (Windows Package Manager)

### Linux
- APT (Debian/Ubuntu)
- DNF/YUM (Fedora/CentOS/RHEL)
- Pacman (Arch Linux)
- Zypper (openSUSE)

## Requirements
- Windows: Administrator privileges for package installation (when needed)
- Linux: Sudo access for package installation (when needed)

## Usage
Simply run the appropriate script for your platform:
- Windows: Double-click `launch_enhanced.bat` or run from command prompt
- Linux: Run `./launch_enhanced.sh` from terminal

The script will handle everything automatically - from installing the compiler if needed to compiling and running the game application.