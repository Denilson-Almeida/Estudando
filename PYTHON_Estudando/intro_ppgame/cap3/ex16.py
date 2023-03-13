import pygame
from pygame.locals import *
from sys import exit

pygame.init()

tamanho_tela = (800, 600)
tela = pygame.display.set_mode(tamanho_tela, 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        print(event)
    
    pygame.display.update()