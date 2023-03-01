import math
import random
import sys
import pygame

from boundary import Boundary
from particle import Particle
from settings import *

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyCast")

walls = []
particle = Particle()

for i in range(0, NUM_WALLS):
    x1 = random.randint(0, MAP_WIDTH)
    y1 = random.randint(0, MAP_HEIGHT)
    x2 = random.randint(0, MAP_WIDTH)
    y2 = random.randint(0, MAP_HEIGHT)
    walls.append(Boundary(x1, y1, x2, y2))
walls.append(Boundary(1, 1, MAP_WIDTH-1, 1))
walls.append(Boundary(MAP_WIDTH-1, 1, MAP_WIDTH-1, MAP_HEIGHT-1))
walls.append(Boundary(MAP_WIDTH-1, MAP_HEIGHT-1, 1, MAP_HEIGHT-1))
walls.append(Boundary(1, MAP_HEIGHT, 1, 1))


def remap(old_val, old_min, old_max, new_min, new_max):
    if old_val > old_max:
        return new_max
    return (new_max - new_min)*(old_val - old_min) / (old_max - old_min) + new_min


def calc_hypo(a, b):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))


def draw():
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    window.fill(BLACK)

    for wall in walls:
        wall.show(window)

    particle.update(mouseX, mouseY)
    particle.show(window)

    scene = particle.look(window, walls)

    w = MAP_WIDTH / len(scene)
    for j in range(0, len(scene)):
        sq = scene[j] * scene[j]
        wSq = MAP_WIDTH * MAP_WIDTH
        b = remap(sq, 0, wSq, 255, 0)
        h = remap(scene[j], 0, MAP_WIDTH, MAP_HEIGHT, 0)
        yoff = (HEIGHT - h) / 2
        pygame.draw.rect(window, (b, b, b), (j * w + MAP_WIDTH, yoff, w, h))
        # pygame.draw.line(window, RED, (j * w + MAP_WIDTH, yoff + h), ((j + 1) * w + MAP_WIDTH, yoff + h))

    # ray.show(window)
    # ray.lookAt(mouseX, mouseY)

    # pt = ray.cast(wall)
    # if pt:
    #     pygame.draw.circle(window, WHITE, (pt.x, pt.y), 8)
    pygame.display.update()


def setup():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            particle.rotate(-0.05)
        if keys_pressed[pygame.K_RIGHT]:
            particle.rotate(0.05)
        if keys_pressed[pygame.K_UP]:
            particle.move(1)
        if keys_pressed[pygame.K_DOWN]:
            particle.move(-1)
        draw()


if __name__ == "__main__":
    setup()