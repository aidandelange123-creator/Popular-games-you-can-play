// GitHub Game Player - Pacman Game
console.log("GitHub Game Player - Pacman Game");
console.log("Loading...");

// Create a canvas for the game
const canvas = document.createElement('canvas');
canvas.width = 600;
canvas.height = 400;
document.body.appendChild(canvas);
const ctx = canvas.getContext('2d');

// Pacman game implementation
class PacmanGame {
    constructor() {
        this.canvas = canvas;
        this.ctx = ctx;
        this.cellSize = 20;
        this.mazeWidth = 30;
        this.mazeHeight = 20;
        
        // Define the maze layout (1 = wall, 0 = dot, 2 = empty, 3 = power pellet)
        this.maze = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
            [1,3,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,3,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1],
            [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,0,1,1,1,1,1,2,1,1,2,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
            [2,2,2,2,2,1,0,1,1,2,2,2,2,2,2,2,2,2,2,1,1,0,1,2,2,2,2,2,2,2],
            [1,1,1,1,1,1,0,1,1,2,1,1,2,2,2,2,1,1,2,1,1,0,1,1,1,1,1,1,1,1],
            [2,2,2,2,2,2,0,2,2,2,1,2,2,2,2,2,2,1,2,2,2,0,2,2,2,2,2,2,2,2],
            [1,1,1,1,1,1,0,1,1,2,1,2,2,2,2,2,2,1,2,1,1,0,1,1,1,1,1,1,1,1],
            [2,2,2,2,2,1,0,1,1,2,1,1,1,1,1,1,1,1,2,1,1,0,1,2,2,2,2,2,2,2],
            [1,1,1,1,1,1,0,1,1,2,2,2,2,2,2,2,2,2,2,1,1,0,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
            [1,3,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,3,1],
            [1,1,0,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ];
        
        this.pacman = {
            x: 14,
            y: 15,
            direction: {x: 0, y: 0}, // Current direction
            nextDirection: {x: 0, y: 0}, // Desired next direction
            mouthOpen: 0,
            mouthChange: 0.1
        };
        
        this.ghosts = [
            {x: 14, y: 9, color: '#FF0000', direction: {x: 1, y: 0}}, // Red
            {x: 13, y: 9, color: '#FFB8FF', direction: {x: -1, y: 0}}, // Pink
            {x: 15, y: 9, color: '#00FFFF', direction: {x: 0, y: 1}}, // Cyan
            {x: 14, y: 10, color: '#FFB852', direction: {x: 0, -1}} // Orange
        ];
        
        this.score = 0;
        this.lives = 3;
        this.dots = this.countDots();
        this.powerMode = false;
        this.powerModeTimer = 0;
        this.gameOver = false;
        this.won = false;
        
        this.setupEventListeners();
    }
    
    setupEventListeners() {
        document.addEventListener('keydown', (e) => {
            if (this.gameOver) return;
            
            switch(e.key) {
                case 'ArrowUp':
                    this.pacman.nextDirection = {x: 0, y: -1};
                    break;
                case 'ArrowDown':
                    this.pacman.nextDirection = {x: 0, y: 1};
                    break;
                case 'ArrowLeft':
                    this.pacman.nextDirection = {x: -1, y: 0};
                    break;
                case 'ArrowRight':
                    this.pacman.nextDirection = {x: 1, y: 0};
                    break;
            }
        });
    }
    
    countDots() {
        let count = 0;
        for (let y = 0; y < this.mazeHeight; y++) {
            for (let x = 0; x < this.mazeWidth; x++) {
                if (this.maze[y][x] === 0 || this.maze[y][x] === 3) {
                    count++;
                }
            }
        }
        return count;
    }
    
    canMove(x, y) {
        if (x < 0 || x >= this.mazeWidth || y < 0 || y >= this.mazeHeight) {
            return false;
        }
        return this.maze[y][x] !== 1;
    }
    
    update() {
        if (this.gameOver) return;
        
        // Move Pacman
        if (this.canMove(this.pacman.x + this.pacman.nextDirection.x, this.pacman.y + this.pacman.nextDirection.y)) {
            this.pacman.direction = {...this.pacman.nextDirection};
        }
        
        if (this.canMove(this.pacman.x + this.pacman.direction.x, this.pacman.y + this.pacman.direction.y)) {
            this.pacman.x += this.pacman.direction.x;
            this.pacman.y += this.pacman.direction.y;
            
            // Handle wrapping around the screen
            if (this.pacman.x < 0) this.pacman.x = this.mazeWidth - 1;
            if (this.pacman.x >= this.mazeWidth) this.pacman.x = 0;
        }
        
        // Animate mouth
        this.pacman.mouthOpen += this.pacman.mouthChange;
        if (this.pacman.mouthOpen > 0.5 || this.pacman.mouthOpen < 0) {
            this.pacman.mouthChange *= -1;
        }
        
        // Check for dot collection
        const cell = this.maze[this.pacman.y][this.pacman.x];
        if (cell === 0) { // Regular dot
            this.maze[this.pacman.y][this.pacman.x] = 2; // Empty space
            this.score += 10;
            this.dots--;
        } else if (cell === 3) { // Power pellet
            this.maze[this.pacman.y][this.pacman.x] = 2; // Empty space
            this.score += 50;
            this.dots--;
            this.powerMode = true;
            this.powerModeTimer = 300; // 5 seconds at 60fps
        }
        
        // Update power mode
        if (this.powerMode) {
            this.powerModeTimer--;
            if (this.powerModeTimer <= 0) {
                this.powerMode = false;
            }
        }
        
        // Move ghosts
        for (let ghost of this.ghosts) {
            // Simple AI: try to move towards Pacman, with some randomness
            const directions = [
                {x: 0, y: -1}, {x: 0, y: 1}, {x: -1, y: 0}, {x: 1, y: 0}
            ];
            
            // Shuffle directions
            for (let i = directions.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [directions[i], directions[j]] = [directions[j], directions[i]];
            }
            
            let moved = false;
            for (let dir of directions) {
                if (this.canMove(ghost.x + dir.x, ghost.y + dir.y) &&
                    !(ghost.x + dir.x === ghost.x && ghost.y + dir.y === ghost.y)) { // Don't go back
                    ghost.direction = dir;
                    ghost.x += ghost.direction.x;
                    ghost.y += ghost.direction.y;
                    moved = true;
                    
                    // Handle wrapping around the screen
                    if (ghost.x < 0) ghost.x = this.mazeWidth - 1;
                    if (ghost.x >= this.mazeWidth) ghost.x = 0;
                    
                    break;
                }
            }
            
            // If couldn't move, stay in place
            if (!moved) {
                // Try again next frame
            }
        }
        
        // Check for collisions with ghosts
        for (let ghost of this.ghosts) {
            if (Math.abs(ghost.x - this.pacman.x) < 0.5 && Math.abs(ghost.y - this.pacman.y) < 0.5) {
                if (this.powerMode) {
                    // Eat the ghost
                    ghost.x = 14;
                    ghost.y = 9;
                    this.score += 200;
                } else {
                    // Lose a life
                    this.lives--;
                    if (this.lives <= 0) {
                        this.gameOver = true;
                    } else {
                        // Reset positions
                        this.pacman.x = 14;
                        this.pacman.y = 15;
                        for (let g of this.ghosts) {
                            g.x = 14;
                            g.y = 9;
                        }
                    }
                }
            }
        }
        
        // Check win condition
        if (this.dots <= 0) {
            this.won = true;
            this.gameOver = true;
        }
    }
    
    draw() {
        // Clear canvas
        this.ctx.fillStyle = '#000';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Calculate offset to center the maze
        const offsetX = (this.canvas.width - this.mazeWidth * this.cellSize) / 2;
        const offsetY = (this.canvas.height - this.mazeHeight * this.cellSize) / 2;
        
        // Draw maze
        for (let y = 0; y < this.mazeHeight; y++) {
            for (let x = 0; x < this.mazeWidth; x++) {
                const cell = this.maze[y][x];
                
                // Draw walls
                if (cell === 1) {
                    this.ctx.fillStyle = '#0000FF';
                    this.ctx.fillRect(
                        offsetX + x * this.cellSize, 
                        offsetY + y * this.cellSize, 
                        this.cellSize, 
                        this.cellSize
                    );
                } 
                // Draw dots
                else if (cell === 0) {
                    this.ctx.fillStyle = '#FFFF00';
                    this.ctx.beginPath();
                    this.ctx.arc(
                        offsetX + x * this.cellSize + this.cellSize/2,
                        offsetY + y * this.cellSize + this.cellSize/2,
                        this.cellSize/6,
                        0,
                        Math.PI * 2
                    );
                    this.ctx.fill();
                }
                // Draw power pellets
                else if (cell === 3) {
                    this.ctx.fillStyle = '#FFFF00';
                    this.ctx.beginPath();
                    this.ctx.arc(
                        offsetX + x * this.cellSize + this.cellSize/2,
                        offsetY + y * this.cellSize + this.cellSize/2,
                        this.cellSize/3,
                        0,
                        Math.PI * 2
                    );
                    this.ctx.fill();
                }
            }
        }
        
        // Draw Pacman
        this.ctx.fillStyle = '#FFFF00';
        this.ctx.save();
        this.ctx.translate(
            offsetX + this.pacman.x * this.cellSize + this.cellSize/2,
            offsetY + this.pacman.y * this.cellSize + this.cellSize/2
        );
        
        // Rotate based on direction
        let rotation = 0;
        if (this.pacman.direction.x === 1) rotation = 0;
        else if (this.pacman.direction.x === -1) rotation = Math.PI;
        else if (this.pacman.direction.y === -1) rotation = Math.PI * 1.5;
        else if (this.pacman.direction.y === 1) rotation = Math.PI * 0.5;
        
        this.ctx.rotate(rotation);
        
        // Draw Pacman with mouth animation
        this.ctx.beginPath();
        this.ctx.moveTo(0, 0);
        this.ctx.arc(0, 0, this.cellSize/2, 
                     this.pacman.mouthOpen * Math.PI, 
                     (1 - this.pacman.mouthOpen) * Math.PI);
        this.ctx.lineTo(0, 0);
        this.ctx.fill();
        this.ctx.restore();
        
        // Draw ghosts
        for (let ghost of this.ghosts) {
            const ghostColor = this.powerMode ? '#0000FF' : ghost.color;
            this.ctx.fillStyle = ghostColor;
            
            // Draw ghost body
            this.ctx.beginPath();
            this.ctx.arc(
                offsetX + ghost.x * this.cellSize + this.cellSize/2,
                offsetY + ghost.y * this.cellSize + this.cellSize/3,
                this.cellSize/2.5,
                Math.PI,
                0,
                false
            );
            
            // Draw wavy bottom
            const waveHeight = this.cellSize/8;
            this.ctx.lineTo(
                offsetX + ghost.x * this.cellSize + this.cellSize,
                offsetY + ghost.y * this.cellSize + this.cellSize/2
            );
            
            for (let i = 0; i < 3; i++) {
                this.ctx.lineTo(
                    offsetX + ghost.x * this.cellSize + this.cellSize - (i + 1) * (this.cellSize/3),
                    offsetY + ghost.y * this.cellSize + this.cellSize/2 + (i % 2 === 0 ? waveHeight : 0)
                );
            }
            
            this.ctx.lineTo(
                offsetX + ghost.x * this.cellSize,
                offsetY + ghost.y * this.cellSize + this.cellSize/2
            );
            
            this.ctx.fill();
            
            // Draw eyes
            this.ctx.fillStyle = '#FFF';
            this.ctx.beginPath();
            this.ctx.arc(
                offsetX + ghost.x * this.cellSize + this.cellSize/3,
                offsetY + ghost.y * this.cellSize + this.cellSize/3,
                this.cellSize/8,
                0,
                Math.PI * 2
            );
            this.ctx.arc(
                offsetX + ghost.x * this.cellSize + 2*this.cellSize/3,
                offsetY + ghost.y * this.cellSize + this.cellSize/3,
                this.cellSize/8,
                0,
                Math.PI * 2
            );
            this.ctx.fill();
            
            // Draw pupils
            this.ctx.fillStyle = '#000';
            this.ctx.beginPath();
            this.ctx.arc(
                offsetX + ghost.x * this.cellSize + this.cellSize/3,
                offsetY + ghost.y * this.cellSize + this.cellSize/3,
                this.cellSize/16,
                0,
                Math.PI * 2
            );
            this.ctx.arc(
                offsetX + ghost.x * this.cellSize + 2*this.cellSize/3,
                offsetY + ghost.y * this.cellSize + this.cellSize/3,
                this.cellSize/16,
                0,
                Math.PI * 2
            );
            this.ctx.fill();
        }
        
        // Draw score and lives
        this.ctx.fillStyle = '#FFF';
        this.ctx.font = '16px Arial';
        this.ctx.fillText(`Score: ${this.score}`, 10, 20);
        this.ctx.fillText(`Lives: ${this.lives}`, 10, 40);
        
        // Draw game over or win message
        if (this.gameOver) {
            this.ctx.fillStyle = 'rgba(0, 0, 0, 0.75)';
            this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
            
            this.ctx.fillStyle = '#FFF';
            this.ctx.font = '30px Arial';
            this.ctx.textAlign = 'center';
            
            if (this.won) {
                this.ctx.fillText('YOU WIN!', this.canvas.width / 2, this.canvas.height / 2);
            } else {
                this.ctx.fillText('GAME OVER', this.canvas.width / 2, this.canvas.height / 2);
            }
            
            this.ctx.font = '16px Arial';
            this.ctx.fillText(`Final Score: ${this.score}`, this.canvas.width / 2, this.canvas.height / 2 + 40);
            this.ctx.textAlign = 'left';
        }
    }
    
    run() {
        console.log("Pacman game started!");
        console.log("Navigate Pacman through the maze to eat all dots while avoiding ghosts!");
        console.log("Controls: Arrow keys to move");
        
        const gameLoop = () => {
            if (!this.gameOver) {
                this.update();
            }
            this.draw();
            requestAnimationFrame(gameLoop);
        };
        
        gameLoop();
    }
}

// Run the game
const game = new PacmanGame();
game.run();