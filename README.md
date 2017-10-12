# ![](resources/spaceship.png) Rocket ![](resources/spaceship.png)
Rocket is a very minimalistic 2d game experiment built with `pyglet`.  
Currently, in Rocket you fly a lonely rocket with no purpose in the infinite darkness of space. However, game features and objectives are on the way!

## Prerequisites
The following python packages are required to run Rocket:
* `pyglet 1.2.4`
* `euclid3 0.1`

## Running the game
The game is launched by:
```sh
$ python3 main.py
```

## Controls
| Key           | Function      |
| ------------- | ------------- |
| `↑`          	| Accelerate    |
| `←`          	| Steer left    |
| `→`          	| Steer right   |
| `SPACE`       | Blink forward |

## Todos
Some ideas to implement:
* :star: Add stars with parallax
* :musical_note: Add awesome music
* :zap: Add laser guns
* :clapper: Add animations
* :space_invader: Add deadly enemies
* :collision: Add hitboxes for collisions
* :trophy: Add levels with score tracking

## Built with
* [pyglet](https://pypi.python.org/pypi/pyglet/1.2.4) - Cross-platform windowing and multimedia library
* [euclid3](https://pypi.python.org/pypi/euclid3) - 2D and 3D vector, matrix, quaternion and geometry module
