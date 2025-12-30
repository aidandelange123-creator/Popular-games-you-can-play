@echo off
title GitHub Game Player (.NET)

echo Checking for .NET installation...

REM Check if dotnet is available
dotnet --version >nul 2>&1
if %errorlevel% neq 0 (
    echo .NET is not installed on this system.
    echo Installing .NET...
    
    REM Try to install .NET using winget (Windows 10/11)
    winget install Microsoft.DotNet.SDK.6 --source winget >nul 2>&1
    if %errorlevel% neq 0 (
        echo Winget installation failed.
        echo Please install .NET SDK manually from:
        echo https://dotnet.microsoft.com/download
        pause
        exit /b 1
    ) else (
        echo .NET SDK installed successfully.
    )
) else (
    echo .NET is already installed.
)

echo Changing to .NET project directory...
cd /d "%~dp0dotnet"

echo Building .NET application...
dotnet build -c Release

if %errorlevel% neq 0 (
    echo Failed to build the application.
    pause
    exit /b 1
)

echo Running GitHub Game Player...
dotnet run --project . --configuration Release

pause