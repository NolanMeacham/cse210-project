import arcade
from game import constants
# from game.start_screen import StartView

class InstructionView(arcade.View):

    def __init__(self):

        super().__init__()

    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

    def on_draw(self):
        """
        Draw this view 
        
        Args:
            self (StartView): an instance of StartView
        """
        arcade.start_render()
        arcade.draw_text("Instruction screen", constants.MAX_X / 2, constants.MAX_Y / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Just win dude", constants.MAX_X / 2, constants.MAX_Y / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Press any key to return to start screen", constants.MAX_X / 2, constants.MAX_Y / 2-100,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    # def on_key_press(self, symbol, modifiers):
        
    #     game_view = StartView()
    #     self.window.show_view(game_view)