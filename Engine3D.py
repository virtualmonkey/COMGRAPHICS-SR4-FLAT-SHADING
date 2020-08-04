from gl import Render, color, V2, V3
from obj import Obj 

import random

r = Render(1000,1000)
#r = Render(200,200)

r.loadModel('./models/model.obj', V3(500,500,0), V3(300,300,300))
#r.loadModel('./models/face.obj', V3(500,250,0), V3(20,20,20))


#r.triangle_bc(V2(10, 70),  V2(50, 160), V2(70, 80), color(random.randint(0, 255) / 255, random.randint(0, 255)/ 255, random.randint(0, 255)/ 255))
#r.triangle_bc(V2(180, 50), V2(150, 1),  V2(70, 180), color(random.randint(0, 255)/ 255, random.randint(0, 255)/ 255, random.randint(0, 255)/ 255))
#r.triangle_bc(V2(180, 150), V2(120, 160), V2(130, 180), color(random.randint(0, 255)/ 255, random.randint(0, 255)/ 255, random.randint(0, 255)/ 255))


r.glFinish('output.bmp')