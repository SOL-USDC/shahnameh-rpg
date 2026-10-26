import pygame
from settings import SCALE 

def load_image(path):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, (image.get_width() * SCALE, image.get_height() * SCALE))