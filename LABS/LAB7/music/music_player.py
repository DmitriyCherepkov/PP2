import pygame
from pygame import mixer

pygame.init()
mixer.init()
pygame.display.set_caption("Dima's player :)")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
FPS = 50

musics = ['blindinglights.mp3', 'giant.mp3', 'humility.mp3', 'icantfeelmyface.mp3', 'moveslikejagger.mp3']
plays = ['blindinglights_play.png', 'giant_play.png', 'humility_play.png', 'cantfeelmyface_play.png', 'moveslikejagger_play.png']
pauses = ['blindinglights_pause.png', 'giant_pause.png', 'humility_pause.png', 'cantfeelmyface_pause.png', 'moveslikejagger_pause.png']

n = 0
paused = False

def start(track_index):
    mixer.music.load(musics[track_index])
    mixer.music.set_volume(0.2)
    mixer.music.play()
    screen.blit(pygame.image.load(plays[track_index]), (0, 0))

start(n)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                if paused:
                    mixer.music.pause()
                    screen.blit(pygame.image.load(pauses[n]), (0, 0))
                else:
                    mixer.music.unpause()
                    screen.blit(pygame.image.load(plays[n]), (0, 0))
            elif event.key == pygame.K_RIGHT:
                n = (n + 1) % len(musics)
                start(n)
            elif event.key == pygame.K_LEFT:
                n = (n - 1) % len(musics)
                start(n)
    
    pygame.display.flip()
    clock.tick(FPS)
