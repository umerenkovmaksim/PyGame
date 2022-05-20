import pygame

w, n = str(input()).split()
if '.' not in w or '.' not in n:
    try:
        w, n = int(w), int(n)
        pygame.init()
        colors = ['red', 'green', 'blue']
        size = width, height = w * n * 2, w * n * 2
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Мишень')
        pygame.display.flip()
        for i in range(n):
            pygame.draw.circle(screen, colors[i % 3], (width // 2, height // 2), w * i + w, w)
            pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass

    except Exception:
        print('Неправильный формат ввода')
pygame.quit()