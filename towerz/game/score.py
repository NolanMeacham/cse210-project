# Import statements
from game import constants
import arcade

class Score():
    """

    Stereotype:
        Information  Holder

    Attributes:
        x, y (int): x and y coordinates for position on screen
        change_x, change_y (int): velocity, necessary for arcade updates
        score (int): keeps track of total score
    """
    def __init__(self):
        """
        Class constructor.

        Args:
            self (Score): an instance of Score.
        """
        self.center_x = 10
        self.center_y = constants.MAX_Y - 30
        self.change_x = 0
        self.change_y = 0

        self._score = 0

    def draw(self):
        """
        Draws the score text at the x and y position on screen.

        Args:
            self (Score): an instance of Score.
        """
        score_text = f"Score: {self._score}"
        arcade.draw_text(score_text, self.center_x, self.center_y, arcade.csscolor.WHITE, 18)

    def get_score(self):
        """
        Returns the value of the score attribute.

        Args:
            self (Score): an instance of Score.
        """
        return self._score

    def add_points(self, points):
        """
        Adds a number of points to the total score attribute.

        Args:
            self (Score): an instance of Score.
            points (int): the number of points to be added to the score.
        """
        self._score += points