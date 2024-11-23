"""
Name: proxlu
Date: Oct 30, 2024

Description: This module contains all of the sprites used in "Minotaur Labyrinth" game, 
             including the Player, Stone, Countdown, GearPieces, GearTracker, HealthKeeper, 
             and the Minotaur. It imports the Pygame and Random module for use.
"""

import pygame, random

class Player(pygame.sprite.Sprite):
    """This class represents the Player Sprite, and inherits from the Sprite class."""
    def __init__(self, screen, maze_arrangement):
        """This method instantiates the Player class, and loads 4 sets of images for
        each animation cycle. It also sets many of the Player's attributes, such as 
        the direrction of the player, its animation state, the frame index of each
        animation cycle, the initial image of the player (Facing down), """
        pygame.sprite.Sprite.__init__(self)
    
        self.__walk_down = [pygame.image.load("./misc/PlayerImages/stand_face_down.png"), \
                            pygame.image.load("./misc/PlayerImages/walk1_face_down.png"), \
                            pygame.image.load("./misc/PlayerImages/stand_face_down.png"), \
                            pygame.image.load("./misc/PlayerImages/walk2_face_down.png"), \
                            pygame.image.load("./misc/PlayerImages/stand_face_down.png")]
        
        self.__walk_up = [pygame.image.load("./misc/PlayerImages/stand_face_up.png"), \
                          pygame.image.load("./misc/PlayerImages/walk1_face_up.png"), \
                          pygame.image.load("./misc/PlayerImages/stand_face_up.png"), \
                          pygame.image.load("./misc/PlayerImages/walk2_face_up.png"), \
                          pygame.image.load("./misc/PlayerImages/stand_face_up.png")]    
        
        self.__walk_right = [pygame.image.load("./misc/PlayerImages/stand_face_right.png"), \
                             pygame.image.load("./misc/PlayerImages/walk1_face_right.png"), \
                             pygame.image.load("./misc/PlayerImages/stand_face_right.png"), \
                             pygame.image.load("./misc/PlayerImages/walk2_face_right.png"), \
                             pygame.image.load("./misc/PlayerImages/stand_face_right.png")]
        
        self.__walk_left = [pygame.image.load("./misc/PlayerImages/stand_face_left.png"), \
                            pygame.image.load("./misc/PlayerImages/walk1_face_left.png"), \
                            pygame.image.load("./misc/PlayerImages/stand_face_left.png"), \
                            pygame.image.load("./misc/PlayerImages/walk2_face_left.png"), \
                            pygame.image.load("./misc/PlayerImages/stand_face_left.png")]
        
        self.image = self.__walk_down[0]
        self.rect = self.image.get_rect()
        
        # Set direction, current frame index, animation state, and 
        self.__direction = "DOWN"
        self.__frame_index = 0
        self.__animating = False
        self.__move_length = 0
        
        self.__maze_arrangement = maze_arrangement
        
        self.rect.x = 50
        self.rect.y = 50  
        
        self.__user_x = self.rect.x // 50
        self.__user_y = self.rect.y // 50        
        self.__x = self.rect.x
        self.__y = self.rect.y    
    
    def walk_down(self, sound):
        """This mutator function moves the Player one tile down. It checks if the tile
        below the Player is free and if the Player is currently in an animation cycle.
        It accepts sound, representing the walking sound effect, as a parameter."""
        
        # Checks if tile below Player is free, and if they are not in an animation cycle
        if (self.__maze_arrangement[self.__user_x][self.__user_y + 1] != 1) and not self.__animating:
            
            # Sets Player direction to down, animating state to true, moves the Player downwards
            # by one tile, and plays the walking sound effect
            self.__direction = "DOWN"
            self.__animating = True
            self.__user_y += 1
            sound.play()
        
    def walk_up(self, sound):
        """This mutator function moves the Player one tile up. It checks if the tile
        above the Player is free and if the Player is currently in an animation cycle.
        It accepts sound, representing the walking sound effect, as a parameter."""        
        
        # Checks if tile below Player is free, and if they are not in an animation cycle
        if (self.__maze_arrangement[self.__user_x][self.__user_y - 1] != 1) and not self.__animating:
            
            # Sets Player direction to up, animating state to true, moves the Player upwards
            # by one tile, and plays the walking sound effect            
            self.__direction = "UP"
            self.__animating = True
            self.__user_y -= 1
            sound.play()

    def walk_right(self, sound):
        """This mutator function moves the Player one tile right. It checks if the tile
        to the right of the Player is free and if the Player is currently in an animation cycle.
        It accepts sound, representing the walking sound effect, as a parameter."""      
        
        # Checks if tile to the right of the Player is free, and if they are not in an animation cycle
        if (self.__maze_arrangement[self.__user_x + 1][self.__user_y] != 1) and not self.__animating:
            
            # Sets Player direction to right, animating state to true, moves the Player to the
            # right by one tile, and plays the walking sound effect              
            self.__direction = "RIGHT"
            self.__animating = True
            self.__user_x += 1
            sound.play()
    
    def walk_left(self, sound):
        """This mutator function moves the Player one tile left. It checks if the tile
        to the left of the Player is free and if the Player is currently in an animation cycle.
        It accepts sound, representing the walking sound effect, as a parameter."""              
        
        # Checks if tile to the left of the Player is free, and if they are not in an animation cycle
        if (self.__maze_arrangement[self.__user_x - 1][self.__user_y] != 1) and not self.__animating:
            
            # Sets Player direction to left, animating state to true, moves the Player to the
            # left by one tile, and plays the walking sound effect                
            self.__direction = "LEFT"
            self.__animating = True
            self.__user_x -= 1
            sound.play()

    def respawn_player(self):
        """This mutator method resets the Player's sprite position to its original
        spawn point in the maze, in the top-left corner tile."""
        self.rect.x = 50
        self.rect.y = 50
        
        # Specifies the Player's spawnpoint as maze_arrangement[1][1], representing
        # the tile in the top-left corner of the maze
        self.__user_x = 1
        self.__user_y = 1
    
    def get_x_position(self):
        """This accessor method returns an integer representing the Player's 
        x position in terms of pixels."""
        return self.rect.x
    
    def get_y_position(self):
        """This accessor method returns an integer representing the Player's 
        y position in terms of pixels."""        
        return self.rect.y
    
    def get_center_position(self):
        return self.rect.center
        
    def set_position(self, x_position, y_position):
        """This mutator method sets the NEW rect cordinates for the Player's sprite
        acccording to their tile position in the maze. It accepts x_position, an integer
        representing the Player's x tile, and y_position, an integer representing
        the Player's y tile, as parameters. It returns the new rect.x and rect.y 
        of the Player."""
        
        # Checks if the tile position is within the x boundaries of the maze
        if x_position >= 0 and x_position <= 18: 
            
            # The new self.rect.x is determined by multiplying the tile value by 50,
            # representing the pixel position of the sprite, and adding 14 as a slight
            # offset to center the image more appropriately on the tile
            self.rect.x = (x_position*50) + 14
            
        # Checks if the tile position is within the y boundaries of the maze    
        if y_position >= 0 and y_position <= 18:
        
            # The new self.rect.y is determined by multiplying the tile value by 50,
            # representing the pixel position of the sprite, and adding 3 as a slight
            # offset to center the image more appropriately on the tile           
            self.rect.y = (y_position*50) + 3

        # Returns the updated self.rect.x and self.rect.y to the caller
        return self.rect.x, self.rect.y

    def animate(self, direction):
        if direction == "DOWN" and self.__move_length < 10:
            self.image = self.__walk_down[self.__frame_index // 2]
            self.__y += 5 
        if direction == "UP" and self.__move_length < 10:
            self.image = self.__walk_up[self.__frame_index // 2]
            self.__y -= 5
        if direction == "LEFT" and self.__move_length < 10:
            self.image = self.__walk_left[self.__frame_index // 2]
            self.__x -= 5
        if direction == "RIGHT" and self.__move_length < 10:
            self.image = self.__walk_right[self.__frame_index // 2]
            self.__x += 5 
     
        self.__move_length += 1
        self.__frame_index += 1
        self.__frame_index %= 10

        if self.__move_length >= 10:
            self.__animating = False
            self.__move_length = 0           

    def update(self):
        if self.__animating:
            self.animate(self.__direction)
            self.rect = self.image.get_rect()
            self.rect.x = self.__x
            self.rect.y = self.__y
        else:
            self.set_position(self.__user_x, self.__user_y)
            self.__x, self.__y = self.rect.x, self.rect.y   
            
class VisionLimiter(pygame.sprite.Sprite):
    
    def __init__(self, screen, vision_limiter):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = vision_limiter
        self.rect = self.image.get_rect()
        self.__center = 0
        
    def set_center(self, player_center_position):
        self.__center = player_center_position
        
    def update(self):
        self.rect.center = self.__center
         
class NoVisionLimiter(pygame.sprite.Sprite):
    
    def __init__(self, screen, no_vision_limiter):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = no_vision_limiter
        self.rect = self.image.get_rect()
        self.__center = 0
        
    def set_center(self, player_center_position):
        self.__center = player_center_position
        
    def update(self):
        self.rect.center = self.__center

class Stone(pygame.sprite.Sprite):
    """This class inherits from the Sprite class and represents each
    wall block that composes the maze."""
    
    def __init__(self, stone_type, x, y, can_disappear):
        """This method initializes the Stone class, and sets unique attributes for the 
        stone_type, the ability of a stone to disappear, and the x and y positions, in 
        pixels, of a stone object. It accepts the stone_type, x position of the brick, 
        y position of the brick, and can_disappear as parameters."""
        
        pygame.sprite.Sprite.__init__(self)
        
        # A flag that indicates whether or not one of the maze_walls has the ability
        # to be killed under certain conditions
        self.__can_disappear = can_disappear
        
        # Following suit with the countdown timer, this sets a timer of 450, 
        # representing 15 seconds in total
        self.__timer = 450
        
        self.__stone_type = stone_type
        
        # Decides what image to use depending on the randomly generated
        # stone_type integer
        if self.__stone_type == 0:
            self.image = pygame.image.load("./misc/MiscImages/stone_brick.jpg")
        elif self.__stone_type == 1:
            self.image = pygame.image.load("./misc/MiscImages/cobble_stone.png")
        else:
            self.image = pygame.image.load("./misc/MiscImages/moss_stone.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y  
        
    def update(self):
        """This method updates the local timer of the Stone Class, and is used to 
        kill specific walls after 15 seconds have passed in order to release the Minotaur.
        It is important to note that this only VISUALLY kills the sprite - it does not
        allow the Player or Minotaur to freely pass through that tile."""
        
        # The timer is decreased by one per iteration of the game loop (30 times a second)
        self.__timer -= 1
        
        # If a maze_wall block is able to be killed, specified by the flag above,
        # then the block will be killed after 15 seconds
        if self.__can_disappear:
            if self.__timer <= 0:
                self.kill()   
        
class GearPieces(pygame.sprite.Sprite):
    def __init__(self, gear_num, x, y):
        """This method initializes the GearPieces class and sets
        the """
        pygame.sprite.Sprite.__init__(self)
        
        self.__gear_num = gear_num
        
        if self.__gear_num == 0:
            self.image = pygame.image.load("./misc/MiscImages/diamondchestplate.png")
        elif self.__gear_num == 1:
            self.image = pygame.image.load("./misc/MiscImages/diamondhelmet.png")
        elif self.__gear_num == 2:
            self.image = pygame.image.load("./misc/MiscImages/diamondsword.png")
        elif self.__gear_num == 3:
            self.image = pygame.image.load("./misc/MiscImages/diamondboots.png")
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Countdown(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.__time = 15
        self.__font1 = pygame.font.Font("./misc/Fonts/DIOGENES.ttf", 40)
        self.__font2 = pygame.font.Font("./misc/Fonts/greekhouse.ttf", 18)
        
    def decrease_time(self, time):
        """This mutator method accepts time as a parameter, and updates the value
        of self.__time to equal time."""
        self.__time = time
        
    def get_time(self):
        """This accessor method returns an integer representing the countdown time."""
        return self.__time 
        
    def update(self):
        """This method updates the countdown message, renders the font, and initializes 
        the rect attributes for the Countdown class. The countdown message displayed 
        is dependent on the time left."""
        
        # If the countdown timer has not yet hit 0
        if self.__time > 0:
            
            # Displays the grace period time in seconds
            countdown_message = str(self.__time)
            self.image = self.__font1.render(countdown_message, 1, (255, 255, 255))
            self.rect = self.image.get_rect()
            
            # Message is positioned in the center of the screen near the top
            self.rect.centerx, self.rect.centery = 400, 30
        
        # If the countdown timer has hit 0
        elif self.__time <= 0:
            
            # Notifies the Player that the Minotaur has escaped from his contained area
            release_message = "he has been released"
            self.image = self.__font2.render(release_message, 1, (255, 255, 255))
            self.rect = self.image.get_rect()
            
            # Message is positioned in the center of the screen near the top
            self.rect.centerx, self.rect.centery = 400, 30
             
class GearTracker(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.__font = pygame.font.Font("./misc/Fonts/geek.ttf", 22)
        self.__num_gear_collected = 0
        
    def add_gear_piece(self):
        """This mutator method increases the number of collected gear pieces by 1."""
        self.__num_gear_collected += 1
        
    def get_num_gear(self):
        """This accessor method returns an integer representing the number of gear
        pieces collected by the Player."""
        return self.__num_gear_collected
        
    def update(self):
        """This method updates the gear collected message, renders the font, and initializes the rect attributes for the GearTracker class."""
        gear_message = "GEAR COLLECTED: %d" % \
            self.__num_gear_collected + "/4"
        self.image = self.__font.render(gear_message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        
        # This message is positioned in the top-left corner of the screen
        self.rect.topleft = (10, 10)
       
class HealthKeeper(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        
        self.image_heart = pygame.image.load("./misc/MiscImages/heart.png")
        self.image = pygame.Surface((150, 50))
        self.rect = self.image.get_rect()
        self.__num_lives = 3
        
    def lose_life(self):
        """This mutator method subtracts one from the total number of Player lives'."""
        self.__num_lives -= 1
        
    def get_lives(self):
        """This accessor method returns an integer representing the number of lives
        the Player has."""
        return self.__num_lives
        
    def update(self):
        """This method visually updates the number of lives the player has, and 
        initializes the rect attributes for the HealthKeeper class."""
        
        # Creates a surface on which 3 hearts can be blitted
        self.image = pygame.Surface((150, 50))
        
        # Blits each of the remaining Player lives' onto this surface
        for life in range(self.__num_lives): 
            
            # Each heart image is 50x50 pixels, and so they are blitted 50 pixels apart
            self.image.blit(self.image_heart, (life*50, 0))
            
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        
        # The surface's rect is set in the top-right corner of the screen
        self.rect.x = 650
        self.rect.y = 0

class Minotaur(pygame.sprite.Sprite):
    def __init__(self, screen, maze_arrangement):
        pygame.sprite.Sprite.__init__(self)
        
        self.__walk_down = [pygame.image.load("./misc/MinotaurImages/minotaur_stand_down.png"), \
                            pygame.image.load("./misc/MinotaurImages/minotaur_walk1_down.png"), \
                            pygame.image.load("./misc/MinotaurImages/minotaur_stand_down.png"), \
                            pygame.image.load("./misc/MinotaurImages/minotaur_walk2_down.png"), \
                            pygame.image.load("./misc/MinotaurImages/minotaur_stand_down.png")]
        
        self.__walk_up = [pygame.image.load("./misc/MinotaurImages/minotaur_stand_up.png"), \
                          pygame.image.load("./misc/MinotaurImages/minotaur_walk1_up.png"), \
                          pygame.image.load("./misc/MinotaurImages/minotaur_stand_up.png"), \
                          pygame.image.load("./misc/MinotaurImages/minotaur_walk2_up.png"), \
                          pygame.image.load("./misc/MinotaurImages/minotaur_stand_up.png")]    
        
        self.__walk_right = [pygame.image.load("./misc/MinotaurImages/minotaur_stand_right.png"), \
                             pygame.image.load("./misc/MinotaurImages/minotaur_walk1_right.png"), \
                             pygame.image.load("./misc/MinotaurImages/minotaur_stand_right.png"), \
                             pygame.image.load("./misc/MinotaurImages/minotaur_walk2_right.png"), \
                             pygame.image.load("./misc/MinotaurImages/minotaur_stand_right.png")]
        
        self.__walk_left = [pygame.image.load("./misc/MinotaurImages/minotaur_stand_left.png"), \
                            pygame.image.load("./misc/MinotaurImages/minotaur_walk1_left.png"), \
                            pygame.image.load("./misc/MinotaurImages/minotaur_stand_left.png"), \
                            pygame.image.load("./misc/MinotaurImages/minotaur_walk2_left.png"), \
                            pygame.image.load("./misc/MinotaurImages/minotaur_stand_left.png")]
        
        self.image = self.__walk_down[0]
        self.rect = self.image.get_rect()
        
        self.__direction = "DOWN"
        self.__frame_index = 0
        self.__animating = False
        self.__move_length = 0
        
        self.__maze_arrangement = maze_arrangement
        
        self.rect.x = 350
        self.rect.y = 400 
        
        self.__minotaur_x = self.rect.x // 50
        self.__minotaur_y = self.rect.y // 50        
        self.__x = self.rect.x
        self.__y = self.rect.y   
    
    # Determines if the Minotaur is within reasonable range of player
    def is_close(self, player_x, player_y):
        """This method determines if the Minotaur is within a reasonable range
        of the player, and returns a string specifying the distance proximity.
        It accepts the player's rect.x and rect.y values as parameters. If the 
        Minotaur is NOT within a reasonable range, this function returns False."""
        x_distance = (self.__minotaur_x - (player_x // 50))
        y_distance = (self.__minotaur_y - (player_y // 50))
        
        # If the Minotaur is a distance of 3 to 4 tiles away from the player
        if 3 < ((abs(x_distance)**2) + (abs(y_distance)**2))**0.5 <= 4:
            return "far"
        
        # If the Minotaur is a distance of 2 to 3 tiles away from the player
        elif 2 < ((abs(x_distance)**2) + (abs(y_distance)**2))**0.5 <= 3:
            return "medium"
        
        # If the Minotaur is a distance of 1 to 2 tiles away from the player
        elif 1 < ((abs(x_distance)**2) + (abs(y_distance)**2))**0.5 <= 2:
            return "close"
        
        # If the Minotaur is NOT within a reasonable range, returns false
        # i.e. The player is outside the audible range of the Minotaur
        else:
            return False
        
    def follow_player(self, player_x, player_y):
        """This method determines the movement of the Minotaur by using simple pathing
        based off the Player's position. This method accepts the Player's rect.x and 
        rect.y as parameters, and returns nothing."""
        
        # Determines the horizontal and vertical distance between the Player and the
        # Minotaur, converting them into that are measured by the tiles (Dividing the
        # difference by 50 turns each of these values into integers that represent tile
        # distances)
        x_distance = (self.rect.x - player_x) // 50 
        y_distance = (self.rect.y - player_y) // 50 
    
        # If the Minotaur is NOT on the same tile as the Player i.e. touching them
        if x_distance != 0 and y_distance != 0:
        
            # Check if the Player is situated ABOVE the Minotaur and if the Minotaur is
            # not currently animating
            if y_distance > 0 and not self.__animating:
                
                # If the tile above the Minotaur is free, then set direction as up, set
                # animating to True, and change the minotaur_y (Tile space)
                if (self.__maze_arrangement[self.__minotaur_x][self.__minotaur_y - 1] != 1):
                    self.__direction = "UP"
                    self.__animating = True
                    self.__minotaur_y -= 1
                
                # If the tile above the Minotaur is NOT free, and the tile to the left
                # of the Minotaur IS free, then set direction to left, set animating
                # to True, and change the minotaur_x (Tile space) accordingly
                elif self.__maze_arrangement[self.__minotaur_x][self.__minotaur_y - 1] and \
                    (self.__maze_arrangement[self.__minotaur_x - 1][self.__minotaur_y]  != 1) and \
                     player_x < self.rect.x:
                    self.__direction = "LEFT"
                    self.__animating = True
                    self.__minotaur_x -= 1
                
                # If the tile above the Minotaur is NOT free, and the tile to the RIGHT
                # of the Minotaur IS free, then set direction to right, set animating
                # to True, and change the minotaur_x (Tile space) accordingly              
                elif self.__maze_arrangement[self.__minotaur_x][self.__minotaur_y - 1] and \
                    (self.__maze_arrangement[self.__minotaur_x + 1][self.__minotaur_y] != 1) and \
                     player_x > self.rect.x:
                    self.__direction = "RIGHT"
                    self.__animating = True
                    self.__minotaur_x += 1                
    
            # Check if the Player is situated BELOW the Minotaur and if the Minotaur is
            # not currently animating 
            if y_distance < 0 and not self.__animating:
                
                # If the tile below the Minotaur is free, then set direction as down, set
                # animating to True, and change the minotaur_y (Tile space)                
                if (self.__maze_arrangement[self.__minotaur_x][self.__minotaur_y + 1] != 1):
                    self.__direction = "DOWN"
                    self.__animating = True
                    self.__minotaur_y += 1
                
                # If the tile below the Minotaur is NOT free, and the tile to the RIGHT
                # of the Minotaur IS free, then set direction to right, set animating
                # to True, and change the minotaur_x (Tile space) accordingly                
                elif self.__maze_arrangement[self.__minotaur_x][self.__minotaur_y + 1] and \
                    (self.__maze_arrangement[self.__minotaur_x + 1][self.__minotaur_y] != 1) and \
                     player_x > self.rect.x:
                    self.__direction = "RIGHT"
                    self.__animating = True
                    self.__minotaur_x += 1
                
                # If the tile below the Minotaur is NOT free, and the tile to the LEFT
                # of the Minotaur IS free, then set direction to left, set animating
                # to True, and change the minotaur_x (Tile space) accordingly                              
                elif self.__maze_arrangement[self.__minotaur_x][self.__minotaur_y + 1] and \
                    (self.__maze_arrangement[self.__minotaur_x - 1][self.__minotaur_y] != 1) and \
                     player_x < self.rect.x:
                    self.__direction = "LEFT"
                    self.__animating = True
                    self.__minotaur_x -= 1                
 
            # Check if the Player is situated RIGHT of the Minotaur and if the Minotaur is
            # not currently animating   
            if x_distance < 0  and not self.__animating:
                
                # If the tile to the right of the Minotaur is free, then set direction as 
                # right, set animating to True, and change the minotaur_x  (Tile space)                        
                if (self.__maze_arrangement[self.__minotaur_x + 1][self.__minotaur_y] != 1):
                    self.__direction = "RIGHT"
                    self.__animating = True
                    self.__minotaur_x += 1     
                
                # If the tile to the right of the Minotaur is NOT free, and the tile ABOVE
                # the Minotaur IS free, then set direction to up, set animating
                # to True, and change the minotaur_y (Tile space) accordingly                    
                elif self.__maze_arrangement[self.__minotaur_x + 1][self.__minotaur_y] and \
                    (self.__maze_arrangement[self.__minotaur_x][self.__minotaur_y - 1] != 1) and \
                     player_y < self.rect.y:
                    self.__direction = "UP"
                    self.__animating = True
                    self.__minotaur_y -= 1
                    
                # If the tile to the right of the Minotaur is NOT free, and the tile BELOW
                # the Minotaur IS free, then set direction to down, set animating
                # to True, and change the minotaur_y (Tile space) accordingly                        
                elif self.__maze_arrangement[self.__minotaur_x + 1][self.__minotaur_y] and \
                    (self.__maze_arrangement[self.__minotaur_x][self.__minotaur_y + 1] != 1) and \
                     player_y > self.rect.y:
                    self.__direction = "DOWN"
                    self.__animating = True
                    self.__minotaur_y += 1            
    
            # Check if the Player is situated LEFT of the Minotaur and if the Minotaur is
            # not currently animating      
            if x_distance > 0  and not self.__animating:
                
                # If the tile to the LEFT of the Minotaur is free, then set direction as 
                # left, set animating to True, and change the minotaur_x (Tile space)                
                if (self.__maze_arrangement[self.__minotaur_x - 1][self.__minotaur_y] != 1):
                    self.__direction = "LEFT"
                    self.__animating = True
                    self.__minotaur_x -= 1
                
                # If the tile to the LEFT of the Minotaur is NOT free, and the tile BELOW
                # the Minotaur IS free, then set direction to down, set animating
                # to True, and change the minotaur_y (Tile space) accordingly                 
                elif self.__maze_arrangement[self.__minotaur_x - 1][self.__minotaur_y] and \
                    (self.__maze_arrangement[self.__minotaur_x][self.__minotaur_y + 1] != 1) and \
                     player_y > self.rect.y:
                    self.__direction = "DOWN"
                    self.__animating = True
                    self.__minotaur_y += 1
                
                # If the tile to the LEFT of the Minotaur is NOT free, and the tile ABOVE
                # the Minotaur IS free, then set direction to up, set animating
                # to True, and change the minotaur_y (Tile space) accordingly                         
                elif self.__maze_arrangement[self.__minotaur_x - 1][self.__minotaur_y] and \
                    (self.__maze_arrangement[self.__minotaur_x][self.__minotaur_y - 1] != 1) and \
                     player_y > self.rect.y:
                    self.__direction = "UP"
                    self.__animating = True
                    self.__minotaur_y -= 1
        
    def reset_position(self):
        """This mutator method resets the Minotaur's sprite position to its original
        spawn point in the maze, in the center chamber."""        
        self.rect.x = 400
        self.rect.y = 400
        
        # Specifies the Player's spawnpoint as maze_arrangement[8][8], representing
        # the tile in the center of the maze       
        self.__minotaur_x = 8
        self.__minotaur_y = 8
        
    def set_position(self, x_position, y_position):
        """This mutator method sets the NEW rect cordinates for the Minotaur's sprite
        acccording to its tile position in the maze. It accepts x_position, an integer
        representing the Minotaur's x tile, and y_position, an integer representing
        the Minotaur's y tile, as parameters. It returns the new rect.x and rect.y 
        of the Minotaur."""        
        
        # Checks if the tile position is within the x boundaries of the maze
        if x_position >= 0 and x_position <= 18:  
            
            # The new self.rect.x is determined by multiplying the tile value by 50,
            # representing the pixel position of the sprite, and adding 3 as a slight
            # offset to center the image more appropriately on the tile            
            self.rect.x = (x_position*50) + 3
            
        # Checks if the tile position is within the y boundaries of the maze      
        if y_position >= 0 and y_position <= 18:
            
            # The new self.rect.y is determined by multiplying the tile value by 50,
            # representing the pixel position of the sprite, and adding 3 as a slight
            # offset to center the image more appropriately on the tile              
            self.rect.y = (y_position*50)
        
        # Returns the updated self.rect.x and self.rect.y to the caller
        return self.rect.x, self.rect.y

    def animate(self, direction):
        if direction == "DOWN" and self.__move_length < 10:
            self.image = self.__walk_down[self.__frame_index // 2]
            self.__y += 5 
        if direction == "UP" and self.__move_length < 10:
            self.image = self.__walk_up[self.__frame_index // 2]
            self.__y -= 5
        if direction == "LEFT" and self.__move_length < 10:
            self.image = self.__walk_left[self.__frame_index // 2]
            self.__x -= 5
        if direction == "RIGHT" and self.__move_length < 10:
            self.image = self.__walk_right[self.__frame_index // 2]
            self.__x += 5 
     
        self.__move_length += 1
        self.__frame_index += 1
        self.__frame_index %= 10

        if self.__move_length >= 10:
            self.__animating = False
            self.__move_length = 0           

    def update(self):
        if self.__animating:
            self.animate(self.__direction)
            self.rect = self.image.get_rect()
            self.rect.x = self.__x
            self.rect.y = self.__y
        else:
            self.set_position(self.__minotaur_x, self.__minotaur_y)
            self.__x, self.__y = self.rect.x, self.rect.y       
