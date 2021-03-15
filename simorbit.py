from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib.animation import FuncAnimation
from math import cos, sin
import sys

G = 6.67e-11
M = 6.24e14
robj = 30
timeacc = 20
fig = plt.figure(figsize = (5, 5))
ax = fig.add_axes([0,0,1,1])
ax.set_xlim((-500,500))
ax.set_ylim((-500,500))


fps = 20
frames = 500

class Particule:
  def __init__(self, x, y, vx, vy):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy

  def move(self, dt):
    r = (self.x**2 + self.y**2)**0.5
    if r <= robj:
        sys.exit()
    self.uy = -self.y/r
    self.ux = -self.x/r
    F = G * M / r**2
    ay = F*self.uy
    ax = F*self.ux
    self.vx += dt * ax
    self.vy += dt * ay
    self.x += self.vx * dt
    self.y += self.vy * dt

part = Particule(0, 100, 25, 0)
pos = (0, 75)
scat = ax.scatter(pos[0], pos[1])
ax.scatter(0,0, c='r', s = 10)
# for i in range(10):
#   part.move(0.1)
#   plt.quiver(part.x, part.y, part.ux, part.uy)
#   plt.scatter(part.x, part.y)
#   print(part.ux, part.uy)
# plt.show()
i = 0
def update(frame):
  global i
#   if i%(fps/2) == 0:
#       plt.scatter(part.x, part.y, c='b', s = 5)
  part.vx *= 0.999
  part.vy *= 0.999

  i+=1
  part.move((1/fps)*timeacc)
  pos = (part.x, part.y)
  scat.set_offsets(pos)
  
  

animation = FuncAnimation(fig, update, interval=(1/fps)*1000, blit=False, frames = frames)

plt.show()