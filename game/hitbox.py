#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pyglet

class Hitbox:
    """A class representing a hitbox used for sprites. A hitbox is attached 
    to a sprite and is used to compute collisions to other sprites."""
    
    def __init__(self, sprite):
        """Initializes hitbox class. Attaches sprite and sets dimensions."""
        self.sprite = sprite
        self.width = sprite.width
        self.height = sprite.height
        self.move()
        
    def move(self):
        """Moves the center of the hitbox to the position of the 
        player sprite."""
        self.x = self.sprite.x
        self.y = self.sprite.y
        self.set_angle()
        self.set_corners()
        
    def set_angle(self):
        """Sets the angle of the hitbox to the rotation angle of the sprite."""
        self.rotation = math.radians(self.sprite.rotation)+math.pi/2
        
    def set_corners(self):
        """Sets the four corners of the hitbox according to the position and 
        rotation angle of the hitbox. A list of four tuples is used to describe 
        the coordinates of the four corners. The order is top right, bottom 
        right, bottom left, top left."""
        
        # Initialize corners with relative positions
        tr = [+self.width/2, +self.height/2]
        br = [+self.width/2, -self.height/2]
        bl = [-self.width/2, -self.height/2]
        tl = [-self.width/2, +self.height/2]
        
        # Adjust corner positions according to hitbox rotation angle
        tr = [tr[0]*math.sin(self.rotation)-tr[1]*math.cos(self.rotation),\
                tr[0]*math.cos(self.rotation)+tr[1]*math.sin(self.rotation)]
        br = [br[0]*math.sin(self.rotation)-br[1]*math.cos(self.rotation),\
                br[0]*math.cos(self.rotation)+br[1]*math.sin(self.rotation)]
        bl = [bl[0]*math.sin(self.rotation)-bl[1]*math.cos(self.rotation),\
                bl[0]*math.cos(self.rotation)+bl[1]*math.sin(self.rotation)]
        tl = [tl[0]*math.sin(self.rotation)-tl[1]*math.cos(self.rotation),\
                tl[0]*math.cos(self.rotation)+tl[1]*math.sin(self.rotation)]
        
        # Adjust corner positions according to hitbox position
        tr = [int(self.x+tr[0]), int(self.y+tr[1])]
        br = [int(self.x+br[0]), int(self.y+br[1])]
        bl = [int(self.x+bl[0]), int(self.y+bl[1])]
        tl = [int(self.x+tl[0]), int(self.y+tl[1])]
        
        self.corners = [tr, br, bl, tl]
        
    def draw_corners(self):
        """Draws the four corners of the hitbox on the game board."""
        for i in range(4):
            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,\
                ('v2f', (self.corners[i][0],self.corners[i][1])),\
                ('c3B', (0, 255, 255)))
                
    def check_collision(self, hitbox):
        """Checks if the hitbox collides with another hitbox"""
        #TODO
        pass
        
    def update(self):
        """Updates the hitbox variables."""
        self.move()
        self.draw()

