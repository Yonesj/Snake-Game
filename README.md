# Snake Game - Multiplayer Version

Welcome to the Multiplayer Snake Game! This project is an adaptation of the classic Snake game where players control a snake to eat food and grow longer while avoiding collisions with walls and other snakes. This version adds a multiplayer feature, allowing multiple players to compete against each other in real-time.

## Table of Contents
1. [Demo](#demo)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [How to Play](#how-to-play)
6. [License](#license)

</br>

## Demo
![](assets/gameplay.gif)


## Features
- Multiplayer support: Players can connect to a server and play together in real-time.
- Flexible server setup: Players can choose the number of players (single-player or multiplayer mode).
- Classic gameplay: Use the W, A, S, D keys to control the movement of your snake.
- Wrapping around edges: Snakes wrap around the edges of the game board instead of dying upon collision.

</br>

## Technologies Used
- Python
- Pygame
- Socket programming
- Data serialization (JSON)

</br>

## Installation
To install the game, follow these steps:
1. **Clone the repository to your local machine:**
   ```bash
   git clone https://github.com/Yonesj/Snake-Game.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Snake-Game
   ```
3. **Install the required dependencies:**
   ```bash
    pip install -r requirements.txt
    ```

</br>

## How to Play
To play the game, follow these steps:
1. **Start the server:**  Run the 'server.py' with the desired number of players (1 for single-player mode, more for multiplayer mode).
   ```bash
   python server.py [number_of_players]
   ```
2. **Join the game:** Run 'client.py' and provide the server's IP address as an argument. If the server is running on the same machine, use 'localhost' as the IP address.
   ```bash
   python client.py [server_ip]
   ```
   Otherwise, you can find the server's IP address by running the following command in the terminal:
   ```bash
    ipconfig
    ```

3. **Play the game:**
   - Use the WASD keys to control the movement of your snake.
      - W: Move up
      - A: Move left
      - S: Move down
      - D: Move right
   - Eat food to grow longer.
   - Avoid collisions with walls and other snakes (including your own).
   - Enjoy the game!

</br>

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

</br>

Enjoy the game! 🐍🎮
