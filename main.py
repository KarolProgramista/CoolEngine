import CoolEngine

window = CoolEngine.Window(200, 200)
window.set_title("TEST")
window.set_background((116, 192, 204))
print(f"BG is {window.get_background()}")

class Boy(CoolEngine.Rectangle):
    def Setup(self):
        print("Set")

    def Update(self):
        pass

class Man(CoolEngine.Cricle):
    def Setup(self):
        pass

    def Update(self):
        pass

class Girl(CoolEngine.Triangle):
    def Setup(self):
        pass

    def Update(self):
        pass

class Woman(CoolEngine.Sprite):
    def Setup(self):
        pass

    def Update(self):
        pass


window.add_game_object(Boy(10, 10, 10, 10, "Karol", (255, 0, 0)))
window.add_game_object(Man(30, 50, 10, 10, 10, "Orofar", (255, 0, 0)))
window.add_game_object(Girl(30, 90, 10, 10, "Trobums", (255, 0, 0)))
window.add_game_object(Woman(100, 100, 40, 40, "Chory", imagePath="image.jpg", color=(255, 0, 0)))
window.run()
