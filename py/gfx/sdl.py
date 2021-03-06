import sdl2
import sdl2.ext as lib

import ascii

lib.init()

# stub draft

class SDL2:
    def __init__(self, size=None):
        if size is None:
            size = ascii.ASCII().dims * 8
        self.window = lib.Window('', size=size)
        self.window.show()
        self.renderer = lib.Renderer(self.window)
    def plot(self, vec2, color=(1.0,1.0,1.0)):
        self.renderer.draw_point(vec2, lib.Color(*(int(color * 255 + 0.5) for color in color)))
    def blit(self):
        self.renderer.present()



if __name__ == '__main__':
    sdl2 = SDL2()
    #for x in range(
    print(sdl2)
