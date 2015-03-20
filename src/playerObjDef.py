#Player Object Definition

class playerObjDef:
    def __init__(self):
        self.x = 0 #Keep as floats but convert to ints before use outside of calculations.
        self.y = 0
        self.z = 0 #Not used for 3D, just for what should be above other stuff

        self.direction = 0 #Bearing
        self.speed = 0
        
        
