import arcade
from game.music_handler import MusicHandler
from game import constants


class TowerzView(arcade.View):
    """
    """
    def __init__(self, cast, script, input_service):
        """
        Class constructor. Initializes the game.

        Args:
            self (TowerzView): 
            cast (dict): 
            script (dict):
            input_service ():

        """
        super().__init__()
        # The "True" boolean above is what makes it go fullscreen. Go ahead and delete it if you don't want it fullscreen
        self._cast = cast
        self._script = script
        self._input_service = input_service
        self.music = MusicHandler()
        self.music.add_song_list(constants.BACKGROUND_MUSIC)
        self.music.play_song_looped()


    def on_show(self):
        """

        Args:
            self (Towerz): an instance of Towerz

        """
        # Reinitializes all game components when game is shown. This ensures that the restart works correctly
        self._cast["zombies"] = arcade.SpriteList()
        self._cast["walls"] = arcade.SpriteList()
        self._cast["resource_counter"][0].cur_health = 0
        self._cast["hero"][0].cur_health = 100
        self._cast["hero"][0].center_x = int(constants.MAX_X / 2)
        self._cast["hero"][0].center_y = int(constants.HERO_Y)
        self._cast["score"][0].set_points(0)
        self._cast["bullets"] = []
        self._cast["turrets"] = arcade.SpriteList()
        self._script["update"][3].count = 0
        self._script["update"][3].wave = "Wave 1"
        for resource in self._cast["resources"]:
            resource.cur_health = 0


    def setup(self):
        """

        Args:
            self (Towerz): an instance of Towerz
        """
        arcade.set_background_color(arcade.color.BLACK)
        
     

    def on_update(self, delta_time):
        """

        Args:
            self (Towerz): an instance of Towerz
            delta_time (): the time between each method call
        """
        # self._cast['hero'][0].update_animation()
        self._cue_action("update")

        self._script["output"][0]._add_enemy = self._script["update"][3]



    def on_draw(self):
        """

        Args:
            self (Towerz): an instance of Towerz
        """
       
        self._cue_action("output")
        

    def on_key_press(self, symbol, modifiers):
        """

        Args:
            self (Towerz): an instance of Towerz
            symbol (): 
            modifiers ():
        """
        self._input_service.set_key(symbol, modifiers)
        self._cue_action("input")


    def on_key_release(self, symbol, modifiers):
        """

        Args:
            self (Towerz): an instance of Towerz
            symbol ():
            modifiers ():
        """
        self._input_service.remove_key(symbol, modifiers)
        self._cue_action("input")


    def on_mouse_motion(self, x, y, dx, dy):
        """

        Args:
            self (Towerz): an instance of Towerz
            x ():
            y ():
            dx ():
            dy ():
        """
        self._input_service.mouse_move(x, y)
        self._cue_action("input")


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            self (Towerz): an instance of Towerz
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)
