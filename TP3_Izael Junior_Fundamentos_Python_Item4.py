import pygame

pygame.init()
largura_tela = 800
altura_tela = 600
tela=pygame.display.set_mode((largura_tela,altura_tela))
preto = (0,0,0)
branco = (255,255,255)
azul = (0,0,255)
amarelo = (255,255,0)
vermelho = (255,0,0)
terminou = False
contador = 0
    
clock = pygame.time.Clock()

font = pygame.font.Font(None,32)
texto_quadrado = "Quadrado"
text = font.render(texto_quadrado, 1, amarelo)
tela.blit(text, (100,120))

texto_quadrado = "Circulo"
text = font.render(texto_quadrado, 1, branco)
tela.blit(text, (360,360))

pygame.draw.rect(tela, vermelho, (100,10, 100,100))
pygame.draw.circle(tela, azul,(400,300), 50)

while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
               
    pygame.display.update()
    
    if contador == 180:
        pygame.draw.rect(tela, azul, (100,10, 100,100))
        pygame.draw.circle(tela, vermelho,(400,300), 50)
        
    clock.tick(60)
    contador = contador + 1

pygame.display.update()

pygame.display.quit()

pygame.quit()


