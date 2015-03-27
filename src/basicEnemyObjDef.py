### Basic Enemy Class Definition ###

class BasicEnemyClassObjDef:
    def __init__(self, X, Y, Z, Health, MaxHealth, Speed, Target):
        self.x = X
        self.y = Y
        self.z = Z

        self.health = Health
        self.maxHealth = MaxHealth

        self.speed = Speed
        self.direction = 0

        self.moving = False

        self.target = Target

    def AI(self):
        ### Movement ###

        # Target Location #

        if type(self.target) is tuple:

            targetUse = []
            
            for item in self.target: targetUse.append(item)

            self.target = targetUse

        elif type(self.target) is list:
            pass #Stops a list from being converted.

        else: self.target = [self.target.x, self.target.y]

        # Got Target Location #

        if self.target[0] > self.x and self.target[1] > self.y: self.direction = 135
        if self.target[0] > self.x and self.target[1] == self.y: self.direction = 90
        if self.target[0] > self.x and self.target[1] < self.y: self.direction = 45
        if self.target[0] == self.x and self.target[1] > self.y: self.direction = 0
        if self.target[0] == self.x and self.target[1] < self.y: self.direction = 180
        if self.target[0] < self.x and self.target[1] > self.y: self.direction = 225
        if self.target[0] < self.x and self.target[1] == self.y: self.direction = 270
        if self.target[0] < self.x and self.target[1] < self.y: self.direction = 315

        # Set Direction #

        self.move()

    def move(self):
        if self.direction == 0: self.y -= self.speed #Straight up
        if self.direction == 90: self.x += self.speed #Right
        if self.direction == 180: self.y += self.speed #Down
        if self.direction == 270: self.x -= self.speed #Left

        if self.direction == 45:
            self.x += self.speed/2
            self.y -= self.speed/2
        if self.direction == 135:
            self.x += self.speed/2
            self.y += self.speed/2
        if self.direction == 225:
            self.x -= self.speed/2
            self.y += self.speed/2
        if self.direction == 315:
            self.x -= self.speed/2
            self.y -= self.speed/2


    def update(self):
        if self.health > self.maxHealth: self.health = self.maxHealth
        if self.speed < 0: print("ERROR: NEGATIVE SPEED")

        self.AI()
        
