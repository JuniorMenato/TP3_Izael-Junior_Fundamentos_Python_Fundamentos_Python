import pygame
import random

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
terminou = False

  # Cria relógio
clock = pygame.time.Clock()

while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True
            
            print(event)
  
  
    pygame.display.update()

  
clock.tick(60)

  # Finaliza a janela do jogo
pygame.display.quit()
 # Finaliza o pygame
pygame.quit()