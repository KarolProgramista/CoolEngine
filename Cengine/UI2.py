import pygame
import time

# Basic UI Element (do not use)
class _UiElement(object):
    pass

# Image class
class Image(object):
    def __init__(self, path: str):
        self._path = path
        self._image = pygame.image.load(self._path)

# Button class
# command must be none argument function
class Button(_UiElement):
    def __init__(self, x: int, y: int, width: int, height: int, normal_color: tuple, hover_color: tuple, 
    text_color: tuple, text_size: int, text: str,command=None, image: Image = None):
        # Coordinates
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # Color when no action is on button
        self.normal_color = normal_color
        # Color when mouse is on it
        self.hover_color = hover_color

        # Text color
        self.text_color = text_color
        # Size of font
        self.text_size = text_size
        # Text variable
        self.text = text
        # Is widget enabled
        self.enabled = True

        self.__command = command
        self._window = None
        self._image = image._image if not image == None else None
        

    def _render(self):
        if self.enabled:
            # Mouse events
            mouse = pygame.mouse.get_pos()
            mouse_key = pygame.mouse.get_pressed()

            # Chechking button events and drawing it
            if self.x+self.width > mouse[0] > self.x and self.y+self.height > mouse[1] > self.y:
                if self._image == None:
                    pygame.draw.rect(self._window._window, self.hover_color, (self.x, self.y, self.width, self.height))
                else:
                    scaled_image = pygame.transform.scale(self._image, (self.width, self.height))
                    self._window._window.blit(scaled_image, (self.x, self.y))
                if mouse_key[0] == 1:
                    time.sleep(0.1)
                    self.__command()

            else:
                if self._image == None:
                    pygame.draw.rect(self._window._window, self.normal_color, (self.x, self.y, self.width, self.height))
                else:
                    scaled_iamge = pygame.transform.scale(self._image, (self.width, self.height))
                    self._window._window.blit(scaled_iamge, (self.x, self.y))

            # Setting a text on the button
            font = pygame.font.SysFont("Arial", self.text_size)
            rendered_text = font.render(self.text, 0, self.text_color)
            text_rect = rendered_text.get_rect(center = (self.x+self.width/2, self.y+self.height/2) )
            text_rect.center = ((self.x+(self.width/2)), (self.y+(self.height/2)))
            self._window._window.blit(rendered_text, text_rect)

    def SetActive(state: bool):
        self.enabled = state


# Label class
class Label(_UiElement):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, text_color: tuple, text_size: int, text: str, image: Image = None):
        # Coordinates
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)

        # background color
        self.color = tuple(color)

        # Text color
        self.text_color = tuple(text_color)
        # Text size
        self.text_size = int(text_size)
        # Text variable
        self.text = str(text)
        # Is widget enabled or not
        self.enabled = True

        self._image = image._image if not image == None else None 
        self._window = None

    def _render(self):
        if self.enabled:
            rect = pygame.Rect(self.x, self.y, self.width, self.height)
            if not self._image:      
                label_rect = pygame.draw.rect(self._window._window, self.color, rect)
            else:
                scaled_image = pygame.transform.scale(self._image, (self.width, self.height))
                self._window._window.blit(scaled_image, (self.x, self.y))
            # Setting a text on the label
            font = pygame.font.SysFont("Arial", self.text_size)
            rendered_text = font.render(self.text, 0, self.text_color)
            text_rect = rendered_text.get_rect(center = (self.x+self.width/2, self.y+self.height/2) )
            text_rect.center = ((self.x+(self.width/2)), (self.y+(self.height/2)))
            self._window._window.blit(rendered_text, text_rect)

    def SetActive(state: bool):
        self.enabled = state