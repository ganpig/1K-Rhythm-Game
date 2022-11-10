import sys
import pygame
#import easygui
#dir = easygui.diropenbox('请选择谱面文件夹')
dir=sys._MEIPASS
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('音游')
pygame.mixer.music.load(dir+'/music.mp3')
name, bpm = open(dir+'/info.txt').read().splitlines()
beat = 60000/int(bpm)
score = 0
combo = 0
exec(open(dir+'/notes.txt').read())
notes=[[i,True] for i in notes]
texiao = []
font = pygame.font.SysFont('Microsoft Yahei', 50)
render = font.render(name, True, (255, 255, 255))
pygame.mixer.music.play()
while True:
    now_beat = pygame.mixer.music.get_pos()/beat
    render2 = font.render(str(round(score)).zfill(7), True, (255, 255, 255))
    render3 = font.render(f'Combo:{combo}', True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(render, (10, 500))
    screen.blit(render2, (10, 10))
    screen.blit(render3, (10, 60))
    pygame.draw.circle(screen, (255, 255, 255), (150, 300), 50, 10)
    while texiao and texiao[0][0] < now_beat-1:
        texiao.pop(0)
    for i in texiao:
        pygame.draw.circle(screen, i[1], (150, 300), 50+(now_beat-i[0])*50, 10)
    for i, j in notes:
        if j:
            pygame.draw.circle(screen, (0, 255, 255),
                               (150+(i-now_beat)*200, 300), 30)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            for i, (j, k) in enumerate(notes):
                if -0.4 <= j-now_beat <= 0.6 and k:
                    notes[i][1] = False
                    if abs(j-now_beat) <= 0.2:
                        score += 1000000/len(notes)
                        texiao.append((j, (255, 255, 0)))
                        combo += 1
                    elif abs(j-now_beat) <= 0.4:
                        score += 500000/len(notes)
                        texiao.append((j, (0, 100, 255)))
                        combo += 1
                    else:
                        texiao.append((j, (255, 0, 0)))
                        combo = 0
                    for m in range(i):
                        if notes[m][1]:
                            combo = 0
                    break
