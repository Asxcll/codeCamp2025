import pygame
import random
pygame.init()

# --- Setup ---
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Epic Game")
LootNumber = 0
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0 ,0 ,255)
SafeZone = 300
font = pygame.font.Font(None, 36)
# Player

x, y = 150.0, 150.0  
speed = 400          
size = 50
Player = (int(x), int(y), size, size)
ChaserSpeed = 250
Cx, Cy = (x * 2, y * 2)
# Loot
Lx = random.randint(25, WIDTH - 25)
Ly = random.randint(25, HEIGHT - 25)
Lsize = 50
Loot = (Lx, Ly, Lsize, Lsize)
# Enemy
Ex = random.randint(25, WIDTH - 25)
Ey = random.randint(25, HEIGHT - 25)
while ((Ex - x)**2 + (Ey - y)**2) ** 0.5 < SafeZone:
    Ex = random.randint(25, WIDTH - 25)
    Ey = random.randint(25, HEIGHT - 25)
Esize = 50
Enemy = (Ex, Ey, Esize, Esize)

clock = pygame.time.Clock()


running = True
while running:
    Player = pygame.Rect(int(x), int(y), size, size)
    Loot = pygame.Rect(Lx, Ly, Lsize, Lsize)
    Chaser = pygame.Rect(Cx, Cy, Lsize, Lsize)
    Enemy = pygame.Rect(Ex, Ey, Esize, Esize)
    textSurfice = font.render(str(LootNumber), True, (0, 0, 0))

 
    dt = clock.tick(120) / 1000  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    move_x = 0
    move_y = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        move_x -= 1
    if keys[pygame.K_d]:
        move_x += 1
    if keys[pygame.K_s]:
        move_y += 1
    if keys[pygame.K_w]:
        move_y -= 1

    if move_x != 0 and move_y != 0:
        move_x *= 0.7071
        move_y *= 0.7071
    
    x += move_x * speed * dt
    y += move_y * speed * dt

    move_Cx = 0
    move_Cy = 0

    if keys[pygame.K_LEFT]:
        move_Cx -= 1
    if keys[pygame.K_RIGHT]:
        move_Cx += 1
    if keys[pygame.K_DOWN]:
        move_Cy += 1
    if keys[pygame.K_UP]:
        move_Cy -= 1
    
    if move_Cx != 0 and move_Cy != 0:
        move_Cx *= 0.7071
        move_Cy *= 0.7071

    Cx += move_Cx * ChaserSpeed * dt
    Cy += move_Cy * ChaserSpeed * dt
    if Player.colliderect(Loot):
        LootNumber += 1
        Lx = random.randint(25, WIDTH - 25)
        Ly = random.randint(25, HEIGHT - 25)
        Ex = random.randint(25, WIDTH - 25)
        Ey = random.randint(25, HEIGHT - 25)
        while ((Ex - x)**2 + (Ey - y)**2) ** 0.5 < SafeZone:
            Ex = random.randint(25, WIDTH - 25)
            Ey = random.randint(25, HEIGHT - 25)
        
    if Player.colliderect(Enemy):
        running = False
    if Player.colliderect(Chaser):
        running = False

    if x > Ex:
        Ex += (((Ex - x)**2 + (Ey - y)**2) ** 0.5 / 80)
    if x < Ex:
        Ex -= (((Ex - x)**2 + (Ey - y)**2) ** 0.5 / 80)
    if y > Ey:
        Ey += (((Ex - x)**2 + (Ey - y)**2) ** 0.5 / 80)
    if y < Ey:
        Ey -= (((Ex - x)**2 + (Ey - y)**2) ** 0.5 / 80)
    ChaserDistanceFromLoot = ((Cx - Lx)**2 + (Cy - Ly)**2) ** 0.5
    if ChaserDistanceFromLoot < 200:
        Cy = 0
        Cx = 0
    # --- Drawing ---
    screen.fill(WHITE)
    screen.blit(textSurfice, (20, 20))
    pygame.draw.rect(screen, BLUE, Player)
    pygame.draw.rect(screen, YELLOW, Loot)
    pygame.draw.rect(screen, RED, Enemy)
    pygame.draw.rect(screen, (0, 0, 0), Chaser)
    pygame.display.flip()