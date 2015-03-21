#Player Object Definition

class playerObjDef:
    def __init__(self):
        self.x = 0 #Keep as floats but convert to ints before use outside of calculations.
        self.y = 0
        self.z = 0 #Not used for 3D, just for what should be above other stuff

        self.direction = 0 #Bearing
        self.speed = 0
        self.solid = True
        self.visible = True

    def move(self):
        if self.direction == 0: self.y -= self.speed #Straight up
        if self.direction == 90: self.x += self.speed #Right
        if self.direction == 180: self.y += self.speed #Down
        if self.direction == 270: self.x -= self.speed #Left

        if self.diection == 45:
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

    def invis(self): self.visible = False
    def vis(self): self.visible = True

    def desolid(self): self.solid = False
    def solidify(self): self.solid = True
    
