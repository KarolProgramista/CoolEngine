import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((300, 300))

clock = pygame.time.Clock()

img = pygame.image.load("bee.png")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 255))
    
    r_img = pygame.transform.scale(img, (100, 100))
    r_img = pygame.transform.rotate(r_img, -90)
    screen.blit(r_img, (10, 10))
    clock.tick(60)
    pygame.display.update()