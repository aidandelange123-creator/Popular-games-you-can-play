#!/bin/bash

echo "Starting Game Server..."
echo

# Navigate to the game server directory
cd "$(dirname "$0")/game_server/GameServer"

# Run the .NET 6 application
echo "Launching Game Server on http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo
dotnet run --urls=http://localhost:5000