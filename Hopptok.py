# Importowanie modułów
import sys
import random 
import pygame 
  
# Deklaracja zmiennych okna 
window_width = 800
window_height = 500

import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
screen = pygame.display.set_mode((window_width, window_height))

# Ustawienia ptaka
bird = pygame.Rect(35, 35, 35, 35)

# Ustawienia grawitacji
gravity = 0.25
bird_movement = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 6

    screen.fill((255, 255, 255))
    bird_movement += gravity
    bird.centery += bird_movement
    pygame.draw.rect(screen, (255, 0, 0), bird)
    pygame.display.update()
