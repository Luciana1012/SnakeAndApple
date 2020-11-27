
#THIS IS A SUPPORT FILE FOR THE MAIN GAME

from tkinter import *
import random
import time
import numpy as np
from PIL import ImageTk,Image

import support #importing the support.py file!!!

# Define useful parameters
size_of_board = 600 #this is the pixel size of the game, not the actual squares in the game
rows = 10
cols = 10
DELAY = 100
snake_initial_length = 3
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 2
RED_COLOR = "#EE4035"
BLUE_COLOR = "#0492CF"
Green_color = "#7BC043"

BLUE_COLOR_LIGHT = '#67B0CF'
RED_COLOR_LIGHT = '#EE7E77'

class SnakeAndApple(support.SnakeSupport):
#---------------------------------
#Initialization Functions:
#---------------------------------

    def __init__(self):
        super().__init__()
        self.window = Tk()
        self.window.title("Snake-and-Apple")
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)	
        self.canvas.pack()

#Input from user in form of clicks and keyboard
        self.window.bind("<Key>", self.key_input)
        self.window.bind("<Button-1>", self.mouse_input)
        self.play_again()
        self.begin = False

    def mainloop(self):
        while True:
            self.window.update()
            if self.begin:
                if not self.crashed:
                    self.window.after(DELAY, self.update_snake(self.last_key))
                else:
                    self.begin = False
                    self.display_gameover()
    def mouse_input(self, event):
        self.play_again()
    
    def initialize_snake(self):
        self.snake = []
        self.crashed = False
        self.snake_heading = "Right"
        self.last_key = self.snake_heading
        #forbidden_actions --> snake cannot do a 180 degree turn
        #can only do a 90 degree turn
        self.forbidden_actions = {}
        self.forbidden_actions["Right"] = "Left"
        self.forbidden_actions["Left"] = "Right"
        self.forbidden_actions["Up"] = "Down"
        self.forbidden_actions["Down"] = "Up"
        self.snake_objects = []
        for i in range(snake_initial_length):
            self.snake.append((i, 0))

    def check_if_key_valid(self, key):
        valid_keys = ["Up", "Down", "Left", "Right"]
        if key in valid_keys and self.forbidden_actions[self.snake_heading] != key:
            return True
        else:
            return False
    
#Logical Functions:
#The modules required to carry out game logic
#---------

    def update_snake(self, key):
    # Check if it hit the wall or its own body
        #self.snake --> [(0,0),(1,0),(2,0)]
        tail = self.snake[0] #---> (0,0) tuple
        head = self.snake[-1] #--> (2,0) 
        if tail != self.old_apple_cell:
            self.snake.pop(0)
        if key == "Left":
            self.snake.append((head[0] - 1, head[1])) #new head --> (1,0)
        elif key == "Right":
            self.snake.append((head[0] + 1, head[1]))
        elif key == "Up":
            self.snake.append((head[0], head[1] - 1))
        elif key == "Down":
            self.snake.append((head[0], head[1] + 1))

        head = self.snake[-1]
        if (
            head[0] > cols -1
            or head[0] < 0
            or head[1] > rows - 1
            or head[1] < 0
            or len(set(self.snake)) != len(self.snake)
            ):
    
                #Hit the wall / Hit on body
            self.crashed = True
        elif self.apple_cell == head:
            # Got the apple
            self.old_apple_cell == self.apple_cell
            self.canvas.delete(self.apple_obj)
            self.place_apple()
            self.display_snake()
        else:
            self.snake_heading = key
            self.display_snake()

game_instance = SnakeAndApple()
game_instance.mainloop()