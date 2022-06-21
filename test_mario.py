import arcade
from mario import MyGame


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