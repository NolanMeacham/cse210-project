
HERO_MOVE_SCALE = 4
HERO_IMAGE = "towerz/images/blue_rectangle.png"
HERO_SLASH_SOUND = "towerz/sounds/sword_slash.m4a"
HERO_HIT_SOUND = "towerz/sounds/hero_gets_hit.m4a"
HERO_RESOURCE_SOUND = "towerz/sounds/hit_resource_sound.m4a"
ZOMBIE_IMAGE = "towerz/images/red_rectangle.png"
WALL_IMAGE = "towerz/images/wall_h.png"
# BACKGROUND = "towerz/images/background.png"
BACKGROUND = "towerz/images/towerz_map.png"
INSTRUCTION_IMAGE = "towerz/images/instructions_image.png"
HERO_Y = 100

UPDATES_PER_FRAME = 12

RIGHT_FACING = 0
LEFT_FACING = 1

MAX_X = 1200
MAX_Y = 800
HERO_SCALING = 0.01
ZOMBIE_SCALING = 1.25

HEALTHBAR_WIDTH = 25
HEALTHBAR_HEIGHT = 3
HEALTHBAR_OFFSET_Y = -10

HEALTH_NUMBER_OFFSET_X = -10
HEALTH_NUMBER_OFFSET_Y = -25

#Hero
HERO_HEALTHBAR_WIDTH = 250
HERO_HEALTHBAR_HEIGHT = 20
HERO_HEALTHBAR_OFFSET_Y = 0

HERO_HEALTH_NUMBER_OFFSET_X = 0
HERO_HEALTH_NUMBER_OFFSET_Y = 0

HERO_HEALTH_X = MAX_X/2
HERO_HEALTH_Y = 50

# Tower
# TOWER_IMAGE = "towerz/images/gray_castle.png"
TOWER_IMAGE = "towerz/images/gray_rectangle.png"
TOWER_SCALE = 4
TOWER_X = MAX_X / 2
TOWER_Y = MAX_Y / 2
TOWER_HEALTH = 500
TOWER_HEALTH_X = 1000
TOWER_HEALTH_Y = 50

# Turret
TURRET_IMAGE = "towerz/images/cannon.png"
TURRET_SCALE = 0.15
TURRET_X = MAX_X / 2
TURRET_Y = MAX_Y / 2 + 10
TURRET_HEALTH =  20

# Bullet
# BULLET_IMAGE = "towerz/images/small_gray_rect.png"
BULLET_IMAGE = "towerz/images/cannon_ball.png"
BULLET_BLAST_IMAGE = "towerz/images/cannon_blast.png"
BULLET_SOUND = "towerz/sounds/turret_updated.m4a"
BULLET_SCALE = 0.07
BULLET_SPEED = 7

#zombie
ZOMBIE_SPEED = 0.25
ZOMBIE_HIT = .1
ZOMBIE_POINTS = 2
BIG_ZOMBIE_POINTS = 7

#wall
WALL_SCALING = 1
WALL_LIFETIME = 20
WALL_MAGIC_IMG = 'towerz/images/lightning.png'
WALL_MAGIC_SCALING = .1
MAGIC_SPEED = 50
MAGIC_SOUND = 'towerz/sounds/magic_sound.wav'

#Resource
RESOURCE_IMAGE = "towerz/images/crystal2.png"
RESOURCE_SCALING = 0.3

RESOURCE_COUNTER_WIDTH = 250

DIFFICULTY = 1.0
SPAWN_DIFFICULTY_MODIFIER = .0002
SPEED_DIFFICULTY_MODIFIER = .00008

#music assets
BACKGROUND_MUSIC = ['towerz/sounds/background.mp3']
DEATH_SOUND = ['towerz/sounds/death_theme.mp3']
MUSIC_VOLUME = 0.18

CROSS_HAIR = 'towerz/images/cross_hair.png'
WIN_SOUND = ['towerz/sounds/victory.mp3']
