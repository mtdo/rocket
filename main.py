#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
from game import graphics, player, gameboard
from pyglet.window import key

# Create a game window and set its location to the middle
game_window = gameboard.GameBoard()

# Create player sprite
player = player.Player()
player.scale = 1

@game_window.event
def on_draw():
    """Draws game objects on screen."""
    game_window.clear()
    player.draw()
    #player.hitbox.draw_corners()
    
@game_window.event
def on_key_press(symbol, modifier):
    """Registers player key presses."""
    if symbol == key.UP:
        player.UP = True
    elif symbol == key.RIGHT:
        player.RIGHT = True
    elif symbol == key.DOWN:
        player.DOWN = True
    elif symbol == key.LEFT:
        player.LEFT = True
    elif symbol == key.SPACE:
        player.blink()
        
@game_window.event
def on_key_release(symbol, modifier):
    """Registers player key releases."""
    if symbol == key.UP:
        player.UP = False
    elif symbol == key.RIGHT:
        player.RIGHT = False
    elif symbol == key.DOWN:
        player.DOWN = False
    elif symbol == key.LEFT:
        player.LEFT = False
        
# Game engine clock for game updates
pyglet.clock.schedule_interval(player.update, 1/120)

if __name__ == "__main__":
    pyglet.app.run()

