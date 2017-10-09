#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet, euclid3, math
from game import resources, graphics, hitbox

# Load the player image and set its achor to its center
player_image = pyglet.resource.image("spaceship.png")
graphics.center_image(player_image)

class Player(pyglet.sprite.Sprite):
	"""A class representing the player sprite."""
	
	def __init__(self):
		super().__init__(player_image, x = 600, y = 450)

		# Velocity variables
		self.velocity = euclid3.Vector2(0,0)
		self.min_speed = 0.05
		self.max_speed = 5
		
		# Acceleration variables
		self.acceleration = euclid3.Vector2(0,0)
		self.acceleration_constant = 0.1
		self.deceleration_constant = 0.001

		# Rotation variables
		self.rotate_speed = 1

		# Movement switches for key presses
		self.UP = False
		self.RIGHT = False
		self.DOWN = False
		self.LEFT = False
		
		# Hitbox
		self.hitbox = hitbox.Hitbox(self)
			
	def rotate_right(self):
		"""Rotates player sprite to the right when right arrow is pressed."""
		if self.RIGHT:
			self.rotation += self.rotate_speed
	
	def rotate_left(self):
		"""Rotates player sprite to the left when right arrow is pressed."""
		if self.LEFT:
			self.rotation -= self.rotate_speed

	def get_angle(self):
		"""Returns sprite rotation in radians."""
		return math.radians(self.rotation)

	def get_angle_components(self):
		"""Returns a tuple of the x and y components of a unit vector having the 
		same rotation angle as the player sprite."""
		angle = self.get_angle()
		x_component = math.sin(angle)
		y_component = math.cos(angle)
		return (x_component, y_component)

	def get_velocity_components(self):
		"""Returns a tuple of the x and y components of the player velocity
		vector."""
		x_component = self.velocity.x
		y_component = self.velocity.y
		return (x_component, y_component)
		
	def accelerate(self):
		"""Accelerates the sprite towards its rotation angle 
		when up arrow is pressed."""
		if self.UP:
			components = self.get_angle_components()
			self.acceleration.x = self.acceleration_constant*components[0]
			self.acceleration.y = self.acceleration_constant*components[1]
			self.velocity += self.acceleration
			
			# Adjust only velocity vector angle if maximum speed is exceeded
			if self.velocity.magnitude() > self.max_speed:
				self.velocity = self.max_speed*self.velocity.normalize()
		
	def decelerate(self):
		"""Decelerates the sprite opposite to its velocity vector
		when up arrow is not pressed."""
		if not self.UP:
			if self.velocity.magnitude() > 0:
				components = self.get_velocity_components()
				self.acceleration.x = -self.deceleration_constant*components[0]
				self.acceleration.y = -self.deceleration_constant*components[1]
				self.velocity += self.acceleration
				
				# Stop the sprite when the velocity vector magnitude is under its threshold
				if self.velocity.magnitude() < self.min_speed:
					self.velocity = euclid3.Vector2(0,0)

	def blink(self):
		"""Teleports the sprite towards its rotation angle."""
		#TODO Make this smoother
		components = self.get_angle_components()
		self.set_position(self.x+200*components[0], self.y+200*components[1])
		
	
	def move(self):
		"""Moves the player sprite."""
		self.rotate_right()
		self.rotate_left()
		self.accelerate()
		self.decelerate()
		self.set_position((self.x+self.velocity.x)%1200,\
			(self.y+self.velocity.y)%900)
		self.hitbox.move()
			
	def update(self, dt):
		"""Updates the player sprite."""
		self.move()
		self.draw()

