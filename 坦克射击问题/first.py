from gekko import GEKKO
import math
import numpy as np
m = GEKKO()
shite = m.Var(0)
t = m.Var(value=20)
m.Equations([0.32 * m.cos(shite) * t * 2 - 10 == 0,
             0.32 * m.sin(shite) - 1 * t == 0,])
# m.Equations([cshite >= 0,cshite <= 1])
# m.Equations([sshite >= 0,sshite <= 1])
m.solve(disp=False)
print(t.value)
# print(x1,y1,x2,y2,x3,y3)
# break



