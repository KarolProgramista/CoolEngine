import pygame

# Class of any object on scene
class GameObject(object):
    def __init__(self, x, y, width, height, name):
        # Public variables
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.name = str(name)
        self.collidable: bool = False
        self.parent: GameObject = None

        # Private variables
        self._rect = pygame.Rect(x, y, width, height)

        # Setup
        self.Setup()

    def _hiden_update(self, window):
        self._rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self._draw(window)

    def _draw(self, window):
        pass

# Rectangle class (I think all args are easy to understand)
class Rectangle(GameObject):
    def __init__(self, x, y, width, height, name, color):
        super().__init__(x, y, width, height, name)
        self.color = tuple(color)

    def _draw(self, window):
        pygame.draw.rect(window, self.color, self._rect)

# Cicle class. Width and height are hit box sizes
class Cricle(GameObject):
    def __init__(self, x, y, width, height, radius, name, color):
        super().__init__(x, y, width, height, name)
        self.color = tuple(color)
        self.radius = int(radius)

    def _draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

# Triangle class
class Triangle(GameObject):
    def __init__(self, x, y, width, height, name, color):
        super().__init__(x, y, width, height, name)
        self.color = tuple(color)

    def _draw(self, window):
        pygame.draw.polygon(window, self.color, [(self.x, self.y+self.height), (self.width+self.x, self.y+self.height), ((self.x + (self.width/2)), self.y)])

# Sprite class. If imagePath = None (default) color will be used
class Sprite(GameObject):
    def __init__(self, x, y, width, height, name, color=None, imagePath=None):
        super().__init__(x, y, width, height, name)
        self.color = tuple(color)
        self.imagePath = str(imagePath)

        # Private
        if imagePath is not None:
            self._image = pygame.image.load(imagePath)

    def _draw(self, window):
        if self.imagePath is not None:
            transformed = pygame.transform.scale(self._image, (self.width, self.height))
            window.blit(transformed, (self.x, self.y))


