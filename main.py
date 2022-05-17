import pygame

if __name__ == '__main__':
    x, y = str(input()).split()
    if '.' not in x or '.' not in y:
        try:
            x, y = int(x), int(y)
            pygame.init()
            size = x, y
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption('Крест')
            pygame.display.flip()
            while pygame.event.wait().type != pygame.QUIT:
                pygame.draw.line(screen, 'white', (0, 0), (x, y), width=6)
                pygame.draw.line(screen, 'white', (x, 0), (0, y), width=6)
                pygame.display.flip()
        except Exception:
            print('Неправильный формат ввода')
    pygame.quit()
