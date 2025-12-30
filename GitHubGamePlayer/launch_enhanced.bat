@echo off
title GitHub Game Player - Auto Installer

echo GitHub Game Player - Auto Installer
echo ================================
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
    call :install_mingw
    if errorlevel 1 (
        echo Failed to install MinGW-w64 or TDM-GCC.
        echo Please install manually from:
        echo - https://www.mingw-w64.org/downloads/
        echo - http://tdm-gcc.tdragon.net/
        pause
        goto end
    )
)

REM Compile the main application with all game files
echo Compiling GitHub Game Player...
g++ -o GitHubGamePlayer.exe src/main.cpp src/snake.cpp src/tetris.cpp src/minesweeper.cpp src/twenty_forty_eight.cpp src/pong.cpp src/pacman.cpp src/chess.cpp src/sudoku.cpp

if errorlevel 1 (
    echo Compilation failed. Please check your compiler setup.
    pause
    goto end
)

echo Compilation successful!
echo Starting GitHub Game Player...
GitHubGamePlayer.exe

:end
pause
exit /b 0

REM Function to install MinGW-w64 or TDM-GCC
:install_mingw
    echo Attempting to install MinGW-w64 or TDM-GCC...
    
    REM Check if chocolatey is installed
    choco --version >nul 2>&1
    if errorlevel 1 (
        goto try_winget
    ) else (
        goto install_with_choco
    )
    
    :try_winget
    echo Chocolatey not found. Trying winget...
    winget --version >nul 2>&1
    if errorlevel 1 (
        goto try_scoop
    ) else (
        echo Installing MinGW-w64 using winget...
        winget install --id=winlibs.mingw-w64 -e
        if errorlevel 1 (
            echo Winget installation failed.
            goto try_scoop
        ) else (
            REM Add to PATH temporarily
            set "PATH=%PATH%;C:\mingw64\bin"
            goto check_compiler
        )
    )
    
    :try_scoop
    echo Winget not found or installation failed. Trying scoop...
    scoop --version >nul 2>&1
    if errorlevel 1 (
        goto try_offline_installer
    ) else (
        echo Installing MinGW-w64 using Scoop...
        scoop install mingw
        if errorlevel 1 (
            echo Scoop installation failed.
            goto try_offline_installer
        ) else (
            REM Add to PATH temporarily
            set "PATH=%PATH%;%USERPROFILE%\scoop\apps\mingw\current\bin"
            goto check_compiler
        )
    )
    
    :install_with_choco
    echo Installing MinGW-w64 using Chocolatey...
    choco install mingw -y
    if errorlevel 1 (
        echo Chocolatey installation failed, trying TDM-GCC...
        choco install tdm-gcc -y
        if errorlevel 1 (
            echo Both Chocolatey installations failed.
            goto try_offline_installer
        )
    )
    REM Refresh PATH
    call refreshenv >nul 2>&1
    goto check_compiler
    
    :try_offline_installer
    echo All package managers failed. Downloading offline installer...
    echo This requires PowerShell for download.
    
    REM Create a temporary directory
    if not exist "temp_install" mkdir temp_install
    cd temp_install
    
    REM Try to download MinGW-w64 using PowerShell
    powershell -Command "Invoke-WebRequest -Uri 'https://github.com/niXman/mingw-builds-binaries/releases/latest/download/x86_64-13.2.0-release-posix-seh-msvcrt-rt_v11-rev0.7z' -OutFile 'mingw.7z'" >nul 2>&1
    
    if errorlevel 1 (
        echo Failed to download installer automatically.
        goto manual_install_instructions
    ) else (
        echo Downloaded MinGW-w64. Extracting...
        REM Try to extract using 7z if available, otherwise use PowerShell
        7z x mingw.7z >nul 2>&1
        if errorlevel 1 (
            powershell -Command "Expand-Archive -Path 'mingw.7z' -DestinationPath '.'" >nul 2>&1
        )
        
        REM Find the extracted directory and move it to C:\mingw64
        for /d %%i in (x86_64-*) do (
            move "%%i" "..\mingw64" >nul 2>&1
            break
        )
        
        cd ..
        
        REM Add to PATH temporarily
        set "PATH=%PATH%;%CD%\mingw64\bin"
        echo Added MinGW-w64 to PATH temporarily.
        goto check_compiler
    )
    
    :manual_install_instructions
    echo.
    echo Automatic installation failed.
    echo Please install MinGW-w64 manually:
    echo 1. Download from: https://www.mingw-w64.org/downloads/
    echo 2. Or use the online installer from: https://github.com/niXman/mingw-builds-binaries/releases
    echo 3. Add the bin directory to your system PATH
    echo 4. Restart this script
    echo.
    echo Press any key to exit...
    pause >nul
    exit /b 1

:check_compiler
    REM Wait a moment for PATH to update
    timeout /t 3 /nobreak >nul
    
    REM Check if g++ is now available
    g++ --version >nul 2>&1
    if errorlevel 1 (
        echo Compiler still not found after installation.
        echo Please ensure MinGW-w64 or TDM-GCC is properly installed and in PATH.
        exit /b 1
    ) else (
        echo Compiler successfully installed!
        exit /b 0
    )