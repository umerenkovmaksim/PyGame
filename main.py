import pygame

pygame.init()
block = True
size = width, height = 300, 200
screen = pygame.display.set_mode(size)
screen.fill('red')
pygame.display.set_caption('Кирпичи')
pygame.display.flip()
for i in range(15, height + 15, 17):
    pygame.draw.line(screen, 'white', (0, i), (width, i), width=2)
    for j in range(30 if block else 15, width, 32):
        pygame.draw.line(screen, 'white', (j, i), (j, i - 15), width=2)
    block = not block
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
