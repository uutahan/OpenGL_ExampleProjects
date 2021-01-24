#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#January 2020

from OpenGL.GL import *
import OpenGL.GL.shaders

class ShaderLoader:

    def load_shader(self,shader_file):
        shader_source = ""
        with open(shader_file) as f:
            shader_source = f.read()
        f.close()
        return str.encode(shader_source)
    
    def compile_shader(self,vs, fs):
        vert_shader = self.load_shader(vs)
        frag_shader = self.load_shader(fs)
    
        shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vert_shader, GL_VERTEX_SHADER),
                                                  OpenGL.GL.shaders.compileShader(frag_shader, GL_FRAGMENT_SHADER))
        return shader