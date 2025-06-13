# A Billion Stars Falling From the Sky

### Video Demo: https://youtu.be/Q5DZOs_EexY?si=0zLqP3Suvm-nBZ4h
### Description:
**A Billion Stars Falling From the Sky** is a simple but engaging survival game developed using Python and the `pygame` library. In this game, the player controls a character that must dodge stars falling randomly from all directions. The gameplay is time-based, and the objective is to survive as long as possible while avoiding collisions with stars.
The game begins when the player presses the **'S' key**, and stars begin to fall immediately. The player can control the character using the **arrow keys (← ↑ → ↓)**. When a star collides with the player, it disappears, a sound effect is played, and one life is lost. The number of remaining lives is displayed on the screen, along with the player's current survival time.
As the game progresses, the number and speed of falling stars increase, creating a more intense and challenging environment. When the player's lives reach zero, the game ends and a result screen is displayed. The player can press the **'R' key** to restart the game and try again.

### Package Structure and Functionality:
- `project.py`: This is the main file where the game is implemented. It contains all the logic for initializing the game window, rendering objects (player, stars), handling keyboard input, collision detection, score/life tracking, and restarting the game.
- `test_project.py`: A Pytest-based test file to validate basic functionalities such as player movement limits, star generation boundaries, and object initialization.
- `config.py`: Stores game-wide configs such as screen size, color values, font sizes, and movement speed settings to keep the code modular and easier to maintain.
- `player.py`: Defines the `Player` class. The player’s position is updated based on arrow key input, and it handles collision checks with stars.
- `sound.py`: Manages all sound effects in the game, including collision sounds and optional background music.
- `star.py`: Contains the `Star` class, which defines how each star behaves, how it moves, and how it is rendered. Stars are spawned at random positions and fall downward with increasing speed as time goes on
