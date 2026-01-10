@echo off
echo Starting Game Server...
echo.

REM Navigate to the game server directory
cd /d "%~dp0game_server\GameServer"

REM Run the .NET 6 application
echo Launching Game Server on http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
dotnet run --urls=http://localhost:5000

pause