import time
import pygame
# Initialise modules
pygame.init()
# Creating Screen
width = 960
height = 304
screen = pygame.display.set_mode((width,height))#(512,288)
# Set Caption
pygame.display.set_caption("Dungeon Hunt")
# # icon
# icon = pygame.image.load("school.png")
# pygame.display.set_icon(icon)
# Set fonts
font = pygame.font.Font('ThaleahFat.ttf',25)
onsurface = font.render("Welcome to Dungeon Hunt",0,(255,15,15),None)
onsurface1 = font.render("The game is still in development",0,(15,255,15),None)
onsurface2 = font.render("Press Any Key to Start",0,(15,15,255),None)
# Setting score
score = font.render("000",0,(0,0,0),None)
# game clock
clock = pygame.time.Clock()

class player():
    right = [pygame.image.load('player/walk1.png').convert_alpha(),pygame.image.load('player/walk2.png').convert_alpha(),pygame.image.load('player/walk3.png').convert_alpha(),
                pygame.image.load('player/walk4.png').convert_alpha(),pygame.image.load('player/walk5.png').convert_alpha(),pygame.image.load('player/walk6.png').convert_alpha()
            ,pygame.image.load('player/walk7.png').convert_alpha(),pygame.image.load('player/walk8.png').convert_alpha(),pygame.image.load('player/walk9.png').convert_alpha()
            ,pygame.image.load('player/walk10.png').convert_alpha(),pygame.image.load('player/walk11.png').convert_alpha(),pygame.image.load('player/walk12.png').convert_alpha()

            ]
    # idle = pygame.image.load('player/walk1.png').convert_alpha()
    left = [pygame.transform.flip(right[0],True,False),pygame.transform.flip(right[1],True,False),pygame.transform.flip(right[2],True,False),pygame.transform.flip(right[3],True,False)
            ,pygame.transform.flip(right[4],True,False),pygame.transform.flip(right[5],True,False),pygame.transform.flip(right[6],True,False),pygame.transform.flip(right[7],True,False)
             ,pygame.transform.flip(right[8],True,False),pygame.transform.flip(right[9],True,False),pygame.transform.flip(right[10],True,False),pygame.transform.flip(right[11],True,False)]

    hit_right = [pygame.image.load('player/hit1.png').convert_alpha(),pygame.image.load('player/hit2.png').convert_alpha(),pygame.image.load('player/hit3.png').convert_alpha(),
                pygame.image.load('player/hit4.png').convert_alpha(),pygame.image.load('player/hit5.png').convert_alpha(),pygame.image.load('player/hit6.png').convert_alpha()]




    hit_left = [pygame.transform.flip(hit_right[0],True,False),pygame.transform.flip(hit_right[1],True,False),pygame.transform.flip(hit_right[2],True,False),pygame.transform.flip(hit_right[3],True,False)
            ,pygame.transform.flip(hit_right[4],True,False),pygame.transform.flip(hit_right[5],True,False)]


    idle = [pygame.image.load('player/idle1.png').convert_alpha(),pygame.image.load('player/idle2.png').convert_alpha(),pygame.image.load('player/idle3.png').convert_alpha(),
                pygame.image.load('player/idle4.png').convert_alpha()]


def redraw():
    screen.fill((0, 0 , 0))
    bg1 = pygame.image.load('bgs/bg1.png').convert_alpha()
    # bg = pygame.image.load('bgs/color.png').convert_alpha()
    # bg_walls = pygame.image.load('bgs/bg.png').convert_alpha()
    # bg_tiles = pygame.image.load('bgs/tiles.png').convert_alpha()
    screen.blit(bg1,(0,0))
    # screen.blit(bg_walls,(0,0))
    # screen.blit(bg_tiles,(0,0))

