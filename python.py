import pygame
import random


pygame.init()

# Window creation
WIDTH, HEIGHT = 1366, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")
# Colors
GRAY = (50,50,50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#fps
FPS = 60
#ball maxspeed
MAX_SPEED = 30


balls = []

# Class ball creation
class Ball:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.x_speed = random.uniform(-self.speed, self.speed)
        self.y_speed = random.uniform(-self.speed, self.speed)
    
    def update(self):
        # position refreshing
        self.x += self.x_speed
        self.y += self.y_speed
        
        # ball collision with window borders
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.x_speed *= -1
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.y_speed *= -1
        
        # balls collision
        for ball in balls:
            if ball != self:
                distance = ((self.x - ball.x) ** 2 + (self.y - ball.y) ** 2) ** 0.5
                if distance <= self.radius + ball.radius:
                    # bounce
                    self.x_speed *= -1
                    self.y_speed *= -1
                    break
        
        self.y_speed += 0.1 

    def draw(self):
        # ball draw
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# main cycle
running = True
clock = pygame.time.Clock()

while running:
    # event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # new ball by mouse clicking
            x, y = event.pos
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            speed = random.uniform(1, MAX_SPEED)
            ball = Ball(x, y, random.randint(10,50), color, speed)
            balls.append(ball)
    
    # background drawing
    screen.fill(GRAY)
    
    # Ball drawing
    for ball in balls:
        ball.update()
        ball.draw()
    
    #Changing tickrate by pressing ARROWUP\ARROWDOWN
    keypressed = pygame.key.get_pressed()

    if keypressed[pygame.K_UP]:
        FPS+=1
        keypressed = None
    elif keypressed[pygame.K_DOWN]:
        FPS-=1
        keypressed = None

    pygame.font.init()

# Font object creation
    font = pygame.font.Font(None, 36)

# Text object creation
    text = font.render("Ticks: " + str(FPS), True, (0, 255, 0))

    screen.blit(text, (1,1))

    # FPSLIMOT
    clock.tick(FPS)
    # DISPLAY UPDATE
    pygame.display.flip()
    
pygame.quit()
