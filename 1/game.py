from pygame import*
font.init()

window = display.set_mode((1200, 1200))
display.set_caption('Ping-Pong')
back = transform.scale(image.load('court2.jpg'),(1200, 1200))

font = font.SysFont('Arial', 70)
lose1 = font.render('Player 1 lost', True, (180,0,0))
lose = font.render('Player 2 lost', True, (180,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100,100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <1200:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <1200:
            self.rect.y += self.speed
        
speed_x = 3
speed_y = 3

player1 = Player('rocket.png', 5, 420,20)
player2 = Player('rocket.png', 1100,0,20)
ball = GameSprite('ball.png', 600,600,100)

game = True
finish = False

while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(back,(0,0))
        if ball .rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
        if ball.rect.x > 1200:
            finish = True
            window.blit(lose, (200,200))    
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        player1.update()
        player1.reset()
        player2.update2()
        player2.reset()
    if ball.rect.y > 1200 -50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    display.update()
    time.delay(20)