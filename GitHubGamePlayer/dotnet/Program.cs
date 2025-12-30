using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;

namespace GitHubGamePlayer
{
    class Program
    {
        static void Main(string[] args)
        {
            GamePlayer player = new GamePlayer();
            player.Run();
        }
    }

    class GamePlayer
    {
        private Dictionary<string, string> games;

        public GamePlayer()
        {
            // Initialize popular games from GitHub
            games = new Dictionary<string, string>
            {
                {"snake", "Python Snake Game"},
                {"tetris", "JavaScript Tetris"},
                {"minesweeper", "C++ Minesweeper"},
                {"2048", "HTML/JS 2048"},
                {"pong", "Python Pong"},
                {"pacman", "JavaScript Pacman"},
                {"chess", "Python Chess"},
                {"sudoku", "JavaScript Sudoku"}
            };
        }

        public void DisplayMenu()
        {
            Console.WriteLine("\n========================================");
            Console.WriteLine("    GITHUB GAME PLAYER - MAIN MENU");
            Console.WriteLine("========================================");
            Console.WriteLine("Available Games:\n");

            int index = 1;
            foreach (var game in games)
            {
                Console.WriteLine($"{index}. {game.Value} ({game.Key})");
                index++;
            }

            Console.WriteLine("\n0. Exit");
            Console.WriteLine("========================================");
            Console.Write("Enter your choice: ");
        }

        public void PlayGame(string gameName)
        {
            Console.WriteLine($"\nLaunching {games[gameName]}...");

            // Simulate game launching
            Console.WriteLine("Loading game assets...");
            Console.WriteLine("Initializing game engine...");
            Console.WriteLine("Starting game loop...");

            // Call the actual game functions
            switch (gameName)
            {
                case "snake":
                    SnakeGame();
                    break;
                case "tetris":
                    TetrisGame();
                    break;
                case "minesweeper":
                    MinesweeperGame();
                    break;
                case "2048":
                    TwentyFortyEightGame();
                    break;
                case "pong":
                    PongGame();
                    break;
                case "pacman":
                    PacmanGame();
                    break;
                case "chess":
                    ChessGame();
                    break;
                case "sudoku":
                    SudokuGame();
                    break;
            }

            Console.WriteLine($"\nThanks for playing {games[gameName]}!");
        }

        public void Run()
        {
            Console.WriteLine("Welcome to GitHub Game Player!");
            Console.WriteLine("Integrating popular GitHub game projects for your enjoyment.");

            int choice;

            while (true)
            {
                DisplayMenu();
                if (!int.TryParse(Console.ReadLine(), out choice))
                {
                    Console.WriteLine("Invalid input. Please enter a number.");
                    continue;
                }

                if (choice == 0)
                {
                    Console.WriteLine("Thanks for playing! Goodbye!");
                    break;
                }

                var gameList = new List<string>(games.Keys);
                if (choice > 0 && choice <= gameList.Count)
                {
                    string gameKey = gameList[choice - 1];
                    PlayGame(gameKey);

                    Console.WriteLine("\nPress Enter to continue...");
                    Console.ReadLine();
                }
                else
                {
                    Console.WriteLine("Invalid choice. Please try again.");
                }
            }
        }

        // Game implementations
        private void SnakeGame()
        {
            Console.WriteLine("Snake Game starting...");
            Console.WriteLine("Use WASD keys to control the snake.");
            Console.WriteLine("Press Enter to return to main menu...");
            Console.ReadLine();
        }

        private void TetrisGame()
        {
            Console.WriteLine("Tetris Game starting...");
            Console.WriteLine("Use arrow keys to move and rotate blocks.");
            Console.WriteLine("Press Enter to return to main menu...");
            Console.ReadLine();
        }

        private void MinesweeperGame()
        {
            Console.WriteLine("Minesweeper Game starting...");
            Console.WriteLine("Use coordinates to reveal cells and mark mines.");
            Console.WriteLine("Press Enter to return to main menu...");
            Console.ReadLine();
        }

        private void TwentyFortyEightGame()
        {
            Console.WriteLine("2048 Game starting...");
            Console.WriteLine("Use arrow keys to move tiles.");
            Console.WriteLine("Press Enter to return to main menu...");
            Console.ReadLine();
        }

        private void PongGame()
        {
            Console.WriteLine("Pong Game starting...");
            Console.WriteLine("Use UP/DOWN keys to move paddle.");
            Console.WriteLine("Press Enter to return to main menu...");
            Console.ReadLine();
        }

        private void PacmanGame()
        {
            Console.WriteLine("Pacman Game starting...");
            Console.WriteLine("Use arrow keys to navigate through maze.");
            Console.WriteLine("Press Enter to return to main menu...");
            Console.ReadLine();
        }

        private void ChessGame()
        {
            Console.WriteLine("Chess Game starting...");
            Console.WriteLine("Use coordinates to move pieces.");
            Console.WriteLine("Press Enter to return to main menu...");
            Console.ReadLine();
        }

        private void SudokuGame()
        {
            Console.WriteLine("Sudoku Game starting...");
            Console.WriteLine("Use number keys to fill in the grid.");
            Console.WriteLine("Press Enter to return to main menu...");
            Console.ReadLine();
        }
    }
}