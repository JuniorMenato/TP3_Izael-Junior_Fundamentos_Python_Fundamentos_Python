import pygame
import random

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
terminou = False
red = (255,0,0)


  # Cria relógio
clock = pygame.time.Clock()


class Quadradinho():
    def __init__(self):
        self.largura = 50
        self.altura = 50
        self.x = random.randint(0,largura_tela-self.largura)
        self.y = random.randint(0,altura_tela-self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = (random.randint(20,255), random.randint(20,255), random.randint(20,255))
    def desenha (self,tela):
        pygame.draw.rect(tela,self.cor,self.area)


lista=[]
for i in range (0,1):
    q = Quadradinho()
    q.desenha(tela)
    lista.append(q)


while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            pos = pygame.mouse.get_pos()
            for q in lista:
                if q.area.collidepoint(pos):
                    lista.remove(q)
                                        
            if event.type == pygame.QUIT:
                terminou = True
     
     
    tela.fill(red)
    for q in lista:
            q.desenha(tela)
    
    # Atualiza o desenho na tela
    pygame.display.update()

  
clock.tick(60)

  # Finaliza a janela do jogo
pygame.display.quit()
 # Finaliza o pygame
pygame.quit()