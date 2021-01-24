#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#January 2020

class Scene:
    def __init__(self):
        self.objects=[]
    def addObject(self,obj):
        self.objects.append(obj)
    def deleteObject(self,obj):
        self.objects.remove(obj)
    def cleanScene(self):
        self.objects=[]