# Cool Engine Documentation

## Classes
This engine is object based so to create
things you need objects and classes

### Window
Let's start with window. To start you need to create
an instance of it.  
Then costumize it with ``window.set_background()`` and ``window.set_title()``.  
If you run it now it won't start. You need to add ``window.run()``  
```python
    # Setting window object
    window = CoolEngine.Window(800, 600)
    # Setting title
    window.set_title("Example")
    # Setting bg
    window.set_background((100, 100, 100))

    # And run program
    window.run()
```

### Game Objects
Of course your game needs objects on window.  
First we need to create class that will represent our object on screen.  
You can add multiple instances on one class for example if you want to create  
walls around a room you can make one wall then add multiple instances.
To create class you need to define  
two functions ``Setup()`` and ``Update()``. Update function is runned once a frame   
and Setup is runned on ``Window.run()``.

Example class:
```python
    class Boy(GameObject):
        def Setup(self):
            pass

        def Update(self):
            pass
```

Then we need to create instance of class and add it into window.

```python
    b = Boy(x, y, width, height, name)

    window.add_game_object(b)

    # And run
    window.run()
```

To create objects we need to pass params. There are more than just  
plain GameObject.

There are other types:

```python
    Rectangle(x, y, width, height, name, color)

    # Width and height are hit box sizes
    Cricle(x, y, width, height, radius, name, color)

    # Uper point may be up, down, left, right
    Triangle(x, y, width, height, name, color, uper_point)

    # If imagePath = None (default) color will be used
    Sprite(x, y, width, height, name, color=None, imagePath=None)
```

----

## Fucntions

There are also a lot of functions for use.

### Window functions
Window has many functions that can help you in
develpoment.

```python
    # This function returns how mouch second pass per one frame
    second_per_frame(None) -> None

    # Destroy object
    destroy(Object: GameObjects.GameObject) -> None

    # Adding objects
    add_game_object(Object: GameObjects.GameObject) -> None

    # Get color of background
    get_background(None) -> tuple

    # Set color background for game
    set_background(color) -> None

    # This function set title of the window
    set_title(text) -> None

    # This function runs engine
    run(None) -> None
```

### Game Object functions
Game Object class has also many functions. There are collisons  
check, Translate and Scaling and more

```python
    # This fucntion scales object
    Scale(width: int, height: int) -> None

    # This function sets size of object
    SetSize(width: int, height: int) -> None

    # This function change position for object
    Translate(x: int, y: int) -> None

    # This function adds force for object
    # Only with useGravity True
    AddForce(x: int, y: int) -> None

    # This function returns parent of GameObject
    GetParent(None) -> None

    # This function gets gameObject and check collision with it
    CheckCollison(gameObject: GameObject) -> bool

    # This function do the same as this upper but
    # this function also handle not colidable objects
    CheckPosCollision(gameObject: GameObject) -> bool
```

### Inputs
There are two input functions: ``CoolEngine.InputDown(window: Window, key)``  
and `` CoolEngine.InputUp(window: Window, key)``. First return true when passed key was  
pressed and second return true when this key is up.

## Variables
### Window variables
Window has one variable that you can modify ``Window.fps`` its default
60  
but you can modify it. There are also ``Window.WIDTH`` and  ``Window.HEIGHT``  
This variables are read-only.

### GameObject variables
GameObjact has a lot of various variables to use.  
You can modify coordinates and size of GameObject but preferd is use  
``Scale()`` and ``Translate()``.

There are names of this variables
```python
    self.x = int(x)
    self.y = int(y)
    self.width = int(width)
    self.height = int(height)
```

Next we have some settings for your personal needs and their defaults

```python
        # Set it if you wont to make collisions with that obj
        self.collidable: bool = False
        # Set it to true if you want to make your obj fall down
        self.useGravity: bool = False
        # Set it to True if you want to display hitboxes of game object
        self.draw_hitboxes: bool = False
        # Set the color of hitbox
        self.hitbox_color: tuple = (0, 0, 0)
        # Set it to change gravity force
        self.gravity = 2 
```

**PRO TIP** If your object isn't going up make sure that you have beaten your  
gravity value.

### Key maps
```python
    KEY_1
    KEY_2
    KEY_3
    KEY_4
    KEY_5
    KEY_6
    KEY_7
    KEY_8
    KEY_9
    KEY_0
    KEY_a
    KEY_b
    KEY_c
    KEY_d
    KEY_e
    KEY_f
    KEY_g
    KEY_h
    KEY_i
    KEY_j
    KEY_k
    KEY_l
    KEY_m
    KEY_n
    KEY_o
    KEY_p
    KEY_q
    KEY_r
    KEY_s
    KEY_t
    KEY_u
    KEY_v
    KEY_w
    KEY_x
    KEY_y
    KEY_z
    KEY_LEFT
    KEY_RIGHT
    KEY_UP
    KEY_DOWN
    KEY_LCTRL
    KEY_RCTRL
    KEY_LSHIFT
    KEY_RSHIFT
    KEY_SLASH
    KEY_BACKSLASH
```

## Integrated UI2 library
### Getting started with UI
UI2 library is simple UI library. Its second version of UI library.  
UI library was used in some my projects. But it was operating on pygame.
UI2 library is now in alpha version. Its not published yet. But the version
for pygame will be published in future. In CoolEngine UI2 is small alpha
version. When UI2 would be published I will add full support.

### Classes
UI2 has three classes: ``UI.Image``, ``UI.Button`` and ``UI.Label``

#### Image
Image class is used for storing image.  
Params:
- path -> Its only one param that pass path to image

If you want to pass image to ``UI.Button`` or ``UI.Label``, pass instance of this class

#### Label
Label is text element with backgroud.  
Params for label\:
- x, y -> Coordinates of label
- width, height -> Size of label
- color -> Color of background
- text_color -> Color of text
- text_size -> Size of text's font
- text -> Text to show on label
- image (optional) -> Instance of class ``UI.Image`` with image
  
#### Button
Button is interactive element with background and text.  
Params for button\:
- x, y -> Coordinates of label
- width, height -> Size of label
- normal_color -> Color of background when no action acqure
- hover_color -> Color of backgorund when is hover over by mouse
- text_color -> Color of text
- text_size -> Size of text's font
- text -> Text to show on button
- command (optional) -> Command that is done when button is clicked. Work only with none argument functions
- image (optional) -> Instance of class ``UI.Image`` with image

---
---


## Ending

I think I have written every thing. Enjoy your usage!

