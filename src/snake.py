import consts
from game_manager import GameManager


class Snake:
    """
    Represents a snake in the game.

    Attributes:
    - keys (dict): A list of keys used to control the snake.
    - cells (list): A list of positions occupied by the snake.
    - game (GameManager): The GameManager object the snake belongs to.
    - color (tuple): The color of the snake.
    - direction (str): The current direction of the snake.

    Methods:
    - __init__(keys, game, pos, color, direction): Initializes a Snake object.
    - get_head(): Returns the head cell of the snake.
    - val(x): Adjusts the value of x to fit within the game size.
    - next_move(): Moves the snake to the next cell based on its current direction.
    - handle(keys): Handles the input keys to change the direction of the snake.
    """

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys: dict, game: 'GameManager', pos: tuple, color: tuple, direction: str):
        """
        Initializes a Snake object.

        Parameters:
        - keys (dict): A list of keys used to control the snake.
        - game (GameManager): The GameManager object the snake belongs to.
        - pos (tuple): The initial position of the snake.
        - color (tuple): The color of the snake.
        - direction (str): The initial direction of the snake.

        """
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def _get_head(self) -> tuple:
        """
        Returns the head cell of the snake.
        """
        return self.cells[-1]

    def _val(self, x: int) -> int:
        """
        Adjusts the value of x to fit within the game size.

        Args:
            x (int): The value to be adjusted.

        Returns:
            int: The adjusted value of x.
        """
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self) -> None:
        """
        Moves the snake to the next cell based on its current direction.
        If the next cell is a block or another snake, the snake is killed.
        Otherwise, the snake moves to the next cell and updates its position.
        If the next cell is the background color, the snake's tail is removed.
        """
        x, y = self._get_head()
        next_cell_pos = (self._val(x + self.dx[self.direction]), self._val(y + self.dy[self.direction]))
        next_cell = self.game.get_cell(next_cell_pos)

        if next_cell.color in [consts.block_color] + [s["color"] for s in consts.snakes]:
            self.game.kill(self)
        else:
            self.cells.append(next_cell_pos)
            if next_cell.color == consts.back_color:
                self.game.get_cell(self.cells.pop(0)).set_color(consts.back_color)
            next_cell.set_color(self.color)

    def handle(self, intput_keys: list) -> None:
        """
        Handles the input keys to change the direction of the snake.

        Parameters:
        input_keys (list): A list of keys pressed by the player.

        Returns:
        None
        """
        for k in intput_keys:
            if k in self.keys and self.keys[k] != self.direction:
                self.direction = self.keys[k]
                break
