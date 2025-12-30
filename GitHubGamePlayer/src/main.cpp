#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstdlib>
#include <ctime>

#ifdef _WIN32
#include <windows.h>
#include <conio.h>
#else
#include <unistd.h>
#endif

// Function declarations for games
void snake_game();
void tetris_game();
void minesweeper_game();
void twenty_forty_eight_game();
void pong_game();
void pacman_game();
void chess_game();
void sudoku_game();

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
        
        // Call the actual game functions
        if (gameName == "snake") {
            snake_game();
        } else if (gameName == "tetris") {
            tetris_game();
        } else if (gameName == "minesweeper") {
            minesweeper_game();
        } else if (gameName == "2048") {
            twenty_forty_eight_game();
        } else if (gameName == "pong") {
            pong_game();
        } else if (gameName == "pacman") {
            pacman_game();
        } else if (gameName == "chess") {
            chess_game();
        } else if (gameName == "sudoku") {
            sudoku_game();
        }
        
        std::cout << "\nThanks for playing " << games[gameName] << "!\n";
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