#Wall Class Definition

class wallObjDef():
    def __init__(self):
        self.x = [0,0]
        self.y = [0,0]
        self.z = [0,0]

        self.solid = True
        self.visible = True

        self.direction = 0
        self.speed = 0

    def move(self):
        if self.direction == 0:
            self.y[0] -= self.speed
            self.y[1] -= self.speed
        if self.direction == 90:
            self.x[0] += self.speed
            self.x[1] += self.speed
        if self.direction == 180:
            self.y[0] += self.speed
            self.y[1] += self.speed
        if self.direction == 270:
            self.x[0] -= self.speed
            self.x[1] -= self.speed
            
        if self.direction == 45:
            self.y[0] -= self.speed/2
            self.y[1] -= self.speed/2
            self.x[0] += self.speed/2
            self.x[1] += self.speed/2

        if self.direction == 135:
            self.y[0] += self.speed/2
            self.y[1] += self.speed/2
            self.x[0] += self.speed/2
            self.x[1] += self.speed/2

        if self.direction == 225:
            self.y[0] += self.speed/2
            self.y[1] += self.speed/2
            self.x[0] -= self.speed/2
            self.x[1] -= self.speed/2

        if self.direction == 315:
            self.y[0] -= self.speed/2
            self.y[1] -= self.speed/2
            self.x[0] -= self.speed/2
            self.x[1] -= self.speed/2

    def vis(self):
        self.visible = True
    def invis(self):
        self.visible = False

    def desolid(self):
        self.solid = False
    def solidify(self):
        self.solid = True
