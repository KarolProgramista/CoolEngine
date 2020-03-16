from Window import *
from GameObjects import *
import pygame

pygame.init()

KEY_1 = pygame.K_1
KEY_2 = pygame.K_2
KEY_3 = pygame.K_3
KEY_4 = pygame.K_4
KEY_5 = pygame.K_5
KEY_6 = pygame.K_6
KEY_7 = pygame.K_7
KEY_8 = pygame.K_8
KEY_9 = pygame.K_9
KEY_0 = pygame.K_0
KEY_a = pygame.K_a
KEY_b = pygame.K_b
KEY_c = pygame.K_c
KEY_d = pygame.K_d
KEY_e = pygame.K_e
KEY_f = pygame.K_f
KEY_g = pygame.K_g
KEY_h = pygame.K_h
KEY_i = pygame.K_i
KEY_j = pygame.K_j
KEY_k = pygame.K_k
KEY_l = pygame.K_l
KEY_m = pygame.K_m
KEY_n = pygame.K_n
KEY_o = pygame.K_o
KEY_p = pygame.K_p
KEY_q = pygame.K_q
KEY_r = pygame.K_r
KEY_s = pygame.K_s
KEY_t = pygame.K_t
KEY_u = pygame.K_u
KEY_v = pygame.K_v
KEY_w = pygame.K_w
KEY_x = pygame.K_x
KEY_y = pygame.K_y
KEY_z = pygame.K_z
KEY_LEFT = pygame.K_LEFT
KEY_RIGHT = pygame.K_RIGHT
KEY_UP = pygame.K_UP
KEY_DOWN = pygame.K_DOWN

# This function takes window and key
# If passed key has been clicked in this window function return True
# If not return False
def Input(window, key):
    for event in window._events:
        if event == key:
            return True
    return False

