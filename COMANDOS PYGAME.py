#IMPORTA BIBLIOTECA
import pygame
#INICIA OS MÓDULOS DA BIBLIOTECA PYGAME
pygame.init()

#CRIA A JANELA
screen = pygame.display.set_mode((600,400))

#TÍTULO DA JANELA
pygame.display.set_caption('Hello Pygame!')

#COR DA JANELA
screen.fill((255,255,255))

#ATUALIZA JANELA
pygame.display.flip()

#DESENHA LINHA
pygame.draw.line(screen, (0, 255, 0), [50, 95], [500, 95], 5)
pygame.display.flip()

#DESENHA SEGMENTO DE LINHA
pygame.draw.lines(screen, (0, 0, 0), False, [(0, 80), (50, 90), (200, 80), (220, 30)], 5)
pygame.display.flip()

#DESENHA UM RETÂNGULO
pygame.draw.rect(screen, (255, 0, 0), [(150, 10), (50, 20)])
pygame.display.flip()

#DESENHA UM POLÍGONO
pygame.draw.polygon(screen, (0, 0, 0), [(100, 100), (0, 200), (200, 200)], 2)
pygame.display.flip()

#DESENHA UM CÍRCULO
pygame.draw.circle(screen, (0, 0, 255), (60, 250), 40)
pygame.display.flip()

#DESENHA UMA ELÍPSE
pygame.draw.ellipse(screen, (255, 0, 0), [(300, 10), (50, 20)])
pygame.display.flip()

#ESCREVE NA JANELA
myfont = pygame.font.SysFont("Arial", 60)
label = myfont.render("Hello Pygame!", 1, (255, 0, 255))
screen.blit(label, (150,250))
pygame.display.update()

#EVENT LOOP TO CLOSE WINDOW
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False