class movement():

    def __init__(self):
        self.playerX = 20
        self.playerY = 200
        self.width = 35
        self.height = 48
        self.velocity = 4
        self.isJump = False
        self.right = False
        self.left = False
        self.isshooting = False
        self.JumpCount = 10
        self.walkcount = 0
        self.shootcount = 1
        self.standing = True
        self.prevl = False
        self.prevr = False
        self.lhitbox = ()
        self.rhitbox = ()
        self.plhitbox = ()
        self.prhitbox = ()
    def move(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.playerX > 10:
            self.playerX -= self.velocity
            self.left = True
            self.standing = False
            self.right = False
            self.isshooting = False
        elif keys[pygame.K_RIGHT] and self.playerX < width-self.width:
            self.playerX += self.velocity
            self.right = True
            self.left = False
            self.standing = False
            self.isshooting = False
        elif keys[pygame.K_a]:
            self.isshooting = True
        elif keys[pygame.K_s]:
            self.isshooting = True
        else:
            self.isshooting = False
            self.standing = True
            self.right = False
            self.left = False
            self.walkcount = 0

        if self.walkcount >=36:
            self.walkcount = 0

        if self.shootcount >= 18:
            self.shootcount = 0

        #  Hitboxes declared
        self.lhitbox=(self.playerX+10,self.playerY + 18,5, 10)
        self.rhitbox=(self.playerX+self.width+40,self.playerY+18,5,10)
        self.prhitbox = (self.playerX+self.width+10,self.playerY+20,10,10)
        self.plhitbox = (self.playerX+5, self.playerY+20, 10,10 )

        if self.right and not(self.isshooting):
            screen.blit(player.right[self.walkcount//3],(self.playerX,self.playerY))
            # pygame.draw.rect(screen,(255,0,0),self.prhitbox,2)
            self.walkcount +=1
        elif self.left and not(self.isshooting):
            screen.blit(player.left[self.walkcount//3],(self.playerX,self.playerY))
            # pygame.draw.rect(screen, (255, 0, 0), self.plhitbox, 2)
            self.walkcount += 1

        elif self.isshooting:
            if keys[pygame.K_a]:
                screen.blit(player.hit_left[self.shootcount//3],(self.playerX,self.playerY))
                # pygame.draw.rect(screen, (255, 0, 0),self.lhitbox,2)
                self.shootcount += 1
                self.left = False
                self.right = False
                self.standing = False
            elif keys[pygame.K_s]:
                screen.blit(player.hit_right[self.shootcount // 3], (self.playerX, self.playerY))
                # pygame.draw.rect(screen,(255,0,0),self.rhitbox,2)
                self.shootcount += 1
                self.left = False
                self.right = False
                self.standing = False

        else:
            screen.blit(player.idle[0],(self.playerX,self.playerY))
            # if self.right:
            #     screen.blit(player.idle[0],(self.playerX,self.playerY))
            # else:
            #     screen.blit(player.idle[0],(self.playerX,self.playerY))

        # Jump code 20 px margin gap if player is jumping not allowed to move up and down also player goes up fast hangs in air and then
        # falls down
        # jump down accelerates due to gravity
        # EQUATION = (jumpcount ** 2) * 0.5 * neg -> neg is to either increase or decrease the speed of jump
        if not (self.isJump):
            if  keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                self.isJump = True
                self.right = False
                self.left = False
        else:
            if self.JumpCount >= -10:
                neg = 1
                if self.JumpCount < 0:
                    neg = -1
                self.playerY -= (self.JumpCount ** 2) * 0.4 * neg
                self.JumpCount -= 1
            else:
                self.isJump = False
                self.JumpCount = 10





class enemy():

    right =[pygame.image.load('player/ewalk1.png').convert_alpha(),
             pygame.image.load('player/ewalk2.png').convert_alpha(),
             pygame.image.load('player/ewalk3.png').convert_alpha(),
             pygame.image.load('player/ewalk4.png').convert_alpha(),
             pygame.image.load('player/ewalk5.png').convert_alpha(),
             pygame.image.load('player/ewalk6.png').convert_alpha()
        , pygame.image.load('player/ewalk7.png').convert_alpha(), pygame.image.load('player/ewalk8.png').convert_alpha(),
             pygame.image.load('player/ewalk9.png').convert_alpha()
        , pygame.image.load('player/ewalk10.png').convert_alpha(),
             pygame.image.load('player/ewalk11.png').convert_alpha(),
             pygame.image.load('player/ewalk12.png').convert_alpha(),
                pygame.image.load('player/ewalk13.png').convert_alpha()
             ]

    left = [pygame.transform.flip(right[0], True, False), pygame.transform.flip(right[1], True, False),
            pygame.transform.flip(right[2], True, False), pygame.transform.flip(right[3], True, False)
        , pygame.transform.flip(right[4], True, False), pygame.transform.flip(right[5], True, False),
            pygame.transform.flip(right[6], True, False), pygame.transform.flip(right[7], True, False)
        , pygame.transform.flip(right[8], True, False), pygame.transform.flip(right[9], True, False),
            pygame.transform.flip(right[10], True, False), pygame.transform.flip(right[11], True, False), pygame.transform.flip(right[12], True, False)]

    def __init__(self,x,y,end,vel):
        self.x = x
        self.y = y
        self.end = end
        self.path = [self.x, self.end]
        self.height = 37
        self.widht = 20
        self.vel = vel
        self.walkCount = 0
        self.hitbox = ()
        self.hit = 0
    def drawe(self,screen):
        self.move()
        self.hitbox = (self.x,self.y,self.widht,self.height)
        if self.walkCount + 1 >= 39:
            self.walkCount = 0
        if self.vel > 0:
            screen.blit(self.right[self.walkCount//3],(self.x,self.y))
            pygame.draw.rect(screen,(255,0,0),self.hitbox,2)
            self.walkCount += 1
        else:
            screen.blit(self.left[self.walkCount//3],(self.x,self.y))
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
            self.walkCount +=1
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x = self.x + self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x = self.x + self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0



#Object Definations
skeleton = enemy(400,210,600,1)
m = movement()


def hit():
    if m.isshooting:
        if m.lhitbox[0]>skeleton.hitbox[0] and m.lhitbox[0]+m.lhitbox[2]<skeleton.hitbox[0]+skeleton.hitbox[2]:
            print('left hit')
        if m.rhitbox[0]>skeleton.hitbox[0] and m.rhitbox[0]+m.rhitbox[2]<skeleton.hitbox[0]+skeleton.hitbox[2]:
            print('right hit')
    if not(m.isJump):
        if m.plhitbox[0]>skeleton.hitbox[0] and m.plhitbox[0]+m.plhitbox[2]<skeleton.hitbox[0]+skeleton.hitbox[2]:
            print('dead boi')

        if m.prhitbox[0]>skeleton.hitbox[0] and m.prhitbox[0]+m.prhitbox[2]<skeleton.hitbox[0]+skeleton.hitbox[2]:
            print('right dead')

# #Display screen loop
Drunning = True
while Drunning:
     for event in pygame.event.get():
         if event.type== pygame.KEYDOWN:
             Drunning = False

     screen.blit(onsurface,(100,100))
     screen.blit(onsurface1,(100,125))
     screen.blit(onsurface2,(100, 150))
     pygame.display.update()

# Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(36)
    redraw()
    skeleton.drawe(screen)
    m.move()
    hit()
    screen.blit(score,(width-50,height-50))
    pygame.display.update()

