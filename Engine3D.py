from gl import Render, color, V2, V3
from obj import Obj 

import random

r = Render(1000,1000)

r.loadModel('./models/natsuki.obj', V3(500,500,0), V3(300,300,300))

r.glFinish('output.bmp')
r.glZBuffer('zbuffer.bmp')
