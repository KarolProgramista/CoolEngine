import pygame
import threading

# Basic error
class Error(Exception):
    pass

# Class of any object on scene
class GameObject(object):
    def __init__(self, x, y, width, height, name):
        # Public variables
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.name = str(name)
        self.collidable: bool = False  # Set it if you wont to make collisions with that obj
        self.draw_hitboxes: bool = False  # Set it to True if you want to display hitboxes of game object
        self.hitbox_color: tuple = (0, 0, 0)  # Set the color of hitbox

        # Private variables
        self._rect = pygame.Rect(x, y, width, height)
        self._parent = None
        self._children = []
        self._window = None
        self._stop = [0, 0]
        self._child_ycoll = False
        self._child_xcoll = False

        # Setup
        self.Setup()

    def _hiden_update(self):
        self._rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self._draw()
        self._draw_hitboxes()

    def _draw_hitboxes(self):
        if self.draw_hitboxes is True:
            pygame.draw.rect(self._window._window, self.hitbox_color, self._rect, 2)

    def _draw(self):
        pass

    # This function add new children to GameObject
    # Children must be game object
    def AddChild(self, child):
        self._children.append(child)
        child._parent = self

    # This fucntion scales object
    def Scale(self, width: int, height: int):
        self.width += width
        self.height += height

        if self._children:
            for child in self._children:
                child.Scale(width, height)

    # This function sets size of object
    def SetSize(self, width: int, height: int):
        self.width = width
        self.height = height

        if self._children:
            for child in self._children:
                child.SetSize(width, height)

    # This function change position for object
    def Translate(self, x: int, y: int):
        if self.collidable or (self._parent and self._parent.collidable):
            new_x = self.x + x
            new_y = self.y + y

            # For x
            self._rect = pygame.Rect(new_x, self.y, self.width, self.height)

            for obj in self._window._all_game_objects:
                if obj.collidable is True and not obj == self:
                    rc = self.CheckCollison(obj)
                    if rc:
                        if self._parent:
                            self._parent._child_xcoll = True
                        new_x = self.x

            if not new_x == self.x:
                if self._children:
                    for child in self._children:
                        child.Translate(x, 0)
                if self._parent:
                    self._parent._child_xcoll = False

            # For y
            self._rect = pygame.Rect(self.x, new_y, self.width, self.height)

            for obj in self._window._all_game_objects:
                if obj.collidable is True and not obj == self:
                    rc = self.CheckCollison(obj)
                    if rc:
                        new_y = self.y

                        if self._parent:
                            self._parent._child_ycoll = True

            if not new_y == self.y:
                if self._children:
                    for child in self._children:
                        child.Translate(0, y)
                if self._parent:
                    self._parent._child_ycoll = False

            if not self._child_xcoll:
                self.x = new_x
            if not self._child_ycoll:
                self.y = new_y
        # else:
        #     self.x += x
        #     self.y += y

        #     if self._children:
        #         for child in self._children:
        #             child.Translate(x, y)

    # This function returns parent of GameObject
    def GetParent(self):
        try:
            return self._parent
        except AttributeError:
            raise Error(self.name + " Does not have a parent")

    # This function gets gameObject and check collision with it
    def CheckCollison(self, gameObject):
        rc = self._rect.colliderect(gameObject._rect)
        return rc

# Rectangle class (I think all args are easy to understand)
class Rectangle(GameObject):
    def __init__(self, x, y, width, height, name, color):
        super().__init__(x, y, width, height, name)
        self.color = tuple(color)

    def _draw(self):
        pygame.draw.rect(self._window._window, self.color, self._rect)

# Cicle class. Width and height are hit box sizes
class Cricle(GameObject):
    def __init__(self, x, y, width, height, radius, name, color):
        super().__init__(x, y, width, height, name)
        self.color = tuple(color)
        self.radius = int(radius/2)

    def _draw(self):
        pygame.draw.circle(self._window._window, self.color, (int(self.x + self.width/2), int(self.y + self.height/2)), self.radius)

# Triangle class. Uper point may be up, down, left, right
class Triangle(GameObject):
    def __init__(self, x, y, width, height, name, color, uper_point):
        super().__init__(x, y, width, height, name)
        self.color = tuple(color)
        self.uper_point = str(uper_point)

    def _draw(self):
        if self.uper_point == "up":
            pygame.draw.polygon(self._window._window, self.color, [(self.x, self.y+self.height), (self.x+self.width, self.y+self.height), ((self.x + self.width/2, self.y))])
        elif self.uper_point == "down":
            pygame.draw.polygon(self._window._window, self.color, [(self.x, self.y), (self.width+self.x, self.y), (self.x + (self.width/2)), (self.y+self.height)])

# Sprite class. If imagePath = None (default) color will be used
class Sprite(GameObject):
    def __init__(self, x, y, width, height, name, color=None, imagePath=None):
        self.color = tuple(color)
        self.imagePath = str(imagePath)

        # Private
        if imagePath is not None:
            self._image = pygame.image.load(imagePath)

        super().__init__(x, y, width, height, name)

    def _draw(self):
        if self.imagePath is not None:
            self._image = pygame.image.load(self.imagePath)
            transformed = pygame.transform.scale(self._image, (self.width, self.height))
            self._window._window.blit(transformed, (self.x, self.y))
        elif self.color is not None:
            pygame.draw.rect(self._window._window, self.color, self._rect)
        else:
            raise ValueError(f"No color and image in {self.name}")


