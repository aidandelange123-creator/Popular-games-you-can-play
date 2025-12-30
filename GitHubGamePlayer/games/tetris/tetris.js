// GitHub Game Player - Tetris Game
console.log("GitHub Game Player - Tetris Game");
console.log("Loading...");

// Simple Tetris game simulation
function simulateTetris() {
    console.log("Tetris game started!");
    console.log("Game grid: 10x20");
    console.log("Controls: A/D to move, W to rotate, S to drop");
    
    // Game pieces
    const pieces = [
        { shape: 'I', color: 'cyan', positions: [[0,0], [1,0], [2,0], [3,0]] },
        { shape: 'O', color: 'yellow', positions: [[0,0], [1,0], [0,1], [1,1]] },
        { shape: 'T', color: 'purple', positions: [[0,0], [1,0], [2,0], [1,1]] },
        { shape: 'S', color: 'green', positions: [[0,0], [1,0], [1,1], [2,1]] },
        { shape: 'Z', color: 'red', positions: [[0,1], [1,1], [1,0], [2,0]] },
        { shape: 'J', color: 'blue', positions: [[0,0], [0,1], [1,1], [2,1]] },
        { shape: 'L', color: 'orange', positions: [[2,0], [0,1], [1,1], [2,1]] }
    ];
    
    let score = 0;
    let level = 1;
    let lines = 0;
    
    console.log("Game running...");
    console.log("Use A/D to move pieces, W to rotate, S to drop");
    
    // Simulate game loop
    for (let i = 0; i < 10; i++) {
        const piece = pieces[Math.floor(Math.random() * pieces.length)];
        console.log(`New piece: ${piece.shape} - ${piece.color}`);
        
        // Simulate some gameplay
        const moves = ['left', 'right', 'rotate', 'down', 'down'];
        moves.forEach(move => {
            console.log(`Moving: ${move}`);
        });
        
        // Simulate line clearing
        if (Math.random() > 0.7) {
            const clearedLines = Math.floor(Math.random() * 4) + 1;
            lines += clearedLines;
            score += clearedLines * 100 * level;
            console.log(`Cleared ${clearedLines} line(s)! Score: ${score}`);
            
            // Level up every 10 lines
            if (lines >= level * 10) {
                level++;
                console.log(`Level up! Now at level ${level}`);
            }
        }
        
        console.log("---");
        // Small delay to simulate gameplay
        // In a real game, we'd have proper timing
    }
    
    console.log("Game over!");
    console.log(`Final Score: ${score}`);
    console.log(`Lines cleared: ${lines}`);
    console.log(`Level reached: ${level}`);
}

// Run the game
simulateTetris();