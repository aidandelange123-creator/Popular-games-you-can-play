// GitHub Game Player - Tetris Game
console.log("GitHub Game Player - Tetris Game");
console.log("Loading...");

// Create a canvas for the game
const canvas = document.createElement('canvas');
canvas.width = 300;
canvas.height = 600;
document.body.appendChild(canvas);
const ctx = canvas.getContext('2d');

// Tetris game implementation
class Tetris {
    constructor() {
        this.canvas = canvas;
        this.ctx = ctx;
        this.boardWidth = 10;
        this.boardHeight = 20;
        this.cellSize = 30;
        
        this.board = Array(this.boardHeight).fill().map(() => Array(this.boardWidth).fill(0));
        
        // Tetromino shapes
        this.shapes = {
            'I': [[[0,0], [1,0], [2,0], [3,0]], [[0,0], [0,1], [0,2], [0,3]]],
            'O': [[[0,0], [1,0], [0,1], [1,1]]],
            'T': [[[1,0], [0,1], [1,1], [2,1]], [[0,0], [0,1], [1,1], [0,2]], [[0,0], [1,0], [2,0], [1,1]], [[1,0], [0,1], [1,1], [1,2]]],
            'S': [[[1,0], [2,0], [0,1], [1,1]], [[0,0], [0,1], [1,1], [1,2]]],
            'Z': [[[0,0], [1,0], [1,1], [2,1]], [[1,0], [0,1], [1,1], [0,2]]],
            'J': [[[0,0], [0,1], [1,1], [2,1]], [[0,0], [1,0], [2,0], [0,1]], [[0,0], [1,0], [2,0], [2,1]], [[2,0], [0,1], [1,1], [2,1]]],
            'L': [[[2,0], [0,1], [1,1], [2,1]], [[0,0], [0,1], [0,2], [1,2]], [[0,0], [1,0], [2,0], [0,1]], [[0,0], [1,0], [1,1], [1,2]]]
        };
        
        // Colors for each shape
        this.colors = {
            'I': '#00FFFF', // Cyan
            'O': '#FFFF00', // Yellow
            'T': '#800080', // Purple
            'S': '#00FF00', // Green
            'Z': '#FF0000', // Red
            'J': '#0000FF', // Blue
            'L': '#FFA500'  // Orange
        };
        
        this.currentPiece = null;
        this.currentX = 0;
        this.currentY = 0;
        this.currentShape = 0;
        this.score = 0;
        this.level = 1;
        this.lines = 0;
        this.gameOver = false;
        this.dropCounter = 0;
        this.dropInterval = 1000; // ms
        this.lastTime = 0;
        
        this.spawnPiece();
        this.setupEventListeners();
    }
    
    setupEventListeners() {
        document.addEventListener('keydown', (e) => {
            if (this.gameOver) return;
            
            switch(e.key) {
                case 'ArrowLeft':
                    this.movePiece(-1, 0);
                    break;
                case 'ArrowRight':
                    this.movePiece(1, 0);
                    break;
                case 'ArrowDown':
                    this.movePiece(0, 1);
                    break;
                case 'ArrowUp':
                    this.rotatePiece();
                    break;
                case ' ':
                    this.hardDrop();
                    break;
            }
        });
    }
    
    spawnPiece() {
        const shapeTypes = Object.keys(this.shapes);
        const randShape = shapeTypes[Math.floor(Math.random() * shapeTypes.length)];
        
        this.currentPiece = randShape;
        this.currentX = Math.floor(this.boardWidth / 2) - 1;
        this.currentY = 0;
        this.currentShape = 0;
        
        // Check if game over
        if (this.checkCollision(0, 0)) {
            this.gameOver = true;
            console.log("Game Over!");
            console.log(`Final Score: ${this.score}`);
            console.log(`Lines cleared: ${this.lines}`);
            console.log(`Level reached: ${this.level}`);
        }
    }
    
    movePiece(dx, dy) {
        if (!this.gameOver) {
            if (!this.checkCollision(dx, dy)) {
                this.currentX += dx;
                this.currentY += dy;
                return true;
            } else if (dy > 0) {
                // If moving down and collision, lock the piece
                this.lockPiece();
                this.clearLines();
                this.spawnPiece();
            }
        }
        return false;
    }
    
    rotatePiece() {
        if (!this.gameOver) {
            const originalShape = this.currentShape;
            this.currentShape = (this.currentShape + 1) % this.shapes[this.currentPiece].length;
            
            if (this.checkCollision(0, 0)) {
                // If rotation causes collision, revert
                this.currentShape = originalShape;
            }
        }
    }
    
