import arcade
from game.towerz import TowerzView
from game.add_enemy import Add_enemy
from game.instruction_view import InstructionView
from game import constants

class StartView(arcade.View):
    """
    """
    def __init__(self, cast, script, input_service):
        """
        Class constructor. Starts by calling the constructor of the parent class.

        Args:
            self (): an instance of StartView
            cast (dict):
            script (dict):
            input_service ():
        """
        super().__init__()
        self.cast = cast
        self.script = script
        self.input_service = input_service
        self.background = arcade.load_texture('towerz/images/start_screen.PNG')

    def on_show(self):
        """

        Args:
            self (StartView): an instance of StartView
        """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)


    def on_draw(self):
        """
        Draw this view 
        
        Args:
            self (StartView): an instance of StartView
        """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            constants.MAX_X, constants.MAX_Y,
                                            self.background)
        arcade.draw_text("Towerz", 150, 700,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click Anywhere To Play", 1000, 100,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Press any key for instructions", 1000, 50, 
                         arcade.color.WHITE, font_size=20, anchor_x="center")
            
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ 
        If the user presses the mouse button, start the game. 
        
        Args:
            self (StartView): and instance of StartView
            x (): 
            y ():
            button ():
            modifiers ():
        """
        self.script['update'].append(Add_enemy())
        game_view = TowerzView(self.cast, self.script, self.input_service)
        game_view.setup()
        self.window.show_view(game_view)
    
    def on_key_press(self, symbol, modifiers):
        
        game_view = InstructionView(self)
        self.window.show_view(game_view)



