import pygame.draw

from settings import *


class Boundary:

    def __init__(self, x1, y1, x2, y2):
        self.a = pygame.math.Vector2(x1, y1)
        self.b = pygame.math.Vector2(x2, y2)

    def show(self, window):
        pygame.draw.line(window, WHITE, self.a, self.b)