#include <iostream>
#include <vector>
#include <random>
#include <ctime>

class Minesweeper {
private:
    static const int MINE = -1;
    static const char HIDDEN = '#';
    static const char REVEALED = ' ';
    static const char FLAG = 'F';
    
    int rows, cols, numMines;
    std::vector<std::vector<int>> board;
    std::vector<std::vector<char>> display;
    bool gameOver;
    bool won;
    
public:
    Minesweeper(int r = 10, int c = 10, int m = 15) : rows(r), cols(c), numMines(m), gameOver(false), won(false) {
        board.resize(rows, std::vector<int>(cols, 0));
        display.resize(rows, std::vector<char>(cols, HIDDEN));
        
        initializeBoard();
        placeMines();
        calculateNumbers();
    }
    
    void initializeBoard() {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                board[i][j] = 0;
                display[i][j] = HIDDEN;
            }
        }
    }
    
    void placeMines() {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> rowDis(0, rows - 1);
        std::uniform_int_distribution<> colDis(0, cols - 1);
        
        int minesPlaced = 0;
        while (minesPlaced < numMines) {
            int r = rowDis(gen);
            int c = colDis(gen);
            
            if (board[r][c] != MINE) {
                board[r][c] = MINE;
                minesPlaced++;
            }
        }
    }
    
    void calculateNumbers() {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] != MINE) {
                    int count = 0;
                    
                    // Check all 8 neighbors
                    for (int di = -1; di <= 1; di++) {
                        for (int dj = -1; dj <= 1; dj++) {
                            if (di == 0 && dj == 0) continue;
                            
                            int ni = i + di;
                            int nj = j + dj;
                            
                            if (ni >= 0 && ni < rows && nj >= 0 && nj < cols) {
                                if (board[ni][nj] == MINE) {
                                    count++;
                                }
                            }
                        }
                    }
                    
                    board[i][j] = count;
                }
            }
        }
    }
    
    void displayBoard() {
        std::cout << "\n   ";
        for (int j = 0; j < cols; j++) {
            std::cout << j % 10 << " ";
        }
        std::cout << "\n";
        
        for (int i = 0; i < rows; i++) {
            std::cout << i % 10 << "  ";
            for (int j = 0; j < cols; j++) {
                std::cout << display[i][j] << " ";
            }
            std::cout << "\n";
        }
        std::cout << "\n";
    }
    
    void reveal(int r, int c) {
        if (r < 0 || r >= rows || c < 0 || c >= cols) return;
        if (display[r][c] != HIDDEN) return;
        
        display[r][c] = (board[r][c] == 0) ? REVEALED : ('0' + board[r][c]);
        
        if (board[r][c] == MINE) {
            gameOver = true;
            std::cout << "GAME OVER! You hit a mine!\n";
            return;
        }
        
        // If it's an empty cell, reveal neighbors
        if (board[r][c] == 0) {
            for (int di = -1; di <= 1; di++) {
                for (int dj = -1; dj <= 1; dj++) {
                    if (di == 0 && dj == 0) continue;
                    reveal(r + di, c + dj);
                }
            }
        }
    }
    
    void play() {
        std::cout << "GitHub Game Player - Minesweeper Game\n";
        std::cout << "Welcome to Minesweeper! Enter row and column to reveal a cell.\n";
        std::cout << "Enter -1 -1 to quit.\n";
        
        while (!gameOver && !checkWin()) {
            displayBoard();
            
            int r, c;
            std::cout << "Enter row and column (0-" << rows-1 << "): ";
            std::cin >> r >> c;
            
            if (r == -1 && c == -1) {
                std::cout << "Thanks for playing!\n";
                return;
            }
            
            if (r < 0 || r >= rows || c < 0 || c >= cols) {
                std::cout << "Invalid coordinates. Try again.\n";
                continue;
            }
            
            reveal(r, c);
        }
        
        if (checkWin()) {
            std::cout << "Congratulations! You won!\n";
            won = true;
        }
        
        // Show the full board at the end
        showFullBoard();
    }
    
    void showFullBoard() {
        std::cout << "\nFinal Board:\n";
        std::cout << "   ";
        for (int j = 0; j < cols; j++) {
            std::cout << j % 10 << " ";
        }
        std::cout << "\n";
        
        for (int i = 0; i < rows; i++) {
            std::cout << i % 10 << "  ";
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == MINE) {
                    std::cout << "*" << " ";
                } else {
                    std::cout << board[i][j] << " ";
                }
            }
            std::cout << "\n";
        }
    }
    
    bool checkWin() {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] != MINE && display[i][j] == HIDDEN) {
                    return false;
                }
            }
        }
        return true;
    }
};

int main() {
    std::cout << "GitHub Game Player - Minesweeper Game\n";
    std::cout << "Loading...\n";
    std::cout << "Starting game...\n";
    
    Minesweeper game(10, 10, 15); // 10x10 grid with 15 mines
    game.play();
    
    return 0;
}