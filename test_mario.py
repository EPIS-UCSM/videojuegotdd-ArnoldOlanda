import arcade
from mario import MyGame

CYLINDER_SCALING = 0.20

window = MyGame(10,25)
window.setup()
#arcade.run()


def test_move_up():
    assert window.on_key_press(arcade.key.UP,None) == "arriba"
    
def test_move_down():
    assert window.on_key_press(arcade.key.DOWN,None) == "abajo"

def test_move_left():
    assert window.on_key_press(arcade.key.LEFT,None) == "izquierda"

def test_move_right():
    assert window.on_key_press(arcade.key.RIGHT,None) == "derecha"


def test_speed_player():
    assert window.PLAYER_MOVEMENT_SPEED == 10

def test_jump_player():
    assert window.PLAYER_JUMP_SPEED == 25

#######################################################################################
def test_sound_background_name():
    assert window.background_name == 'super-mario-bros.mp3'

def test_sound_jump_name():
    assert window.jump_name == 'mario-bros-jump.mp3'

def test_position_player():
    assert window.on_update(delta_time=None) == [window.player_sprite.center_y,window.player_sprite.center_x]

def test_position_player2():    
    assert window.on_key_release(arcade.key.LEFT,None) == window.player_sprite.center_x

def obstaculo():
    wall = arcade.Sprite("cylinder.png", CYLINDER_SCALING)
    assert window.wall_list.append(wall) == "cilindro"

def posicion_obstaculo():
    wall = arcade.Sprite("cylinder.png", CYLINDER_SCALING)
    assert wall.position== [256, 110]

def posicion_obstaculo1():
    wall = arcade.Sprite("cylinder.png", CYLINDER_SCALING)
    assert wall.position== [865, 110]

def posicion_obstaculo2():
    wall = arcade.Sprite("cylinder.png", CYLINDER_SCALING)
    assert wall.position== [3800, 110]

def posicion_obstaculo3():
    wall = arcade.Sprite("cylinder.png", CYLINDER_SCALING)
    assert wall.position== [1200, 110]
