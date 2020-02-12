import pygame
import GameObjects

pygame.init()


class Window(object):
    def __init__(self, width, height):
        # Public variables
        # Width and height variables
        self.WIDTH = width
        self.HEIGHT = height

        # Private variables
        self.__window = pygame.display.set_mode((width, height))
        self.__all_game_objects = list()
        self.__bg = (0, 0, 0)

    # This function runs engine
    def run(self):
        while(True):
            self.__update()

    # This function set title of the window
    def set_title(self, text):
        if type(text) is str:
            pygame.display.set_caption(text)
        else:
            raise Exception("Title must be string")

    # Set color background for game
    def set_background(self, color):
        if type(color) is tuple:
            self.__bg = color
        else:
            raise ValueError("Color must be tuple")

    # Get color of background
    def get_background(self):
        return self.__bg

    # This fuction update display and draw all images
    def __update(self):
        # Get inputs
        self.__get_inputs()

        # Fill window
        self.__window.fill(self.__bg)

        # Update all objs
        for object in self.__all_game_objects:
            object._hiden_update(self.__window)
            object.Update()

        # Update display
        pygame.display.update()

    def __get_inputs(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()

    # Adding objects
    def add_game_object(self, Object):
        if isinstance(Object, GameObjects.GameObject) is True:
            self.__all_game_objects.append(Object)
        else:
            raise ValueError("Given arg isn't GameObject")

