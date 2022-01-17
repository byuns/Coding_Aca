import pygame


music_file = "1.mp3"   # mp3 or mid file
pygame.mixer.init()

pygame.mixer.music.load(music_file)
pygame.mixer.music.play()
clock = pygame.time.Clock()

while pygame.mixer.music.get_busy():
    clock.tick(30)
pygame.mixer.quit()




