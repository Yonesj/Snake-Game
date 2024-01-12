import pygame
import consts
from cell import Cell


class GameManager:
    """
    The GameManager class manages the game state and logic.

    Attributes:
        screen (pygame.Surface): The pygame screen object.
        size (int): The size of the game board.
        cells (list): A 2D list representing the cells on the game board.
        sx (int): The starting x-coordinate of the game board.
        sy (int): The starting y-coordinate of the game board.
        snakes (list): A list of Snake objects in the game.
        turn (int): The current turn number.

    Methods:
        __init__(self, size, screen, sx, sy, block_cells): Initializes the GameManager object.
        get_cell(self, pos): Retrieves the cell at the specified position.
        get_next_fruit_pos(self): Returns the position of the next fruit based on the current game state.
    """

    def __init__(self, size, screen, sx, sy, block_cells):
        """
        Initialize the GameManager object.

        Args:
            size (int): The size of the game board.
            screen (pygame.Surface): The pygame screen object.
            sx (int): The starting x-coordinate of the game board.
            sy (int): The starting y-coordinate of the game board.
            block_cells (list): A list of cells to be blocked.

        Returns:
            None
        """
        self.screen = screen
        self.size = size
        self.cells = []
        self.sx = sx
        self.sy = sy
        self.snakes = list()
        self.turn = 0
        for i in range(self.size):
            tmp = []
            for j in range(self.size):
                tmp.append(Cell(screen, sx + i * consts.cell_size, sy + j * consts.cell_size))
            self.cells.append(tmp)
        for cell in block_cells:
            self.get_cell(cell).set_color(consts.block_color)

    def get_cell(self, pos):
        """
        Retrieves the cell at the specified position.

        Args:
            pos (tuple): The position of the cell in the grid.

        Returns:
            object: The cell at the specified position, or None if the position is out of bounds.
        """
        try:
            return self.cells[pos[0]][pos[1]]
        except:
            return None

    def get_next_fruit_pos(self):
        """
        Returns the position of the next fruit based on the current game state.

        Returns:
            tuple: The position of the next fruit as a tuple (x, y).
        """
        ret = -1, -1
        mx = -100

        for i in range(0, self.size):
            for j in range(0, self.size):

                mn = 100000000

                for x in range(0, self.size):
                    for y in range(0, self.size):
                        if self.get_cell((x, y)).color != consts.back_color:
                            mn = min(mn, int(abs(x - i) + abs(y - j)))

                if mn > mx:
                    mx = mn
                    ret = i, j

        return ret
