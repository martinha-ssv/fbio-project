import pygame
from sprites import SpriteObject # from game.sprites import SpriteObject
import constants as gc # import game.constants as gc


class Player():
    players = []
    def __init__(self, name, window, center, weights=(gc.default_weight_size, gc.default_weight_size)):
        self.name = name
        self.center = center
        self.window = window

        self.bar = SpriteObject(self.window, 'src/game/sprites/bar.png', center, gc.bar_center_start, gc.bar_length_px)
        self.left_weight = SpriteObject(self.window, 'src/game/sprites/weight-left.png', center - gc.bar_length_px//2, gc.bar_center_start, gc.default_weight_size)
        self.right_weight = SpriteObject(self.window, 'src/game/sprites/weight-right.png', center + gc.bar_length_px//2, gc.bar_center_start, gc.default_weight_size)
        self.arms = SpriteObject(self.window, 'src/game/sprites/arms.png', center, gc.arms_y, gc.body_width)

        self.body = SpriteObject(self.window, 'src/game/sprites/mrmeeseeks-body.png', center+gc.body_x_offset, gc.body_y, gc.body_width) # TODO anti-aliasing

        

        self.moving_parts = pygame.sprite.Group() #TODO test
        self.moving_parts.add(self.bar)
        self.moving_parts.add(self.arms)
        self.moving_parts.add(self.left_weight)
        self.moving_parts.add(self.right_weight)

        Player.players.append(self)

        # PHYSICAL CONSTANTS
        

    def getPlayerByName(name):
        for player in Player.players:
            if player.name == name:
                return player
            
    def updateWeights(self, left, right):
        # TODO
        self.Lw = left
        self.Rw = right

    def draw(self):
        self.left_weight.draw()
        self.right_weight.draw()
        self.bar.draw()
        self.arms.draw()
        self.body.draw()