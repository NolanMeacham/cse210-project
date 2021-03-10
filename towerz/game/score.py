# Import statements
from game import constants
import arcade

class Score():
    """
    """
    def __init__(self):
        """
        """
        self.x = 10
        self.y = 10
        self.change_x = 0
        self.change_y = 0
        
        self._score = 0

    def draw(self):
        """
        """
        score_text = f"Score: {self._score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.WHITE, 18)

    def get_score(self):
        """
        """
        return self._score

    def add_points(self, points):
        """
        """
        self._score += points