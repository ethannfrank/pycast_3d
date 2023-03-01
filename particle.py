import math

import pygame.math

from settings import *
from ray import Ray


class Particle:

    def __init__(self):
        self.pos = pygame.math.Vector2(100, 100)
        self.rays = []
        self.heading = 0
        for a in range(-30, 30, 1):
            self.rays.append(Ray(self.pos, math.radians(a)))

    def rotate(self, angle):
        self.heading += angle
        for i in range(0, len(self.rays), 1):
            self.rays[i].setAngle(math.radians(i) + self.heading)

    def move(self, amt):
        vel = pygame.math.Vector2(math.cos(self.heading), math.sin(self.heading))
        vel = vel.magnitude() * amt
        self.pos.__add__(vel)

    def update(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def look(self, window, walls):
        scene = []
        for i in range(0, len(self.rays)):
            closest = None
            record = math.inf
            for wall in walls:
                pt = self.rays[i].cast(wall)
                if pt:
                    d = pygame.Vector2.distance_to(self.pos, pt)
                    if d < record:
                        record = d
                        closest = pt
            if closest:
                pygame.draw.line(window, WHITE, self.pos, closest)
            scene.append(record)
        return scene

    def show(self, window):
        for ray in self.rays:
            ray.show(window)
        pygame.draw.circle(window, WHITE, (self.pos.x, self.pos.y), 4)