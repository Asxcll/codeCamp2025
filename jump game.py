import pygame
import math
pygame.init()
running = True
playerPosition = [0.0, 600.0]
playerSize = [10, 10]
playerDisplay = (*playerPosition, *playerSize)
screenSize = pygame.display.get_desktop_sizes()
falling = True
screenX, screenY = screenSize[0]
screenY -= 60
screenSize = screenX, screenY
screen = pygame.display.set_mode(screenSize)
playerMomentum = [0, 0]
clock = pygame.time.Clock()
groundY = screenY - 100
platforms = [
    [0, screenX, 700, screenY, (155, 155, 0)],
    [500, 800, 500, 700, (100, 255, 255)],
    [0, 800, 600, 700, (100, 100, 100)]
]
font = pygame.font.SysFont('Impact', 50)
jumps = 2
enemy = [
    [0.0, 0.0, 0, 0, True]
]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and jumps > 0:
                playerPosition[1] -= 1
                playerMomentum[1] = -3  # jump strength
                jumps -= 1

    
    dt = clock.tick(60) / 1000

    keys = pygame.key.get_pressed()
    screenX, screenY = screenSize
    enemy[0][4] = True
    falling = True
    player_bottom = playerPosition[1] + playerSize[1]

    player_left = playerPosition[0]
    player_right = playerPosition[0] + playerSize[0]
    player_bottom = playerPosition[1] + playerSize[1]
    enemy_left = enemy[0][0]
    enemy_right = enemy[0][0] + 20
    enemy_bottom = enemy[0][1] + 20
    for plat in platforms:
        plat_left = plat[0]
        plat_right = plat[1]
        plat_top = plat[2]
        plat_bottom = plat[3]
 
        if player_right > plat_left and player_left < plat_right:
            if player_bottom >= plat_top and player_bottom <= plat_top + 10:
                falling = False
                playerPosition[1] = plat_top - playerSize[1]
                playerMomentum[1] = 0

        if enemy_right > plat_left and enemy_left < plat_right:
            if enemy_bottom >= plat_top and enemy_bottom <= plat_top + 10:  
                falling = False
                enemy[0][1] = plat_top - 20
                enemy[0][2] = 0
    
    
    move = pygame.Vector2(0, 0)
    
    if keys[pygame.K_LEFT]:
        if falling == False:
            playerMomentum[0] -= 0.5
        else:
            playerMomentum[0] -= 0.2
    if keys[pygame.K_RIGHT]:
        if falling == False:
            playerMomentum[0] += 0.5
        else:
            playerMomentum[0] += 0.2
    if keys[pygame.K_UP]:
            playerMomentum[1] -= 0.03
    if keys[pygame.K_r]:
        playerPosition = [0.0, 600.0]
        playerMomentum = [0, 0]
    if falling:
            playerMomentum[1] += 0.1
    if playerMomentum[0] > 0:
        if falling == False:
            playerMomentum[0] -= 0.2
    if playerMomentum[0] < 0:
        if falling == False:
            playerMomentum[0] += 0.2
    if abs(playerMomentum[0]) < 0.2:
        playerMomentum[0] = 0
    if not falling:
        if abs(playerMomentum[0]) > 12:
            playerMomentum[0] = 0
    if not falling:
        jumps = 2
    if enemy[0][4] == True:
        enemy[0][3] += 0.1
    
    playerPosition[0] += playerMomentum[0]
    playerPosition[1] += playerMomentum[1]
    enemy[0][0] += enemy[0][0]
    enemy[0][1] += enemy[0][1]
    playerDisplay = (*playerPosition, *playerSize)
    enemyDisplay = (enemy[0][0], enemy[0][1], 20, 20)
    screen.fill((30, 30, 55))
    textSurfice = font.render(str(jumps), False, (255, 255, 255))
    for i in enemy:
        pygame.draw.rect(screen, (255, 255, 255), enemyDisplay, border_radius=2)
    for i in platforms:
        pygame.draw.rect(screen, i[4], (i[0], i[2], (i[1] - i[0]), (i[3] - i[2])))
    pygame.draw.rect(screen, (0, 255, 0), playerDisplay, border_radius=2)
    screen.blit(textSurfice, (50, 50))
    pygame.display.flip()

