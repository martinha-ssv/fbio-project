import pygame
from sprites import SpriteObject
import constants as gc
import numpy as np
from player import Player


class MovingParts():
    def __init__(self, sprite_group, pivot, player):
        self.player = player
        self.moving_parts = sprite_group
        self.pivot = pivot
        self.theta = 0 # Angle between a line vertical to the bar and the horizontal
        self.inertia = 
        
def rotateGroupAroundPoint(group, theta, pivot):
    for sprite in group:
        sprite.rotate_around_point(theta, pivot)

def calculateTorque

