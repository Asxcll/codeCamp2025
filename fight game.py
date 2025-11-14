import pygame

running = True

# Player Vars
playerPosition = [0, 0]
playerMomentum = [0, 0]
weight = 9
speed = (11 - weight) / 10
if speed < 0:
     speed = 0

# World Vars
screenD = [1000, 780]
screen = pygame.display.set_mode((screenD))
pygame.display.set_caption('Game')
friction = 0.07
damage = playerMomentum[0] + playerMomentum[1]

# Main Game Loop
while running:
    # Clock
    clock = pygame.time.Clock()
    clock.tick(60)

    # Var Checkups
    speed = (11 - weight) / 10
    if speed < 0:
        speed = 0

    # Handling inputs
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if keys[pygame.K_a]:
                playerMomentum = [(playerMomentum[0] * -1), (playerMomentum[1] * -1)]
    
    # Wall bounce
    if playerPosition[0] <= 0:
        playerPosition[0] = 1
        playerMomentum[0] *= -1
    if playerPosition[0] >= screenD[0] - 10:
        playerPosition[0] = screenD[0] - 11
        playerMomentum[0] *= -1
    if playerPosition[1] <= 0:
        playerPosition[1] = 1
        playerMomentum[1] *= -1
    if playerPosition[1] >= screenD[1] - 10:
        playerPosition[1] = screenD[1] - 11
        playerMomentum[1] *= -1

    # player Inputs
    if keys[pygame.K_UP]:
        playerMomentum[1] -= speed
    if keys[pygame.K_DOWN]:
        playerMomentum[1] += speed
    if keys[pygame.K_LEFT]:
        playerMomentum[0] -= speed
    if keys[pygame.K_RIGHT]:
        playerMomentum[0] += speed
    if keys[pygame.K_SPACE]:
        playerMomentum[0] = 0
        playerMomentum[1] = 0
    if keys[pygame.K_r]:
        playerPosition = [0, 0]
        playerMomentum = [0, 0]
    
    # Momentum Aplication
    playerPosition[0] += playerMomentum[0]
    playerPosition[1] += playerMomentum[1]
    
    # Drawing
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (playerPosition[0], playerPosition[1], 10, 10), border_radius=5)
    
    # Updating
    pygame.display.flip()