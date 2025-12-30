# GitHub Game Player (.NET Version)

This is the .NET implementation of the GitHub Game Player application. It provides a unified interface to various games available on GitHub, now built with .NET technology.

## Features

- Unified interface for multiple games
- Cross-platform compatibility (.NET)
- Automatic .NET installation if not present
- Easy one-click launch

## Games Available

- Snake
- Tetris
- Minesweeper
- 2048
- Pong
- Pacman
- Chess
- Sudoku

## Quick Start

### Windows
Run the batch file:
```
launch_dotnet.bat
```

### Linux
Run the shell script:
```bash
./launch_dotnet.sh
```

Both scripts will:
1. Check if .NET is installed
2. Automatically install .NET if needed
3. Build the application
4. Run the GitHub Game Player

## Requirements

- .NET 6.0 SDK (will be installed automatically if missing)

## Building Manually

If you prefer to build manually:

```bash
cd dotnet
dotnet build -c Release
dotnet run --configuration Release
```

## .NET Installation (Manual)

If automatic installation fails, you can install .NET manually:

- Download from: https://dotnet.microsoft.com/download
- Choose .NET 6.0 SDK for your platform
- Follow the installation instructions for your OS