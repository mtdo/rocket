#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet

class GameBoard(pyglet.window.Window):
    """A class representing the game board (environment)."""
    
    def __init__(self):
        """Initializes the game board. The game board is initialized empty and 
        objects are added to the game board with the respective method."""
        super().__init__(width = 1200, height = 900, caption="Rocket")
        self.objects = []
        
    def add_game_object(self, game_object):
        """Adds game object to the game board."""
        self.objects.append(game_object)

