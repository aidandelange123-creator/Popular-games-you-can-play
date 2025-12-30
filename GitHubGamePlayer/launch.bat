@echo off
title GitHub Game Player

echo Welcome to GitHub Game Player!
echo ===============================
echo.

REM Check if the executable exists
if exist "GitHubGamePlayer.exe" (
    echo Launching GitHub Game Player...
    GitHubGamePlayer.exe
) else (
    echo GitHub Game Player executable not found.
    echo Compiling the application...
    g++ src/main.cpp -o GitHubGamePlayer.exe
    if errorlevel 1 (
        echo Compilation failed. Please make sure you have g++ installed.
        pause
        exit /b 1
    )
    echo Compilation successful. Launching...
    GitHubGamePlayer.exe
)

pause