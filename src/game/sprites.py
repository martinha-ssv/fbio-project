import pygame
import numpy as np

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, surface, image_file, x, y, width, height=None):
        super().__init__()
        self.surface = surface
        self.image = pygame.image.load(image_file)

        original_width, original_height = self.image.get_size()
        if height is None:
            aspect_ratio = original_height / original_width
            height = int(width * aspect_ratio)
        
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, x=None, y=None, surface=None):
        if x is None or y is None: x, y = self.rect.center
        if surface is None: surface = self.surface 
        self.rect.center = (x, y)
        surface.blit(self.image, self.rect)

    def rotate_around_point(self, theta, pivot):
        last_coords = np.array(self.rect.center)
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        r_pivot = last_coords - pivot
        rotated_rpivot = rotation_matrix @ (r_pivot)
        new_coords = pivot + rotated_rpivot

        self.rect.center = new_coords
        return new_coords, pygame.transform.rotate(self.image, np.degrees(theta))

    def update(self):
        pass