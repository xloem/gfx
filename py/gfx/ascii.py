import curses
import numpy as np
import os
import sys

curses.setupterm()
def _dims():
    return (curses.tigetnum('lines'), curses.tigetnum('cols'))
HOME = curses.tigetstr('home')

class ASCII:
    aspect = np.array((1, 0.5))
    def __init__(self, dims = None, background = ' '):
        self.background = background
        self._dims = dims
        self.clear()
    @property
    def width(self):
        return self.backbuffer.shape[1]
    @property
    def height(self):
        return self.backbuffer.shape[0]
    @property
    def dims(self):
        return np.array((self.width, self.height))
    def clear(self):
        dims = _dims() if self._dims is None else self._dims
        self.backbuffer = np.full(dims, self.background)
    def plot(self, x, y, char = '#'):
        self.backbuffer[y, x] = char
    def blit(self):
        sys.stdout.buffer.write(HOME)
        sys.stdout.buffer.write(b'\r\n'.join(self.backbuffer))
    def __enter__(self):
        self.clear()
        return self
    def __exit__(self, *params):
        self.blit()
        
if __name__ == '__main__':
    display = ASCII()
    center = display.dims // 2
    import math
    import time
    last_bounds = np.array((center, center))
    max_radius = min(center * display.aspect) / 2 + 1
    while True:

        radius = (math.sin(time.time() * 4) + 1) * max_radius / 2
        bounds = np.array(((center - radius + 0.5), (center + radius + 0.5)), dtype=np.int)
        if (bounds != last_bounds).any():
            with display:
                # this could also be a block assignment
                for x in range(*bounds[:,0]):
                    for y in range(*bounds[:,1]):
                        display.plot(x, y, '#')
            last_bounds = bounds
        else:
            time.sleep(0.1)
