import pygame, random, time
pygame.init()
width = 750
height = 750
title = "Flag Game"
white = (255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans',75)
font1 = pygame.font.SysFont('comicsans',40)
best_score = 223
#mushroom not spawning after blue and then skull
class Game:
    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.score = 0
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption(title)
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width,height))
    def CreateFlag(self):
        try:
            self.bpowerups.remove("Time Travel")
        except:
            pass
        try:
            self.bpowerups.remove("Cleared!")
        except:
            pass
        if self.bdeath == True and self.score >= self.bdeathscore:
            if self.shield == False and self.doubleshield == False:
                self.done = True
            else:
                if self.doubleshield == True:
                    self.useddoubleshield = True
                    self.strongshield = False
                self.usedshield = True
                self.poweractive = False
                self.bpowerups.remove("Death at Score: "+str(new_game.bdeathscore))
                self.bdeath = False
        if self.busedshield == True:
            if "Damaged Anti Shield" not in self.bpowerups and "Strong Anti Shield" not in self.bpowerups:
                self.bshield = False
            self.busedshield = False
        if self.buseddoubleshield == True:
            if "Strong Anti Shield" not in self.bpowerups:
                self.bdoubleshield = False
            self.buseddoubleshield = False
        if self.usedshield == True:
            self.usedshield = False
            self.shield = False
        if self.useddoubleshield == True:
            self.doubleshield = False
            self.useddoubleshield = False
        if (self.bspawn == True and self.bmisspower == True) or (self.bspawn == True and self.bgetpower == True):
                self.bspawn = False
                self.bpoweractive = False
                self.bgetpower = False
                self.bmisspower = False
        if (self.spawn == True and self.getpower == True) or (self.spawn == True and self.misspower == True):
            self.delay += 1
            if self.delay >= 5 and self.strongshield == False:
                self.delay = 0
                self.getpower = False
                self.misspower = False
                self.spawn = False
                self.poweractive = False
                self.togglefriction = 1
                self.increasespeed = 0
                if self.miniimage == True:
                    self.player.x_pos -= 7.5
                    self.player.speed = self.playerspeed + self.increasespeed
                    if self.gotblue == True:
                        self.player.x_pos -= 7.5
                self.miniimage = False
                self.player.width = 50
                self.player.height = 50
                self.gapboost = 0
                self.speedratio = 1
                self.slow = False
                self.scoreboost = 0
                self.score = round(self.score)
                self.shield = False
                self.opposite = False
                self.bounceeffect = 1
                self.player.y_pos = 100
                self.gotblue = False
                self.luck = False
        if self.opposite == True:
            self.speedratio = 1
        if self.luck == True:
            self.luckboost = random.randint(15,25)
        self.flaggap = random.randint(200 + self.gapboost + self.luckboost,250 + self.gapboost)
        self.flag1x_pos = random.randint(20,width-20-50-self.flaggap)
        self.flag1 = EnemyCharacter('Flag.png',self.flag1x_pos,self.height+50,50,50)
        self.flag2 = EnemyCharacter('Flag.png',self.flag1x_pos,self.height+50,50,50)
        self.flag2.x_pos += self.flaggap
        if self.luck == True:
            distance = ((new_game.player.x_pos+25) - (new_game.flaggap/2+25+new_game.flag1.x_pos))/self.luckratio 
            if self.flag1.x_pos + distance < 0:
                distance = -self.flag1.x_pos
            elif self.flag2.x_pos + distance > width - self.flag2.width:
                distance = width - self.flag2.width - self.flag2.x_pos
            self.flag1.x_pos += distance
            self.flag2.x_pos += distance
        self.flag1.speed = self.level + self.blevel
        self.flag2.speed = self.level + self.blevel
        if random.randint(1,5 + self.powerchance) == 1 and self.spawn == False and self.bpoweractive == False:
                self.spawn = True
                if random.randint(1,7) == 1:
                    self.gotblue = True
                    self.powerup = PowerUp('BluePowerup.png',random.randint(20,width-20-50),self.height,35,35)
                else:
                    self.powerup = PowerUp('Powerup.png',random.randint(20,width-20-50),self.height,50,50)
        if random.randint(1,4 - self.bpowerchance) == 1 and self.bspawn == False:
            self.bspawn = True
            self.bpowerup = BadPowerup('BadPowerup.png',random.randint(20,width-20-50),self.height,50,50)
            if random.randint(1,3) == 1:
                self.change = True
                self.bpowerup.image = pygame.transform.scale(pygame.image.load("Powerup.png"), (50,50))
    def run_game_loop(self):
        global best_score, new_game
        game_over = False
        self.bpowerups = ["Permanent Effects:"]
        self.powerchance = 0
        self.bpowerchance = 0
        self.playerspeed = 7.5
        self.pause = False
        self.xdirection = 0
        self.slide = 0
        self.player = PlayerCharacter('Player.png',350,100,50,50)
        self.powerup = PowerUp('Powerup.png',350,-50,50,50)
        self.bpowerup = BadPowerup('Powerup.png',350,-50,50,50)
        self.level = 5.0
        self.togglefriction = 1
        self.randomizeflagpos = False
        self.getpower = False
        self.poweractive = False
        self.misspower = False
        self.spawn = False
        self.delay = 0      
        self.gapboost = 0
        self.speedratio = 1
        self.slow = False
        self.miniimage = False
        self.increasespeed = 0
        self.scoreboost = 0
        self.shield = False
        self.usedshield = False
        self.doubleshield = False
        self.useddoubleshield = False
        self.strongshield = False
        self.opposite = False
        self.bounceeffect = 1
        self.gotblue = False
        self.luck = False
        self.luckboost = 0
        self.luckratio = 0
        self.bgetpower = False
        self.bpoweractive = False
        self.bmisspower = False
        self.bspawn = False
        self.change = False
        self.blevel = 0
        self.bshield = False
        self.busedshield = False
        self.bdoubleshield = False
        self.buseddoubleshield = False
        self.bdeath = False
        self.bdeathscore = 0
        self.done = False
        self.dash = False
        self.dashcount = 0
        self.CreateFlag()
        for event in pygame.event.get():
                pass
        while not game_over:
            self.displaylevel = round(self.level * self.speedratio + new_game.blevel,1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause = True
                        self.screen.blit(font.render('Paused', True, white),(285,325))
                        pygame.display.update()
                        while self.pause == True:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_p:
                                        self.pause = False
                                if event.type == pygame.QUIT:
                                    from os import _exit
                                    _exit(0)
                        self.xdirection = 0
                    if event.key == pygame.K_UP and self.xdirection != 0 and self.slide == 0 and self.dashcount < 3:
                        self.dash = True
                        self.dashcount += 1
                        self.player.speed = (self.playerspeed + self.increasespeed) * 1.5
                        text = font.render('Dash!', True, black)
                    if event.key == pygame.K_r:
                        best_score = self.score
                    if event.key == pygame.K_RIGHT:
                        self.player.speed = self.playerspeed + self.increasespeed
                        self.slide = 0
                        self.xdirection = 1
                    elif event.key == pygame.K_LEFT:
                        self.player.speed = self.playerspeed + self.increasespeed
                        self.slide = 0
                        self.xdirection = -1
                elif event.type == pygame.KEYUP:
                    if (event.key == pygame.K_RIGHT and self.xdirection == 1) or (event.key == pygame.K_LEFT and self.xdirection == -1):
                        self.dash = False
                        self.slide = 1
                        if self.miniimage == True:
                            self.xdirection = 0
            if self.slide == 1:
                self.player.speed = round(self.player.speed / (1.1 * self.bounceeffect) * self.togglefriction,3)
            self.screen.blit(self.image,(0,0))
            if self.dash == True:
                self.screen.blit(text,(305,285))
            for i in range(len(self.bpowerups)):
                name = font1.render(self.bpowerups[i], True, white)
                name_rect = name.get_rect()
                name_rect.right = width - 5
                name_rect.bottom = height - 5 - (len(self.bpowerups)-i-1) * name_rect.height
                self.screen.blit(name, name_rect)
            self.screen.blit(font.render('Score: '+str(round(self.score)), True, white),(0,0))
            if self.score > best_score:
                best_score = self.score
            self.screen.blit(font.render('Best: '+str(round(best_score)), True, white),(0,55))
            if self.poweractive == True:
                name = font.render(self.powername, True, white)
                name_rect = name.get_rect()
                name_rect.right = width - 5
                self.screen.blit(name, name_rect)
            self.player.move(self.xdirection)
            self.powerup.move()
            self.flag1.move()
            self.flag2.move()
            self.screen.blit(font.render('Speed:'+str(self.displaylevel), True, white),(0,655))
            self.screen.blit(font1.render('Dashes left: '+str(3 - self.dashcount), True, white),(0,710))
            if self.powerup.y_pos + self.powerup.height <= self.player.y_pos and self.getpower == False and self.spawn == True:
                self.misspower = True
            if self.bpowerup.y_pos <= -self.powerup.height and self.bgetpower == False and self.bspawn == True:
                self.bmisspower = True
            self.bpowerup.move()
            if self.randomizeflagpos == True:
                self.randomizeflagpos = False
                self.score += (1 + self.scoreboost)
                if not self.score % 50:
                    self.dashcount += 1
                self.CreateFlag()
                if self.done == True:
                    game_over = True
                    loseface = GameObject('LosePlayer.png',self.player.x_pos,self.player.y_pos,self.player.width,self.player.height)
                    loseface.draw(self.screen)
                    text = font.render('Game Over!', True, black)
                    self.screen.blit(text,(225,325))
                    pygame.display.update()
                    break
            if self.poweractive == False and self.bpoweractive == False:
                self.powerup.draw(self.screen)
            else:
                self.powerup.y_pos = -self.powerup.height
            if self.bpoweractive == False:
                self.bpowerup.draw(self.screen)
            else:
                self.bpowerup.y_pos = -self.bpowerup.height
            if self.poweractive == True and self.miniimage == True:
                self.player.image = pygame.transform.scale(pygame.image.load('PowerPlayer.png'), (35,35))
                if self.gotblue == True:
                    self.player.image = pygame.transform.scale(pygame.image.load('PowerPlayer.png'), (20,20))
            elif self.poweractive == True:
                self.player.image = pygame.transform.scale(pygame.image.load('PowerPlayer.png'), (50,50))
            elif self.bpoweractive == True:
                self.player.image = pygame.transform.scale(pygame.image.load('BadPlayer.png'), (50,50))
            else:
                self.player.image = pygame.transform.scale(pygame.image.load('Player.png'), (50,50))
            self.player.draw(self.screen)
            self.flag1.draw(self.screen)
            self.flag2.draw(self.screen)
            pygame.display.update()
            clock.tick(60)
            if self.player.detect_collision(self.flag1,True,False,self.flag2) or self.player.detect_collision(self.flag2,False,True,self.flag1):          
                if self.shield == False and self.doubleshield == False:
                    game_over = True
                    loseface = GameObject('LosePlayer.png',self.player.x_pos,self.player.y_pos,self.player.width,self.player.height)
                    loseface.draw(self.screen)
                    text = font.render('Game Over!', True, black)
                    self.screen.blit(text,(225,325))
                    pygame.display.update()
                    break
                elif self.doubleshield == True:
                    self.useddoubleshield = True
                    self.powername = 'Damaged Shield'
                else:
                    self.strongshield = False
                    self.usedshield = True
                    self.poweractive = False
            if self.spawn == True and self.poweractive == False: 
                if self.player.detect_collision(self.powerup,True,True,None):
                    if self.bshield == False and self.bdoubleshield == False:
                        if len(self.bpowerups) > 1:
                            self.clearchance = 5
                            if self.gotblue == True:
                                self.clearchance = 2
                            if random.randint(1,self.clearchance) == 1:
                                self.powerchance = 0
                                self.blevel = 0
                                self.playerspeed = 7.5
                                self.bshield = False
                                self.powerchance = 0
                                self.bpowerchance = 0
                                self.bdeath = False
                                self.bpowerups = ["Permanent Effects:", "Cleared!"]
                        if self.player.y_pos > self.flag1.y_pos + self.flag1.height:
                            self.delay -= 1
                        self.getpower = True
                        self.poweractive = True
                        self.player.image = pygame.transform.scale(pygame.image.load('PowerPlayer.png'), (50,50))
                        random.choice([self.powerup.mini,self.powerup.increasegap,self.powerup.decreaseflagspeed,self.powerup.scoreboost,self.powerup.shield,self.powerup.opposite,self.powerup.luck])()
                    elif self.bdoubleshield == True:
                        if self.buseddoubleshield == False:
                            self.bpowerups[self.bpowerups.index("Strong Anti Shield")] = "Damaged Anti Shield"
                        self.buseddoubleshield = True
                    else:
                        if self.busedshield == False:
                            self.bpowerups.remove("Damaged Anti Shield")
                        self.busedshield = True
                    self.powerup.y_pos = -self.height
            if self.bspawn == True and self.bpoweractive == False:
                if self.player.detect_collision(self.bpowerup,True,True,None):
                    self.bgetpower = True
                    self.bpoweractive = True
                    self.getpower = False
                    self.misspower = True
                    self.spawn = True
                    self.poweractive = False
                    self.togglefriction = 1
                    self.increasespeed = 0
                    if self.miniimage == True:
                        self.player.speed = self.playerspeed + self.increasespeed
                        self.player.x_pos -= 7.5
                        if self.gotblue == True:
                            self.player.x_pos -= 7.5
                    self.miniimage = False
                    self.player.width = 50
                    self.player.height = 50
                    self.gapboost = 0
                    self.speedratio = 1
                    self.slow = False
                    self.scoreboost = 0
                    self.score = round(self.score)
                    self.shield = False
                    self.opposite = False
                    self.bounceeffect = 1
                    self.player.y_pos = 100
                    self.gotblue = False
                    self.luck = False
                    self.player.image = pygame.transform.scale(pygame.image.load('PowerPlayer.png'), (35,35))
                    random.choice([self.bpowerup.bmove,self.bpowerup.bspeed,self.bpowerup.bscore,self.bpowerup.bshield,self.bpowerup.brare,self.bpowerup.bcommon,self.bpowerup.bdeath])()
        new_game = Game('Background.png',title, width, height)
        clock.tick(1)
        new_game.run_game_loop()
class GameObject:
    def __init__(self,image_path,x,y,width,height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width,height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height    
    def draw(self,background):
        background.blit(self.image, (self.x_pos,self.y_pos))
class PowerUp(GameObject):
    speed = 2.5
    def __init__(self,image_path,x,y,width,height):
        super().__init__(image_path,x,y,width,height)
    def move(self):
        if new_game.gotblue == True:
            self.speed = 1.25
        else:
            self.speed = 2.5
        self.y_pos -= self.speed
    def mini(self):
        new_game.togglefriction = 0
        new_game.miniimage = True
        new_game.player.width = 35
        new_game.player.height = 35
        new_game.player.x_pos += 7.5
        new_game.increasespeed = 1.75
        new_game.powername = 'Mini'
        if new_game.gotblue == True:
            new_game.player.x_pos += 7.5
            new_game.player.width = 20
            new_game.player.height = 20
            new_game.player.y_pos -= 35
            new_game.increasespeed = 4
            new_game.powername = 'Nano'
        new_game.player.speed = new_game.playerspeed + new_game.increasespeed
    def increasegap(self):
        new_game.gapboost = 42
        new_game.powername = 'Gap Boost'
        if new_game.gotblue == True:
            new_game.gapboost = 95
            new_game.powername = 'Huge Gap Boost'
        new_game.newflaggap = random.randint(200 + new_game.gapboost,250 + new_game.gapboost)
        distance = ((new_game.newflaggap - new_game.flaggap)/2)
        distance2 = 0
        if new_game.flag1.x_pos - distance < 0:
            distance2 = -(new_game.flag1.x_pos - distance)
        elif new_game.flag2.x_pos + distance > width - new_game.flag2.width:
            distance2 = width - new_game.flag2.width - (new_game.flag2.x_pos + distance)
        new_game.flag1.x_pos += -distance + distance2
        new_game.flag2.x_pos += distance + distance2
    def decreaseflagspeed(self):
        new_game.speedratio = 0.67
        new_game.powername = 'Slow Flag Speed'
        if new_game.gotblue == True:
            new_game.slow = True
            new_game.speedratio = 0.55
            new_game.powername = 'Freeze'
    def scoreboost(self):
        new_game.scoreboost = 0.51
        new_game.powername = 'Score Boost'
        if new_game.gotblue == True:
            new_game.scoreboost = 1.15
            new_game.powername = 'Doubler'
    def shield(self):
        new_game.shield = True
        new_game.powername = 'Shield'
        if new_game.gotblue == True:
            new_game.strongshield = True
            new_game.doubleshield = True
            new_game.powername = 'Strong Shield'
    def opposite(self):
        if new_game.gotblue == False:
            new_game.luck = True
            new_game.luckratio = 4
            new_game.speedratio = 0.1
            new_game.opposite = True
            new_game.bounceeffect = -1
            new_game.gapboost = 10
            new_game.newflaggap = random.randint(200 + new_game.gapboost,250 + new_game.gapboost)
            distance = ((new_game.newflaggap - new_game.flaggap)/2)
            distance2 = 0
            if new_game.flag1.x_pos - distance < 0:
                distance2 = -(new_game.flag1.x_pos - distance)
            elif new_game.flag2.x_pos + distance > width - new_game.flag2.width:
                distance2 = width - new_game.flag2.width - (new_game.flag2.x_pos + distance)
            new_game.flag1.x_pos += -distance + distance2
            new_game.flag2.x_pos += distance + distance2
            new_game.player.y_pos -= 7.5
            new_game.powername = 'Power Surge'
        else:
            random.choice([new_game.powerup.mini,new_game.powerup.increasegap,new_game.powerup.decreaseflagspeed,new_game.powerup.scoreboost,new_game.powerup.shield,new_game.powerup.opposite,new_game.powerup.luck])()
    def luck(self):
        new_game.luck = True
        if new_game.gotblue == True:
            new_game.luckratio = 2.5
            new_game.powername = 'Four Leaf Clover'
        else:
            new_game.luckratio = 4.25
            new_game.powername = 'Luck'
        distance = ((new_game.player.x_pos+25) - (new_game.flaggap/2+25+new_game.flag1.x_pos))/new_game.luckratio
        if new_game.flag1.x_pos + distance < 0:
            distance = -new_game.flag1.x_pos
        elif new_game.flag2.x_pos + distance > width - new_game.flag2.width:
            distance = width - new_game.flag2.width - new_game.flag2.x_pos
        new_game.flag1.x_pos += distance
        new_game.flag2.x_pos += distance
        new_game.luckboost = random.randint(15,25)
        new_game.newflaggap = random.randint(200 + new_game.luckboost,250 + new_game.luckboost)
        distance = ((new_game.newflaggap - new_game.flaggap)/2)
        distance2 = 0
        if new_game.flag1.x_pos - distance < 0:
            distance2 = -(new_game.flag1.x_pos - distance)
        elif new_game.flag2.x_pos + distance > width - new_game.flag2.width:
            distance2 = width - new_game.flag2.width - (new_game.flag2.x_pos + distance)
        new_game.flag1.x_pos += -distance + distance2
        new_game.flag2.x_pos += distance + distance2
class BadPowerup(GameObject): #OPPURTUNITY?
    speed = 3
    def __init__(self,image_path,x,y,width,height):
        super().__init__(image_path,x,y,width,height)
    def move(self):
        self.y_pos -= self.speed
        if new_game.change == True and (self.y_pos + self.height < height / 2):
            new_game.change = False
            self.image = pygame.transform.scale(pygame.image.load("BadPowerup.png"), (50,50))
    def bmove(self):
        new_game.playerspeed -= 0.4
        new_game.bpowerups.append("Exhaustion")
    def bspeed(self):
        new_game.blevel += 0.5
        new_game.bpowerups.append("Flag Speed Up")
    def bscore(self):
        new_game.score -= 20
        new_game.bpowerups.append("Time Travel")
    def bshield(self):
        new_game.bshield = True
        new_game.bdoubleshield = True
        new_game.bpowerups.append("Strong Anti Shield") 
    def brare(self):
        new_game.powerchance += 2
        new_game.bpowerups.append("Rarer Powerups")
    def bcommon(self):
        if new_game.bpowerchance != 3:
            new_game.bpowerchance += 1
            new_game.bpowerups.append("Skull Reinforcement")
        else:
            random.choice([new_game.bpowerup.bmove,new_game.bpowerup.bspeed,new_game.bpowerup.bscore,new_game.bpowerup.bshield,new_game.bpowerup.brare,new_game.bpowerup.bdeath])()
    def bdeath(self):
        if new_game.bdeath == False:
            new_game.bdeath = True
            new_game.bdeathscore = new_game.score + random.randint(40,60)
            new_game.bpowerups.append("Death at Score: "+str(new_game.bdeathscore))
        else:
            random.choice([new_game.bpowerup.bmove,new_game.bpowerup.bspeed,new_game.bpowerup.bscore,new_game.bpowerup.bshield,new_game.bpowerup.brare,new_game.bpowerup.bcommon])()
    #worse effects
    #disguise luck?
class PlayerCharacter(GameObject):
    speed = 7.5
    def __init__(self,image_path,x,y,width,height):
        super().__init__(image_path,x,y,width,height)
    def move(self, directionx):
        if new_game.opposite == True:
            if random.randint(1,20) == 1:
                if self.y_pos == 85:
                    self.y_pos += 7.5
                elif self.y_pos == 115:
                    self.y_pos -= 7.5
                else:
                    self.y_pos += random.choice([-7.5,7.5])
        if directionx < 0:
            if not self.x_pos <= 0 :
                if not (new_game.opposite == True and random.randint(1,12) == 1):
                    self.x_pos = round(self.x_pos - self.speed,2)
                else:
                    if random.randint(1,11) != 1:
                        self.x_pos = round(random.choice([self.x_pos - self.speed * 3,self.x_pos + self.speed]),2)
                    else:
                        self.x_pos = round(random.choice([self.x_pos - self.speed * 9,self.x_pos + self.speed * 7]),2)
            else:
                self.x_pos = 0
        elif directionx > 0:
            if not self.x_pos + self.width >= width:
                if not (new_game.opposite == True and random.randint(1,12) == 1):
                    self.x_pos = round(self.x_pos + self.speed,2)
                else:
                    if random.randint(1,11) != 1:
                        self.x_pos = round(random.choice([self.x_pos + self.speed * 3,self.x_pos - self.speed]),2)
                    else:
                        self.x_pos = round(random.choice([self.x_pos + self.speed * 9,self.x_pos - self.speed * 7]),2)
            else:
                self.x_pos = width - self.width
    def detect_collision(self,body,leftcancel,rightcancel,otherbody):
        collide = False
        if new_game.opposite == True and otherbody != None:
            collide = True
        if self.y_pos >= body.y_pos + body.height:
            return False
        if self.y_pos + self.height <= body.y_pos:
            return False
        if leftcancel:
            if self.x_pos >= body.x_pos + body.width:
                if collide == True:
                    if self.x_pos <= otherbody.x_pos + otherbody.width:
                        return collide
                return False
        if rightcancel:
            if self.x_pos + self.width <= body.x_pos:
                if collide == True:
                    if self.x_pos + self.width >= otherbody.x_pos:
                        return collide
                return False
        return not collide
class EnemyCharacter(GameObject):
    speed = 1
    def __init__(self,image_path,x,y,width,height):
        super().__init__(image_path,x,y,width,height)
    def move(self):
        if self.y_pos <= -self.height:
            self.y_pos = height
            if new_game.level < 13:
                new_game.level = round(new_game.level + 0.1, 2)
            new_game.randomizeflagpos = True
        else:
            if (self.y_pos + self.height / 2 < height / 2) or new_game.slow == True:
                self.y_pos -= (self.speed * new_game.speedratio)
            else:
                new_game.displaylevel = round(new_game.level + new_game.blevel,1)
                self.y_pos -= self.speed
new_game = Game('Background.png',title, width, height)
new_game.run_game_loop()
