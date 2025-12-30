// GitHub Game Player - Pacman Game Simulation
console.log("GitHub Game Player - Pacman Game");
console.log("Loading...");

// Simple Pacman game simulation
function simulatePacman() {
    console.log("Pacman game started!");
    console.log("Navigate Pacman through the maze to eat all dots while avoiding ghosts!");
    console.log("Controls: Arrow keys to move");
    
    // Game elements
    const maze = [
        "############",
        "#........#.#",
        "#.##.#.#.#.#",
        "#.#..#.#.#.#",
        "#.#.##.#.#.#",
        "#........#.#",
        "#.####.###.#",
        "#....#.....#",
        "####.#.#####",
        "#...........",
        "############"
    ];
    
    let score = 0;
    let lives = 3;
    let dotsRemaining = 50; // Estimated number of dots in the maze
    
    console.log("\nMaze layout:");
    maze.forEach((row, index) => {
        console.log(row);
    });
    
    console.log("\nGame in progress...");
    console.log("Use arrow keys to navigate Pacman through the maze");
    
    // Simulate game rounds
    for (let round = 0; round < 15; round++) {
        if (lives <= 0) {
            console.log("Game Over! All lives lost.");
            break;
        }
        
        if (dotsRemaining <= 0) {
            console.log("Level Complete! All dots collected!");
            break;
        }
        
        console.log(`\nRound ${round + 1}:`);
        
        // Simulate Pacman movement and dot collection
        const dotsCollected = Math.min(Math.floor(Math.random() * 5) + 1, dotsRemaining);
        dotsRemaining -= dotsCollected;
        score += dotsCollected * 10;
        
        console.log(`Pacman collected ${dotsCollected} dots!`);
        console.log(`Dots remaining: ${dotsRemaining}`);
        console.log(`Score: ${score}`);
        
        // Simulate ghost encounter
        if (Math.random() > 0.7) {
            console.log("Ghost encountered!");
            if (Math.random() > 0.5) {
                console.log("Pacman lost a life!");
                lives--;
                console.log(`Lives remaining: ${lives}`);
            } else {
                console.log("Pacman ate the ghost! Bonus points!");
                score += 200;
                console.log(`Score: ${score}`);
            }
        }
        
        // Small delay to simulate gameplay
        // In a real game, we'd have proper timing
    }
    
    if (lives > 0 && dotsRemaining <= 0) {
        console.log("\nCongratulations! You won the game!");
    } else if (lives > 0) {
        console.log("\nGame ended early.");
    }
    
    console.log(`Final Score: ${score}`);
    console.log(`Lives remaining: ${lives}`);
    console.log(`Dots remaining: ${dotsRemaining}`);
}

// Run the game
simulatePacman();