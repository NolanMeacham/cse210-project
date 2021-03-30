import arcade
from game import constants
from game.music_handler import MusicHandler

class WinView(arcade.View):
    """
    Game Over view screen.

    """
    def __init__(self, start_screen, tower):
        """
        Class constructor.

        Args:
            self ():
            start_screen ():
            tower ();
        """
        super().__init__()
        self.start_view = start_screen
        self.tower = tower
        self.music = start_screen.music
        self.music.clear_queue()
        self.music.add_song_list(constants.WIN_SOUND)
        self.music.play_song()
    def on_show(self):
        """
        """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)


    def on_draw(self):
        """
        Draw this view
        
        """
        arcade.start_render()
        arcade.draw_text("You Won! Kinda", constants.MAX_X / 2, constants.MAX_Y / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click Anywhere to Go to Main Menu", constants.MAX_X / 2, constants.MAX_Y / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
            
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """
        If the user presses the mouse button, start the game
        
        """
        self.tower.cur_health = constants.TOWER_HEALTH
        self.window.show_view(self.start_view)
