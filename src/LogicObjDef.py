### Logic Object Definition ###

class LogicObjDef:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

        self.obj = [] #Have actual game object

        self.action = 0 #ID of an action

    def activate(self, obj):
        self.obj[obj].activate()

    def addObj(self, obj):
        self.obj.append(obj)
    def removeObj(self, pos):
        self.obj.pop(pos)
        
