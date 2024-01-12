import pygame
import consts


class Cell:
    """
    A class used to represent a cell in the game.

    Attributes:
        sx (int): The x-coordinate of the top-left corner of the cell.
        sy (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        surface (pygame.Surface): The surface on which the cell will be drawn.
        color (tuple): The RGB color value of the cell.

    Methods:
        set_color(color): Sets the color of the cell and updates the display.
        is_empty(): Check if the cell is empty.
        is_fruit(): Check if the cell is a fruit.
    """

    def __init__(self, surface, sx, sy, color=consts.back_color):
        """
        Initializes a Cell object.

        Args:
            surface (pygame.Surface): The surface on which the cell will be drawn.
            sx (int): The x-coordinate of the top-left corner of the cell.
            sy (int): The y-coordinate of the top-left corner of the cell.
            color (tuple, optional): The color of the cell. Defaults to consts.back_color.
        """
        self.sx = sx
        self.sy = sy
        self.size = consts.cell_size
        self.surface = surface
        self.color = color
        pygame.draw.rect(surface, (0, 0, 0), (sx, sy, consts.cell_size, consts.cell_size), 1)
        self.set_color(color)

    def set_color(self, color):
        """
        Sets the color of the cell and updates the display.

        Parameters:
            color (tuple): The RGB color value to set.

        Returns:
            None
        """
        self.color = color
        pygame.draw.rect(self.surface, color, (self.sx + 1, self.sy + 1, self.size - 2, self.size - 2))
        pygame.display.update()

    def is_empty(self):
        """
        Check if the cell is empty.

        Returns:
            bool: True if the cell is empty, False otherwise.
        """
        return self.color == consts.back_color

    def is_fruit(self):
        """
        Check if the cell is a fruit.

        Returns:
            bool: True if the cell is a fruit, False otherwise.
        """
        return self.color == consts.fruit_color
