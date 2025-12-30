#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstdlib>
#include <ctime>

#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif

class GamePlayer {
private:
    std::map<std::string, std::string> games;
    
public:
    GamePlayer() {
        // Initialize popular games from GitHub
        games["snake"] = "Python Snake Game";
        games["tetris"] = "JavaScript Tetris";
        games["minesweeper"] = "C++ Minesweeper";
        games["2048"] = "HTML/JS 2048";
        games["pong"] = "Python Pong";
        games["pacman"] = "JavaScript Pacman";
        games["chess"] = "Python Chess";
        games["sudoku"] = "JavaScript Sudoku";
    }
    
    void displayMenu() {
        std::cout << "\n========================================\n";
        std::cout << "    GITHUB GAME PLAYER - MAIN MENU\n";
        std::cout << "========================================\n";
        std::cout << "Available Games:\n\n";
        
        int index = 1;
        for (const auto& game : games) {
            std::cout << index << ". " << game.second << " (" << game.first << ")\n";
            index++;
        }
        
        std::cout << "\n0. Exit\n";
        std::cout << "========================================\n";
        std::cout << "Enter your choice: ";
    }
    
    void playGame(const std::string& gameName) {
        std::cout << "\nLaunching " << games[gameName] << "...\n";
        
        // Simulate game launching
        std::cout << "Loading game assets...\n";
        std::cout << "Initializing game engine...\n";
        std::cout << "Starting game loop...\n";
        
        // In a real implementation, this would launch the actual game
        // For now, we'll simulate by calling appropriate executables
        if (gameName == "snake") {
            std::cout << "Playing Snake game...\n";
            // system("python games/snake/snake.py");
        } else if (gameName == "tetris") {
            std::cout << "Playing Tetris game...\n";
            // system("node games/tetris/tetris.js");
        } else if (gameName == "minesweeper") {
            std::cout << "Playing Minesweeper game...\n";
            // system("./games/minesweeper/minesweeper");
        } else if (gameName == "2048") {
            std::cout << "Playing 2048 game...\n";
            // system("start games/2048/index.html");
        } else if (gameName == "pong") {
            std::cout << "Playing Pong game...\n";
            // system("python games/pong/pong.py");
        } else if (gameName == "pacman") {
            std::cout << "Playing Pacman game...\n";
            // system("node games/pacman/pacman.js");
        } else if (gameName == "chess") {
            std::cout << "Playing Chess game...\n";
            // system("python games/chess/chess.py");
        } else if (gameName == "sudoku") {
            std::cout << "Playing Sudoku game...\n";
            // system("node games/sudoku/sudoku.js");
        }
        
        std::cout << "Game launched successfully! Enjoy playing " << games[gameName] << "\n";
    }
    
    void run() {
        srand(time(0));
        int choice;
        
        std::cout << "Welcome to GitHub Game Player!\n";
        std::cout << "Integrating popular GitHub game projects for your enjoyment.\n";
        
        while (true) {
            displayMenu();
            std::cin >> choice;
            
            if (choice == 0) {
                std::cout << "Thanks for playing! Goodbye!\n";
                break;
            }
            
            auto it = games.begin();
            std::advance(it, choice - 1);
            
            if (choice > 0 && choice <= games.size()) {
                std::string gameKey = it->first;
                playGame(gameKey);
                
                std::cout << "\nPress Enter to continue...";
                std::cin.ignore();
                std::cin.get();
            } else {
                std::cout << "Invalid choice. Please try again.\n";
            }
        }
    }
};

int main() {
    GamePlayer player;
    player.run();
    return 0;
}