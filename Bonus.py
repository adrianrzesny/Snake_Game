import pygame
import random

class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        super(Bonus, self).__init__()
        self.image = pygame.image.load("images/bonus.png")
        random_position = pygame.Rect(random.randrange(1,25)*32, random.randrange(1,19)*32, 32, 32)
        self.rect = random_position
        pass
    pass

