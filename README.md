# Game Server

A localhost-based game server built with .NET 6 that serves various browser-based games.

## Features

- Hosts multiple classic games in the browser
- Modern UI with responsive design
- Easy to extend with additional games
- Runs locally on your machine

## Included Games

- **Tic Tac Toe**: Classic X and O game for two players
- **Snake**: Control the snake to eat food and grow
- **Pong**: Classic two-player arcade game

## How to Run

1. Make sure you have .NET 6 installed on your system
2. Run the main launcher:
   ```bash
   ./main_launch.bat    # On Windows
   ```
   or
   ```bash
   chmod +x main_launch.sh && ./main_launch.sh  # On Linux/Mac
   ```
3. Open your browser and navigate to `http://localhost:5000`
4. Select a game from the main menu to play

## Adding New Games

To add a new game:

1. Create a new folder under `/wwwroot/games/` with your game name
2. Add an `index.html` file with your game implementation
3. Include CSS and JavaScript files as needed
4. Update the main index.html to include a link to your new game

## Architecture

- Backend: .NET 6 Web Application serving static files
- Frontend: HTML, CSS, and JavaScript for each game
- Structure: Each game has its own folder with its assets

## Technologies Used

- .NET 6
- ASP.NET Core
- HTML5
- CSS3
- JavaScript (ES6+)
- Canvas API (for games)

## Development

The application is designed to be easily extensible. Each game is self-contained in its own directory under `/wwwroot/games/`, making it easy to add, remove, or modify games independently.