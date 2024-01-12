import consts


class Snake:
    """
    Represents a snake in the game.

    Attributes:
    - keys (list): A list of keys used to control the snake.
    - cells (list): A list of positions occupied by the snake.
    - game (GameManager): The GameManager object the snake belongs to.
    - color (str): The color of the snake.
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

    def __init__(self, keys, game, pos, color, direction):
        """
        Initializes a Snake object.

        Parameters:
        - keys (list): A list of keys used to control the snake.
        - game (GameManager): The GameManager object the snake belongs to.
        - pos (tuple): The initial position of the snake.
        - color (str): The color of the snake.
        - direction (str): The initial direction of the snake.

        """
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        """
        Returns the head cell of the snake.
        """
        return self.cells[-1]

    def val(self, x):
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

    def next_move(self):
        """
        Moves the snake to the next cell based on its current direction.
        If the next cell is a block or another snake, the snake is killed.
        Otherwise, the snake moves to the next cell and updates its position.
        If the next cell is the background color, the snake's tail is removed.
        """
        x, y = self.get_head()
        print(x, y)
        next_cell = self.game.get_cell((self.val(x + self.dx[self.direction]), self.val(y + self.dy[self.direction])))

        if next_cell.color in [consts.block_cells] + [s["color"] for s in consts.snakes]:
            self.game.kill(self)
        else:
            next_cell.set_color(self.color)
            self.cells.append((x + self.dx[self.direction], y + self.dy[self.direction]))
            if next_cell.color == consts.back_color:
                self.game.get_cell(self.cells.pop(0)).set_color(consts.back_color)

    def handle(self, keys):
        """
        Handles the input keys to change the direction of the snake.

        Parameters:
        keys (list): A list of keys pressed by the player.

        Returns:
        None
        """
        for k in keys:
            if k in self.keys and self.keys[k] != self.direction:
                self.direction = self.keys[k]
                break