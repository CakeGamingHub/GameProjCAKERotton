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
        pass #Add move method from player class here, possible tweaks needed.