    hardDrop() {
        if (!this.gameOver) {
            while (this.movePiece(0, 1)) {
                // Keep moving down until collision
            }
        }
    }
    
    checkCollision(dx, dy) {
        const shape = this.shapes[this.currentPiece][this.currentShape];
        
        for (let i = 0; i < shape.length; i++) {
            const [x, y] = shape[i];
            const newX = this.currentX + x + dx;
            const newY = this.currentY + y + dy;
            
            if (
                newX < 0 || 
                newX >= this.boardWidth || 
                newY >= this.boardHeight ||
                (newY >= 0 && this.board[newY][newX])
            ) {
                return true;
            }
        }
        return false;
    }
    
    lockPiece() {
        const shape = this.shapes[this.currentPiece][this.currentShape];
        
        for (let i = 0; i < shape.length; i++) {
            const [x, y] = shape[i];
            const boardX = this.currentX + x;
            const boardY = this.currentY + y;
            
            if (boardY >= 0) {
                this.board[boardY][boardX] = this.currentPiece;
            }
        }
    }
    
    clearLines() {
        let linesCleared = 0;
        
        for (let y = this.boardHeight - 1; y >= 0; y--) {
            if (this.board[y].every(cell => cell !== 0)) {
                // Remove the line
                this.board.splice(y, 1);
                // Add new empty line at top
                this.board.unshift(Array(this.boardWidth).fill(0));
                linesCleared++;
                y++; // Recheck the same index since we removed a line
            }
        }
        
        if (linesCleared > 0) {
            // Update score based on lines cleared
            const points = [0, 40, 100, 300, 1200]; // Points for 0,1,2,3,4 lines
            this.score += points[linesCleared] * this.level;
            this.lines += linesCleared;
            
            // Level up every 10 lines
            this.level = Math.floor(this.lines / 10) + 1;
            
            console.log(`Cleared ${linesCleared} line(s)! Score: ${this.score}`);
            console.log(`Level: ${this.level}, Lines: ${this.lines}`);
        }
    }
    
    draw() {
        // Clear canvas
        this.ctx.fillStyle = '#000';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw board
        for (let y = 0; y < this.boardHeight; y++) {
            for (let x = 0; x < this.boardWidth; x++) {
                if (this.board[y][x]) {
                    this.ctx.fillStyle = this.colors[this.board[y][x]];
                    this.ctx.fillRect(
                        x * this.cellSize, 
                        y * this.cellSize, 
                        this.cellSize - 1, 
                        this.cellSize - 1
                    );
                }
            }
        }
        
        // Draw current piece
        if (this.currentPiece) {
            const shape = this.shapes[this.currentPiece][this.currentShape];
            this.ctx.fillStyle = this.colors[this.currentPiece];
            
            for (let i = 0; i < shape.length; i++) {
                const [x, y] = shape[i];
                const boardX = this.currentX + x;
                const boardY = this.currentY + y;
                
                if (boardY >= 0) {
                    this.ctx.fillRect(
                        boardX * this.cellSize, 
                        boardY * this.cellSize, 
                        this.cellSize - 1, 
                        this.cellSize - 1
                    );
                }
            }
        }
        
        // Draw score
        this.ctx.fillStyle = '#FFF';
        this.ctx.font = '16px Arial';
        this.ctx.fillText(`Score: ${this.score}`, 10, 20);
        this.ctx.fillText(`Level: ${this.level}`, 10, 40);
        this.ctx.fillText(`Lines: ${this.lines}`, 10, 60);
        
        if (this.gameOver) {
            this.ctx.fillStyle = 'rgba(0, 0, 0, 0.75)';
            this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
            
            this.ctx.fillStyle = '#FFF';
            this.ctx.font = '30px Arial';
            this.ctx.textAlign = 'center';
            this.ctx.fillText('GAME OVER', this.canvas.width / 2, this.canvas.height / 2);
            this.ctx.font = '16px Arial';
            this.ctx.fillText(`Final Score: ${this.score}`, this.canvas.width / 2, this.canvas.height / 2 + 40);
            this.ctx.textAlign = 'left';
        }
    }
    
    update(time = 0) {
        if (this.gameOver) return;
        
        const deltaTime = time - this.lastTime;
        this.lastTime = time;
        
        this.dropCounter += deltaTime;
        if (this.dropCounter > this.dropInterval / this.level) {
            this.movePiece(0, 1);
            this.dropCounter = 0;
        }
        
        this.draw();
        requestAnimationFrame((time) => this.update(time));
    }
    
    start() {
        console.log("Tetris game started!");
        console.log("Controls: Arrow keys to move, Up to rotate, Space to drop");
        this.update();
    }
}

// Run the game
const game = new Tetris();
game.start();