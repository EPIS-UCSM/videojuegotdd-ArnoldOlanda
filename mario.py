import arcade

#Dimensiones y titulo de la ventana
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Mario Demo"

#Constantes para escalar los sprites
CHARACTER_SCALING = 0.20
GROUND_SCALING = 0.20


#Viewports
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

class MyGame(arcade.Window):
	

	def __init__(self,player_speed,player_jump):

		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
		self.PLAYER_MOVEMENT_SPEED = player_speed
		self.PLAYER_JUMP_SPEED = player_jump

		arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

		self.wall_list = None
		self.player_list = None

		#Variable del sprite jugador
		self.player_sprite = None

		#Seguimiento de camara
		self.view_bottom = 0
		
		self.view_left = 0


	def setup(self):
		self.player_list = arcade.SpriteList()
		self.wall_list = arcade.SpriteList()

		#Jugador
		image_source = "mario.png"
		self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
		self.player_sprite.center_x = 64
		self.player_sprite.center_y = 93
		self.player_list.append(self.player_sprite)

		#Creacion del piso
		for x in range(0, 2050, 64):
			wall = arcade.Sprite("ground.png", GROUND_SCALING)
			wall.center_x = x
			wall.center_y = 32
			self.wall_list.append(wall)
		
		self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
	
	def on_draw(self):
		arcade.start_render()
		self.player_list.draw()
		self.wall_list.draw()

	def on_key_press(self, key, modifiers):
		#Controlar el movimiento
		if key == arcade.key.UP or key == arcade.key.W:
			self.player_sprite.change_y = self.PLAYER_JUMP_SPEED
			return "arriba"
		elif key == arcade.key.DOWN or key == arcade.key.S:
			self.player_sprite.change_y = -self.PLAYER_JUMP_SPEED
			return "abajo"
		elif key == arcade.key.LEFT or key == arcade.key.A:
			self.player_sprite.change_x = -self.PLAYER_MOVEMENT_SPEED
			return "izquierda"
		elif key == arcade.key.RIGHT or key == arcade.key.D:
			self.player_sprite.change_x = self.PLAYER_MOVEMENT_SPEED
			return "derecha"
		
	def on_key_release(self, key, modifiers):
		#Evitar el movimiento infinito
		if key == arcade.key.UP or key == arcade.key.W:
			self.player_sprite.change_y = 0
		elif key == arcade.key.DOWN or key == arcade.key.S:
			self.player_sprite.change_y = 0
		elif key == arcade.key.LEFT or key == arcade.key.A:
			self.player_sprite.change_x = 0
		elif key == arcade.key.RIGHT or key == arcade.key.D:
			self.player_sprite.change_x = 0

	def on_update(self, delta_time):

		# Actualizar movimiento del jugador
		self.physics_engine.update()

		changed = False

        # Scroll izquierda
		left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
		if self.player_sprite.left < left_boundary:
			self.view_left -= left_boundary - self.player_sprite.left
			changed = True

		# Scroll derecha
		right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
		if self.player_sprite.right > right_boundary:
			self.view_left += self.player_sprite.right - right_boundary
			changed = True

		# Scroll arriba
		top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
		if self.player_sprite.top > top_boundary:
			self.view_bottom += self.player_sprite.top - top_boundary
			changed = True

        # Scroll abajo
		bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
		if self.player_sprite.bottom < bottom_boundary:
			self.view_bottom -= bottom_boundary - self.player_sprite.bottom
			changed = True

		if changed:

			self.view_bottom = int(self.view_bottom)
			self.view_left = int(self.view_left)
			arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left, self.view_bottom,SCREEN_HEIGHT + self.view_bottom)

def main():
	window = MyGame(10,25)
	window.setup()
	arcade.run()

if __name__ == "__main__":
	main()