import arcade
from game import constants
# from game.start_screen import StartView

class InstructionView(arcade.View):

    def __init__(self, start):

        super().__init__()
        self.start = start
        self.texture = arcade.load_texture(constants.INSTRUCTION_IMAGE)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK_OLIVE)

    def on_draw(self):
        """
        Draw this view 
        
        Args:
            self (StartView): an instance of StartView
        """
        arcade.start_render()
        arcade.draw_text("Instructions", constants.MAX_X / 2, constants.MAX_Y - 75,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("(Press any key to return to start screen)", constants.MAX_X / 2, constants.MAX_Y - 100,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

        self.texture.draw_sized(constants.MAX_X / 2 - 85, constants.MAX_Y / 2, constants.MAX_X - 150, constants.MAX_Y - 150)

        
        arcade.draw_text("JUST WIN DUDE!", constants.MAX_X / 2, 40,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        

    def on_key_press(self, symbol, modifiers):
        
        game_view = self.start
        self.window.show_view(game_view)