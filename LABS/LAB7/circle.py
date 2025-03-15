import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
FPS = 50
posX, posY = 400, 400

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and posY > 20:
                posY -= 20
            elif event.key == pygame.K_DOWN and posY < 750:
                posY += 20   
            elif event.key == pygame.K_LEFT and posX > 20:
                posX -= 20
            elif event.key == pygame.K_RIGHT and posX < 765:
                posX += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (posX, posY), 25)
    pygame.display.flip()
    clock.tick(FPS)
