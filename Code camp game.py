import pygame
pygame.init

# World Vars
pygame.font.init()
run = True
screenD = [1000, 800]
screen = pygame.display.set_mode((screenD))
friction = 0.08
fonts = pygame.font.Font(None, 50)


# Squares

squares = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
class BackroundSquare():
    def __init__(self,location):
        self.image = []
        self.image.append(pygame.image.load('images/black_backround.png').convert_alpha())
        self.image.append(pygame.image.load('images/purple_galixy.png').convert_alpha())
        self.image.append(pygame.image.load('images/green_galixy.png').convert_alpha())
        self.rect = (location[1] * 50, location[0] * 50, 50, 50)
        self.imageType = 0
    def draw(self):
        screen.blit(self.image[self.imageType],self.rect)

def displaySquares(squares):
    for y,row in  enumerate(squares):
        for x, col in  enumerate(row):
            if col == 1:
                pygame.draw.rect(screen, (200, 100, 100), (50 * x, 50*y, 45, 45))
            elif col == 2:
                pygame.draw.rect(screen, (100, 100, 200), (50 * x, 50*y, 45, 45))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (50 * x, 50*y, 45, 45))
        

    # pygame.draw.rect(screen, (0, 0, 0), (50, 50, 50, 50))

# Player Vars
class player(pygame.sprite.Sprite):
    def __init__(self,location,playerNumber,images):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        self.playerMomentum = [0, 0]
        self.playerLocation = location
        self.playerNumber = playerNumber
        self.image.append(pygame.image.load(images[0]).convert_alpha())
        self.image.append(pygame.image.load(images[1]).convert_alpha())
        self.rect = self.image[0].get_rect()
        self.rect.left,self.rect.top = location
        self.anamationFrame = 0
    def playerMovment(self):
        keys = pygame.key.get_pressed()

        if self.playerNumber == 1:
            if keys[pygame.K_w]:
                self.playerMomentum[1] -= 0.41
            if keys[pygame.K_s]:
                self.playerMomentum[1] += 0.41
            if keys[pygame.K_a]:
                self.playerMomentum[0] -= 0.41
            if keys[pygame.K_d]:
                self.playerMomentum[0] += 0.41
        elif self.playerNumber == 2:
            if keys[pygame.K_UP]:
                self.playerMomentum[1] -= 0.41
            if keys[pygame.K_DOWN]:
                self.playerMomentum[1] += 0.41
            if keys[pygame.K_LEFT]:
                self.playerMomentum[0] -= 0.41
            if keys[pygame.K_RIGHT]:
                self.playerMomentum[0] += 0.41

        if self.playerMomentum[1] < 0:
            self.playerMomentum[1] += friction
        if self.playerMomentum[1] > 0:
            self.playerMomentum[1] -= friction
        if self.playerMomentum[0] < 0:
            self.playerMomentum[0] += friction
        if self.playerMomentum[0] > 0:
            self.playerMomentum[0] -= friction
        if abs(self.playerMomentum[0]) < 0.1:
            self.playerMomentum[0] = 0
        if abs(self.playerMomentum[1]) < 0.1:
            self.playerMomentum[1] = 0
        if self.playerLocation[0] < 0:
            self.playerLocation[0] = 1
            self.playerMomentum[0] *= -0.7
        if self.playerLocation[1] < 0:
            self.playerLocation[1] = 1
            self.playerMomentum[1] *= -0.7
        if self.playerLocation[0] > screenD[0] - 40:
            self.playerLocation[0] = screenD[0] - 40
            self.playerMomentum[0] *= -0.7
        if self.playerLocation[1] > screenD[1] - 40:
            self.playerLocation[1] = screenD[1] - 40
            self.playerMomentum[1] *= -0.7

        self.playerLocation[0] += self.playerMomentum[0]
        self.playerLocation[1] += self.playerMomentum[1]
        self.rect.left,self.rect.top = self.playerLocation
    def Draw(self, screen):
        if self.anamationFrame > 60:
            self.anamationFrame = 0
        self.anamationFrame += 1
        cerentFrame = 0
        if self.anamationFrame > 30:
            cerentFrame = 1
        screen.blit(self.image[cerentFrame],self.rect)    
    def score(self):
        points = 0
        for row in squares:
            for square in row:
                if square == self.playerNumber:
                    points += 1
        return points
                



clock = pygame.time.Clock()
playerLocation = [500, 500]
# Player Updates
player1 = player([500, 500], 1, ['images/purple_galixy_cat_left.png', 'images/purple_galixy_cat_right.png'])
player2 = player([500, 500], 2, ['images/green_galixy_cat_right.png', 'images/green_galixy_cat_left.png'])
test = BackroundSquare([3, 4])
def paint(player):
    x = int((player.playerLocation[0] + 15)/50)
    y = int((player.playerLocation[1] + 15)/50)
    if x > screenD[0] - 40:
        x = screenD[0] - 40
    if y > screenD[1] - 40:
        y = screenD[1] - 40
    squares[y][x] = player.playerNumber


while run:
    
    # Frame Rate Stuff
    clock.tick(60)

    # Saving inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()


    player1.playerMovment()
    player2.playerMovment()

    paint(player1)
    paint(player2)
    player1score = player1.score()
    player2score = player2.score()
    text1 = fonts.render(str(player1score), True, (255, 255, 255), None)
    text2 = fonts.render(str(player2score), True, (255, 255, 255), None)
    # Display 
    screen.fill((100, 100, 100))
    displaySquares(squares)
    player1.Draw(screen)
    player2.Draw(screen)
    screen.blit(text1, (20, 10))
    screen.blit(text2, (screenD[0] - 100 ,10))
    test.draw()
    pygame.display.flip()