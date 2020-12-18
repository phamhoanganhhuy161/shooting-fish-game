import pygame, sys, random
pygame.init()
clock=pygame.time.Clock()

#SCREEN
screen_height=500
screen_width=500
screen=pygame.display.set_mode((screen_width,screen_height))
background=pygame.image.load('SEA background.png')
background=pygame.transform.scale(background,(screen_width,screen_height))
pygame.mouse.set_visible(False)
#SCORE
score=0
BLACK=(0,0,0)
game_font=pygame.font.Font('freesansbold.ttf',32)
#CROSSHAIR
class crosshair(pygame.sprite.Sprite):
    def __init__(self,picture_path):
        super().__init__()
        self.image=pygame.image.load(picture_path)
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()
        self.gunshot=pygame.mixer.Sound('Futuristic Sniper Rifle Single Shot.wav')
    def shoot(self):
        global fish_amount1,fish_amount2,fish_amount3,score
        self.gunshot.play()
        if pygame.sprite.spritecollide(crosshair,target_group1,True):
            fish_amount1-=1
            score+=1
        if pygame.sprite.spritecollide(crosshair,target_group2,True):
            fish_amount2-=1
            score+=1
        if pygame.sprite.spritecollide(crosshair,target_group3,True):
            fish_amount3-=1
            score+=1
    def update(self):
        self.rect.center=pygame.mouse.get_pos()

crosshair=crosshair('crosshair paternus1.png')
crosshair_group=pygame.sprite.Group()
crosshair_group.add(crosshair)
#TARGET

class Target1(pygame.sprite.Sprite):
    def __init__(self,picture_path,pos_x,pos_y):
        super().__init__()
        self.image=pygame.image.load(picture_path)
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()
        self.rect.center= [pos_x,pos_y]
    def update(self):
        self.rect.x+=1
        if self.rect.x>=screen_width-20: 
            self.rect.x=-20
    
target_group1=pygame.sprite.Group()
target_group3=pygame.sprite.Group()
fish_amount1=random.randrange(2,5)
fish_amount3=random.randrange(2,5)
for fish_predator1 in range(fish_amount1):
    new_target1=Target1("fish Predator 1.png",random.randrange(0,screen_width),random.randrange(0,screen_height))
    target_group1.add(new_target1)
for fish_predator2 in range(fish_amount3):
    new_target3=Target1("Fish Predator Sick.png",random.randrange(0,screen_width),random.randrange(0,screen_height))
    target_group3.add(new_target3)        
    
def update1():
    global fish_amount1
    if fish_amount1==0:
        fish_amount1=random.randrange(3,6)
        for fish_predator1 in range(fish_amount1):
            new_target1=Target1("fish Predator 1.png",random.randrange(0,screen_width),random.randrange(0,screen_height))
            target_group1.add(new_target1)
def update3():
    global fish_amount3
    if fish_amount3==0:
        fish_amount3=random.randrange(3,6)
        for fish_predator2 in range(fish_amount3):
            new_target3=Target1("Fish Predator Sick.png",random.randrange(0,screen_width),random.randrange(0,screen_height))
            target_group3.add(new_target3)

class Target2(pygame.sprite.Sprite):
    def __init__(self,picture_path,pos_x,pos_y):
        super().__init__()
        self.image=pygame.image.load(picture_path)
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()
        self.rect.center= [pos_x,pos_y]
    def update(self):
        self.rect.y-=1
        self.rect.x+=1
        if self.rect.y>=screen_height: 
            self.rect.y=random.randrange(0,screen_height)
            self.rect.x=random.randrange(0,screen_width)
        if self.rect.x>=screen_width-20: 
            self.rect.x=random.randrange(0,screen_width)
            self.rect.y=random.randrange(0,screen_height)
target_group2=pygame.sprite.Group()
fish_amount2=random.randrange(5,8)
for jellyfish in range(fish_amount2):
    new_target2=Target2("Jellyfish5.png",random.randrange(0,screen_width),random.randrange(0,screen_height))
    target_group2.add(new_target2)

def update2():
    global fish_amount2
    if fish_amount2==0:
        fish_amount2=random.randrange(1,3)
        for jellyfish in range(fish_amount2):
            new_target2=Target2("Jellyfish5.png",random.randrange(0,screen_width),random.randrange(0,screen_height))
            target_group2.add(new_target2)

    

#LOOP
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
    player_text=game_font.render(f"{score}",False,BLACK)
    screen.blit(player_text,(screen_width/2,100))
        
    pygame.display.flip()
    screen.blit(background,(0,0))
    target_group1.draw(screen)
    target_group1.update()
    target_group3.draw(screen)
    target_group3.update()
    target_group2.draw(screen)
    target_group2.update()
    crosshair_group.draw(screen)
    crosshair_group.update()
    update1()
    update2()
    update3()
    clock.tick(60)
