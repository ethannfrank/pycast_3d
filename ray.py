import math
import pygame.math

from settings import *


class Ray:

    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = pygame.math.Vector2(math.cos(angle), math.sin(angle))

    def setAngle(self, a):
        self.dir = pygame.math.Vector2(math.cos(a), math.sin(a))

    def lookAt(self, x, y):
        self.dir.x = x - self.pos.x
        self.dir.y = y - self.pos.y
        self.dir = pygame.math.Vector2(self.dir).normalize()

    def show(self, window):
        pygame.draw.line(window, WHITE, self.pos, self.pos + self.dir * 10)

    # def show(self, window):
    #     pygame.draw.line(window, WHITE, self.pos,
    #                      (pygame.mouse.get_pos()[0] / self.pos.x * 10 + self.pos.x,
    #                       pygame.mouse.get_pos()[1] / self.pos.y * 10 + self.pos.y))

    def cast(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if den == 0:
            return

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if 0 < t < 1 and u > 0:
            pt = pygame.math.Vector2()
            pt.x = x1 + t * (x2 - x1)
            pt.y = y1 + t * (y2 - y1)
            return pt
        else:
            return