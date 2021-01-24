#CENG487 Assignment5 by
#Umut Utku Tahan
#250201086
#December 2019

class Material: #ambient and diffuse values taken from polygons original color
    def __init__(self,specular,emission,shininess):
        #self.ambient=ambient
        self.shininess=shininess
        self.specular=specular
        self.emission=emission
        #self.diffuse=diffuse
        