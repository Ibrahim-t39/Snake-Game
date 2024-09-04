# Snake Game

## Short Description

A classic Snake game built using Python's Turtle module. Control the snake to eat food, grow longer, and avoid collisions with the walls or its own body. The game features a scoreboard that tracks and resets the score when the game ends. Inspired by Angela Yu's Udemy course.

## Full Description

This project is a classic implementation of the Snake game using Python's Turtle graphics module. The game is simple yet addictive, challenging players to control a snake that grows longer each time it eats food. The objective is to grow the snake as long as possible without hitting the walls or colliding with itself.

**Features:**
- **Snake Movement:** The snake is controlled using the arrow keys, with smooth and responsive movement.
- **Food Generation:** Randomly placed food appears on the screen for the snake to eat, which causes the snake to grow.
- **Scoreboard:** A dynamic scoreboard tracks the player's score, increasing with each piece of food consumed. The score resets when the game is over.
- **Collision Detection:** The game ends if the snake hits the walls or collides with its own body, prompting a reset of the game.

**Note**: This project was inspired by Angela Yu's course on Udemy.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- The Turtle graphics module (usually included with Python installations).

### How to Play

1. Clone or download the repository to your local machine.
2. Run the script using Python:

   ```bash
   python snake_game.py
   ```

3. Use the arrow keys to control the snake:
   - Up: Move up
   - Down: Move down
   - Left: Move left
   - Right: Move right

4. Try to eat the food to grow the snake longer and increase your score.
5. Avoid colliding with the walls or the snake's own body. If you do, the game will reset.

### Customization

You can customize the game by:
- **Changing Colors:** Modify the snake, food, or background colors in the code.
- **Adjusting Speed:** Change the `time.sleep(0.1)` value to make the game faster or slower.
- **Adding Features:** Enhance the game by adding obstacles, levels, or special effects.
