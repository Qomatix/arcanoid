import pygame

TITLE = "Arcanoid"
WIDTH = 800
HEIGHT = 600
FPS = 60
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(TITLE)

class GameObject:
    def __init__(self, filename) -> None:
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(filename)

    def draw(self, scr):
        rect = self.image.get_rect()
        rect.x += self.x
        rect.y += self.y
        scr.blit(self.image, rect)

    def update(self):
        pass
    
    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y
   
    def getX(self):
        return self.x
    
    def getWidth(self):
        return self.image.get_rect().width

paddle = GameObject("images/paddleblue.png")
paddle.setX(300)
paddle.setY(450)

ball = GameObject("images/ballblue.png")
ball.setX(200)
ball.setY(300)


barimages = ["element_blue_rectangle_glossy.png","element_green_rectangle_glossy.png","element_red_rectangle_glossy.png"]
bars = []
y = 0
for file in barimages:
    x = 0
    y += 50
    for i in range(0,8):
        imagename = "images/" + file
        obj = GameObject(filename = imagename)
        x += 80
        obj.setX(x)
        obj.setY(y)
        bars.append(obj)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_LEFT:
    #             paddle.setX(paddle.getX() - 10)
    #         if event.key == pygame.K_RIGHT:
    #              paddle.setX(paddle.getX() + 10)
        
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = paddle.getX() - 10
        if x < 0:
            x = 0
        paddle.setX(x)


    if keys[pygame.K_RIGHT]:
        x = paddle.getX() + 10 
        if x > WIDTH - paddle.getWidth():
            x = WIDTH - paddle.getWidth()
        paddle.setX(x)

    screen.fill("black")
    for b in bars:
        b.draw(screen)
    ball.draw(screen)
    paddle.draw(screen)
    pygame.display.flip()

pygame.quit()