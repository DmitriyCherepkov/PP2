import pygame
from pygame import mixer
import datetime

pygame.init()
mixer.init()
mixer.music.load('tictac.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()
FPS = 50

def load_and_scale(image_path, size):
    return pygame.transform.scale(pygame.image.load(image_path), size)

myClock = load_and_scale('image.png', (600, 600))
hour_arrow = load_and_scale('hour.png', (23, 166))
minute_arrow = load_and_scale('minute.png', (20, 233))
second_arrow = load_and_scale('second.png', (16, 266))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    my_time = datetime.datetime.now()
    angleHOUR = my_time.hour % 12 * -30
    angleMINUTE = my_time.minute * -6
    angleSECOND = my_time.second * -6

    screen.fill((255, 255, 255))
    screen.blit(myClock, (100, 100))
    
    for arrow, angle in zip([hour_arrow, minute_arrow, second_arrow], [angleHOUR, angleMINUTE, angleSECOND]):
        rotated_arrow = pygame.transform.rotate(arrow, angle)
        screen.blit(rotated_arrow, (399 - rotated_arrow.get_width() // 2, 400 - rotated_arrow.get_height() // 2))
    
    pygame.draw.circle(screen, (0, 0, 0), (400, 400), 22)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()