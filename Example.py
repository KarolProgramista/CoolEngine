import Cengine.CoolEngine as CoolEngine

# Setting window object
window = CoolEngine.Window(800, 600)
# Setting title
window.set_title("Example")
# Setting bg
window.set_background((100, 100, 100))

# Simple rectangle
# Every game object needs Setup and Update
class Box(CoolEngine.Rectangle):
    def Setup(self):
        pass
    def Update(self):
        pass

class Enemy(CoolEngine.Rectangle):
    def Setup(self):
        self.dir = 1
        self.strike = 0
    def Update(self):
        if self.strike > 100:
            self.strike = 0
            self.dir *= -1
        else:
            self.strike += 1
            self.Translate(self.dir, 0)

e1 = Enemy(600, 100, 20, 20, 'Enemy1', (255, 0, 0))
e1.collidable = True
e1.useGravity = True

class Player(CoolEngine.Triangle):
    def Setup(self):
        self.dir = 0
        self.speed = 3
        self.is_left_clicked = False
        self.is_right_cliced = False
        self.timer = 0
        self.alive = True
        self.current_scale = 0
    def Update(self):
        # Basic timer
        self.timer += window.second_per_frame()
        # Die
        if self.CheckCollison(e1):
            self.alive = False
        if not self.alive:
            self.die()
            
        if self.alive:
            # Translateing player
            self.Translate(self.dir*self.speed, 0)
            # Example of inputs
            if(CoolEngine.InputDown(window, CoolEngine.KEY_LEFT)):
                self.is_left_clicked = True
            elif (CoolEngine.InputUp(window, CoolEngine.KEY_LEFT)):
                self.is_left_clicked = False
            if(CoolEngine.InputDown(window, CoolEngine.KEY_RIGHT)):
                self.is_right_cliced = True
            elif (CoolEngine.InputUp(window, CoolEngine.KEY_RIGHT)):
                self.is_right_cliced = False

            if self.is_left_clicked:
                self.dir = -1
            elif self.is_right_cliced:
                self.dir = 1
            else:
                self.dir = 0

    def die(self):
        if self.timer >= 1:
            self.useGravity = False
            self.collidable = False
            self.Scale(2,2)
            self.Translate(-2, -2)
            self.current_scale += 1

        if self.current_scale >100:
            window.destroy(self)


floor = Box(0, window.HEIGHT-20, window.WIDTH, 20, 'floor', (0, 0, 0))
floor.collidable = True

player = Player(10, 100, 10, 20, 'Player', (255, 0,0), 'up')
player.collidable = True
player.useGravity = True

window.add_game_object(player)
window.add_game_object(floor)
window.add_game_object(e1)


# Running game
window.run()

