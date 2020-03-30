import Cengine.CoolEngine as CoolEngine
import time

window = CoolEngine.Window(300, 200)
window.set_title("TEST")
window.set_background((116, 192, 204))
print(f"BG is {window.get_background()}")

class Boy(CoolEngine.Rectangle):
    def Setup(self):
        pass

    def Update(self):
        if self.GetParent().changed == 1:
            if self.GetParent().dir == 1:
                self.x = self.GetParent().x + 20
            elif self.GetParent().dir == -1:
                self.x = self.GetParent().x - 10

class Wall(CoolEngine.Rectangle):
    def Setup(self):
        self.collidable = True
    def Update(self):
        pass

class Man(CoolEngine.Cricle):
    def Setup(self):
        self.collidable = True
        self.dir = 1
        self.diry = -3
        self.changed = 0
        self.timer = 0

    def Update(self):
        self.timer += window.second_per_frame()
        if self.timer >= 1:
            self.diry = 0
        if CoolEngine.Input(window, CoolEngine.KEY_RIGHT):
            if not self.dir == 1:
                self.changed = 1
            else:
                self.changed = 0
            self.dir = 1
        elif CoolEngine.Input(window, CoolEngine.KEY_LEFT):
            if not self.dir == -1:
                self.changed = 1
            else:
                self.changed = 0
            self.dir = -1
        else:
            self.changed = 0

        if CoolEngine.Input(window, CoolEngine.KEY_UP):
            self.AddForce(-3, -3)
        self.Translate(self.dir, self.diry)

class Girl(CoolEngine.Triangle):
    def Setup(self):
        pass

    def Update(self):
        pass

class Woman(CoolEngine.Sprite):
    def Setup(self):
        self.ScaleUp = True
        self.timer = 0

    def Update(self):
        self.timer += window.second_per_frame()
        self.Scaleing()

    def Scaleing(self):
        if self.timer > 0.01:
            if self.ScaleUp is True and self.width < 100:
                self.Scale(1, 1)
            elif self.ScaleUp is True:
                self.ScaleUp = False
            elif self.ScaleUp is False and self.width > 5:
                self.Scale(-1, -1)
            elif self.ScaleUp is False:
                self.ScaleUp = True

            self.timer = 0


m = Man(40, 175, 20, 20, 20, "Orofar", (255, 0, 0))
# m.draw_hitboxes = True
m.useGravity = True
b = Boy(60, 180, 10, 10, "Karol", (255, 0, 0))
wall1 = Wall(100, 180, 10, 10, "WAll1.0", (0, 0, 0))
wall2 = Wall(10, 180, 10, 10, "wall2.0", (0, 0, 0))
wall3 = Wall(10, 50, 300, 10, "wall3.0", (0, 0, 0))
wall4 = Wall(0, 196, 300, 10, "wall4.0", (0, 0, 0))

g = Girl(30, 90, 10, 10, "Trobums", (255, 0, 0), "up")
g.draw_hitboxes = True

m.AddChild(b)

window.add_game_object(b)
window.add_game_object(m)
window.add_game_object(g)
window.add_game_object(Woman(100, 90, 0, 0, "Chory", imagePath="bee.png", color=(255, 0, 0)))
window.add_game_object(wall1)
window.add_game_object(wall2)
window.add_game_object(wall3)
window.add_game_object(wall4)

window.run()
