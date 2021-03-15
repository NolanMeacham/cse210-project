import arcade
from game.towerz import TowerzView
from game.add_enemy import Add_enemy
from game import constants

class StartView(arcade.View):
    def __init__(self, cast, script, input_service):
        super().__init__()
        self.cast = cast
        self.script = script
        self.input_service = input_service

    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)


    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Start Screen", constants.MAX_X / 2, constants.MAX_Y / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click Anywhere To Play", constants.MAX_X / 2, constants.MAX_Y / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
            
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        self.script['update'].append(Add_enemy())
        game_view = TowerzView(self.cast, self.script, self.input_service)
        game_view.setup()
        self.window.show_view(game_view)
