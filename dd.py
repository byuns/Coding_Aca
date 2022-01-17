import pygame
a = 5
x = 1
while x:
    music_file = str(a)+".mp3"   # mp3 or mid file
    a=a+1
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
   
    clock = pygame.time.Clock()

    while pygame.mixer.music.get_busy():
        t = input()
        if t == "1":
            pass
        if t == "2":
            a=a-2
        if t == "3":
            x = 0
        break
        clock.tick(30)
    pygame.mixer.quit()






#1 다음노래
#2 이전노래
#3 종료
