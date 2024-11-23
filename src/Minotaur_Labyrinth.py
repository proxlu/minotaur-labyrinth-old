"""
Name: proxlu
Date: Oct 30, 2024

Description: "Minotaur Labyrinth" is a survival-maze game in which the player, Theseus,
              must survive the trials of the Labyrinth by finding and killing the Minotaur.
              
              The Player is controlled using the arrow keys, and the Minotaur is controlled
              by a very simple pathing AI.
              
              In order to win the game, the player must collect all four pieces of 
              gear, after which they must find the Minotaur and walk into him, 
              killing him and allowing the player to ultimately escape the maze.
              
              If the player is caught by the Minotaur before obtaining all four pieces
              of gear, they will lose a life and respawn at their original spawn point within the maze. 
              If the player loses all 3 lives, they lose the game.
              
              The player must rely on the sounds made by the Minotaur through 
              proximity, to determine where he is located within the maze. 
"""

# I - IMPORT AND INITIALIZE ====================================================
import pygame, src.labyrinthSprites, random

pygame.init()
pygame.mixer.init()

def generate_maze(maze_wall, maze_arrangement):
 
    for row in range(len(maze_arrangement)):
        for col in range(len(maze_arrangement[row])):
            if maze_arrangement[row][col] == 1: 
                if (row == 7 and col == 6) or (row == 6 and col == 8) or \
                   (row == 8 and col == 9):
                    stone = src.labyrinthSprites.Stone(random.randint(0,3), row*50, col*50, True)
                    maze_wall.add(stone)
                else:
                    stone = src.labyrinthSprites.Stone(random.randint(0,3), row*50, col*50, False)
                    maze_wall.add(stone)                    

def hide_gear_pieces(gear_powerups, maze_arrangement):
    
    for gear_item in range(4):
        valid_place = False
        
        while not valid_place:
            
            row = random.randint(0, len(maze_arrangement) - 1)
            col = random.randint(0, len(maze_arrangement[:]) - 1)
        
            # Ensuring the gear pieces do not spawn in the Minotaur's spawn point
            if (row == 7 or row == 8) and (col == 7 or col == 8):
                valid_place = False
            
            # Ensuring the gear pieces do not spawn on the player's spawn point    
            elif (row == 1 or col == 1):
                valid_place = False
                
            # Ensuring the gear pieces do not spawn on a tile where a gear piece already exists
            elif maze_arrangement[row][col] == 2:
                valid_place = False
            
            # Ensuring the gear pieces only spawn on a valid pathway block
            elif maze_arrangement[row][col] == 0:
                maze_arrangement[row][col] = 2
                powerup = src.labyrinthSprites.GearPieces(gear_item, row*50, col*50)
                gear_powerups.add(powerup)
                valid_place = True                

def game_instructions(screen):
    # DISPLAY ==================================================================
    background = pygame.image.load("./misc/MiscImages/Introduction_Screen.jpg")
    screen.blit(background, (0, 0))    
    
    # ENTITIES ================================================================= 
    start_game_sound = pygame.mixer.Sound("./misc/Sounds/metal_gong.wav")
    start_game_sound.set_volume(0.7)
    
    # ASSIGN ===================================================================
    clock = pygame.time.Clock()
    keep_going = True
    player_hit = False

    # LOOP =====================================================================
    while keep_going:
        
        # TIME =================================================================
        clock.tick(30)
        
        # EVENT HANDLING =======================================================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game_sound.play()
                    keep_going = False
                    return True, 1
                
        # REFRESH SCREEN ===========================================================
        pygame.display.flip()

def game(screen):
    """This function defines the mainline logic for "The Labyrinth" Game"""
    
    # DISPLAY ==================================================================
    background = pygame.image.load("./misc/MiscImages/background.jpg")
    background = background.convert()
    screen.blit(background, (0, 0))
  
    # ENTITIES ================================================================= 
    
    # Set the variable indicating the arrangement of the maze
    # X's represent walls
    # O's represent the pathway blocks on which the minotaur and player can traverse
    X, O = 1, 0
    maze_arrangement = [[X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X], \
                        [X,O,X,X,O,O,O,O,O,O,X,X,O,O,O,X], \
                        [X,O,O,O,O,X,X,X,O,X,X,X,X,X,O,X], \
                        [X,O,X,X,O,X,O,O,O,O,O,O,O,O,O,X], \
                        [X,O,O,O,O,X,O,X,O,X,X,O,X,X,X,X], \
                        [X,O,X,X,O,O,O,X,O,X,X,O,O,O,O,X], \
                        [X,O,X,X,X,X,X,X,X,X,X,X,X,X,O,X], \
                        [X,O,O,O,O,O,X,O,O,X,X,X,O,O,O,X], \
                        [X,O,X,O,X,X,X,O,O,X,O,O,O,X,O,X], \
                        [X,O,X,O,O,O,X,X,X,X,O,X,O,X,O,X], \
                        [X,O,X,X,X,O,X,X,O,X,X,X,O,X,O,X], \
                        [X,O,O,O,O,O,O,O,O,O,O,O,O,X,O,X], \
                        [X,O,X,O,X,O,X,O,X,X,X,O,O,O,O,X], \
                        [X,X,X,O,X,O,X,O,O,O,X,X,X,X,O,X], \
                        [X,O,O,O,X,O,O,O,X,O,X,O,O,O,O,X], \
                        [X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X]] 
    
    # Any position occupied by a hidden_gear_piece will be equal to 2
    hidden_gear_piece = 2
        
    # Music and Sound Effects
    
    pygame.mixer.music.load("./misc/Sounds/eerie_music.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1) 
    
    # The Minotaur's growl when his distance is "far" from the player
    far_minotaur_growl = pygame.mixer.Sound("./misc/Sounds/monster_snarl.wav")
    far_minotaur_growl.set_volume(0.1)

    # Light Click
    click = pygame.mixer.Sound("./misc/Sounds/click.wav")
    click.set_volume(0.5)
    shock = pygame.mixer.Sound("./misc/Sounds/shock.wav")
    shock.set_volume(0.5)
    # The Minotaur's growl when his distance is "somewhat far" from the player
    med_minotaur_growl = pygame.mixer.Sound("./misc/Sounds/monster_snarl.wav")
    med_minotaur_growl.set_volume(0.25) 
    
    # The Minotaur's growl when his distance is "close" to the player
    close_minotaur_growl = pygame.mixer.Sound("./misc/Sounds/monster_snarl.wav")
    close_minotaur_growl.set_volume(0.5)       
    
    equip_gear_sound = pygame.mixer.Sound("./misc/Sounds/sword_clash.wav")
    equip_gear_sound.set_volume(0.7)
    
    minotaur_death_sound = pygame.mixer.Sound("./misc/Sounds/minotaur_death.wav")
    minotaur_death_sound.set_volume(1.0)
    
    minotaur_spawn_sound = pygame.mixer.Sound("./misc/Sounds/metal_gong.wav")
    minotaur_spawn_sound.set_volume(1.0)
    
    player_death_sound = pygame.mixer.Sound("./misc/Sounds/player_death.wav")
    player_death_sound.set_volume(0.8)
    
    player_walking_sound = pygame.mixer.Sound("./misc/Sounds/player_walking.wav")
    player_walking_sound.set_volume(0.5)
    
    # The sound played when the player collects all four pieces of gear
    all_gear_sound = pygame.mixer.Sound("./misc/Sounds/player_full_gear.wav")
    all_gear_sound.set_volume(0.8)

    # Images
    
    game_over_message = pygame.image.load("./misc/MiscImages/Game_Over_Screen.jpg")
    
    vision_space = pygame.image.load("./misc/MiscImages/vision_limiter.png")
    vision_off = pygame.image.load("./misc/MiscImages/vision_limiter_off.png")

    player = src.labyrinthSprites.Player(screen, maze_arrangement)
    minotaur = src.labyrinthSprites.Minotaur(screen, maze_arrangement)
    visible_area = src.labyrinthSprites.VisionLimiter(screen, vision_space)
    visible_off = src.labyrinthSprites.NoVisionLimiter(screen, vision_off)
    maze_wall = pygame.sprite.Group()
    gear_powerups = pygame.sprite.Group()
    
    generate_maze(maze_wall, maze_arrangement)
    hide_gear_pieces(gear_powerups, maze_arrangement)
    
    health_tracker = src.labyrinthSprites.HealthKeeper(screen)
    gear_tracker = src.labyrinthSprites.GearTracker()
    countdown = src.labyrinthSprites.Countdown()
    
    allSprites = pygame.sprite.OrderedUpdates(maze_wall, gear_powerups, minotaur, player, visible_area)
    allSprites2 = pygame.sprite.OrderedUpdates(gear_tracker, health_tracker, countdown)
    
    # ASSIGN ===================================================================
    clock = pygame.time.Clock()
    keep_going = True 
    grace_period_countdown = 15
    time_tracker = 0
    
    growl_sound_counter = 0
    
    pygame.mouse.set_visible(False)
    
    # LOOP =====================================================================
    def toggle_light(light_state):
        """Alterna o estado da lanterna"""
        return not light_state

    # Inicializa o estado da lanterna
    light_state = False
    movement_cooldown = 0  # Tempo restante para permitir o próximo movimento
    movement_delay = 15
    random_chance = 100
    while keep_going:
         
        # TIME =================================================================
        clock.tick(30) 
    
        # EVENT HANDLING =======================================================
        if movement_cooldown > 0:
            movement_cooldown -= 1
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                keep_going = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Alterna o estado da lanterna
                    light_state = toggle_light(light_state)
                    click.play()

        # 
        keys = pygame.key.get_pressed()  # Obtém o estado de todas as teclas
        if movement_cooldown == 0:
            if keys[pygame.K_DOWN]:  # Se a tecla para baixo estiver pressionada
                player.walk_down(player_walking_sound)  # Mova o jogador para baixo
                movement_cooldown = movement_delay
            if keys[pygame.K_UP]:  # Se a tecla para cima estiver pressionada
                player.walk_up(player_walking_sound)  # Mova o jogador para cima
                movement_cooldown = movement_delay
            if keys[pygame.K_RIGHT]:  # Se a tecla direita estiver pressionada
                player.walk_right(player_walking_sound)  # Mova o jogador para a direita
                movement_cooldown = movement_delay
            if keys[pygame.K_LEFT]:  # Se a tecla esquerda estiver pressionada
                player.walk_left(player_walking_sound)  # Mova o jogador para a esquerda
                movement_cooldown = movement_delay


        # If the player collides with any of the gear powerups,
        # the gear sprite is killed and the add_gear_piece() method is called
        if pygame.sprite.spritecollide(player, gear_powerups, False):
            for gear in pygame.sprite.spritecollide(player, gear_powerups, False):
                gear.kill()
                gear_tracker.add_gear_piece()
                equip_gear_sound.play()  # Toca o som de equipar

                # If all four pieces of gear have been collected, play the 
                # "I will find you" sound effect
                if gear_tracker.get_num_gear() == 4:
                    all_gear_sound.play()
                
                # Play the gear equip sound effect every time a gear piece is collected 
                #equip_gear_sound.play()
                
            # Check if the player collides with the minotaur
        if player.rect.colliderect(minotaur.rect):
                
                # Checks if the player has obtained all four pieces of gear
                # If no, then the player is unable to kill the minotaur
                # The player loses a life, and is respawned at their starting position
                # The Minotaur is repositioned in its original spawn point 
            if gear_tracker.get_num_gear() < 4 and not player_hit:
                player_death_sound.play()
                player.respawn_player()
                minotaur.reset_position()
                health_tracker.lose_life()
                player_hit = True
                # Checks if the player has obtained all four pieces of gear
                # If yes, then the player is able to kill the minotaur
                # The minotaur sprite is killed, and a death sound is played
            elif gear_tracker.get_num_gear() == 4:
                minotaur_death_sound.play()
                minotaur.kill()
                    
                    # End the game if the Minotaur has been killed and
                    # return True and 1 to game_ended, user_survived
                keep_going = False
                return True, 1
        else:
            player_hit = False  # Resetar a variável se não houver colisão

        if health_tracker.get_lives() <= 0:
            screen.blit(game_over_message, (0, 0))
            pygame.display.flip()
            pygame.time.wait(3000)
            keep_going = False
            return True, False
        
        # Checking the Proximity of the Minotaur to the Player in order to 
        # determine the volume of the minotaur's growl that will be played
        # If the proximity is returned as "close", and the counter is 0, the volume will be 0.5
        if minotaur.is_close(player.get_x_position(), player.get_y_position()) == "close" and growl_sound_counter == 0:
            close_minotaur_growl.play()
        
        # If the proximity is returned as "medium", and the counter is 0, the volume will be 0.3  
        elif minotaur.is_close(player.get_x_position(), player.get_y_position()) == "medium" and growl_sound_counter == 0:
            med_minotaur_growl.play()
                      
        # If the proximity is returned as "far", and the counter is 0, the volume will be 0.1
        elif minotaur.is_close(player.get_x_position(), player.get_y_position()) == "far" and growl_sound_counter == 0:
            far_minotaur_growl.play()
        
        # Increases the growl sound counter by 1 each iteration of the game loop (1 frame)    
        growl_sound_counter += 1
        
        # If the growl sound counter is equal to 120 (4 seconds of staying within a proximity
        # of the minotaur) or the Player exits the a valid proximity to the Minotaur, the
        # counter is set to 0
        if growl_sound_counter >= 120 or not minotaur.is_close(player.get_x_position(), player.get_y_position()):
            growl_sound_counter = 0
            
        # Increase the time tracker by 1 every iteration of the game loop
        time_tracker += 1
          
        # Reduces the grace period timer by one second every 30 frames
        grace_period_countdown = 15 - int(time_tracker/30)
        countdown.decrease_time(grace_period_countdown)
        
        # Checks if the countdown timer has hit 0
        if countdown.get_time() <= 0:
            
            # Specifies the same blocks that can be killed by the Flag can_disappear
            # and sets them to 0 in order to FUNCTIONALLY update them and make them
            # invisible - These blocks are the tiles surrounding the Minotaur within
            # His contained center space
            maze_arrangement[6][8] = 0
            maze_arrangement[7][6] = 0
            maze_arrangement[8][9] = 0
            
        # Call the Minotaur follow algorithm, that takes the player's x and y position
        minotaur.follow_player(player.get_x_position(), player.get_y_position())  
        
        visible_area.set_center(player.get_center_position())
                        
        # REFRESH SCREEN ====================ss===================================
        allSprites.clear(screen, background)
        allSprites2.clear(screen, background)
        allSprites.update()
        allSprites2.update()
        allSprites.draw(screen)
        
        if light_state:
            screen.blit(vision_off, (0, 0))  # Exibir a imagem preta cobrindo tudo
            
        if not light_state:  # Só apagar se a lanterna estiver ligada
            if random.randint(1, random_chance) == 1:
                light_state = True
                shock.play()
        
        allSprites2.draw(screen)
        
        # Atualizar a tela
        pygame.display.flip() 
    
    # Display a "Game Over" message and unhide the mouse pointer    
    #screen.blit(game_over_message, (0, 0))
    pygame.display.flip()
    pygame.mouse.set_visible(True) 
    #pygame.time.wait(2000)
        
    return False, 0

def save_user_name(screen):
    # DISPLAY ==================================================================
    background = pygame.image.load("./misc/MiscImages/Player_Name_Screen.jpg")
    screen.blit(background, (0, 0))    
        
    # ENTITIES ================================================================= 
    survivors_file = open("survivors.txt", "a")
    
    player_name = " "
    
    survivor_font = pygame.font.Font("./misc/Fonts/PressStart2P.ttf", 18)
    
    text = survivor_font.render(player_name, 1, (255, 255, 255))
    text_rect = text.get_rect()
    
    text_rect.center = (400, 400)
    
    message = player_name
    
    # ASSIGN ===================================================================
    clock = pygame.time.Clock()
    keep_going = True
    
    # LOOP =====================================================================
    while keep_going:
        
        # TIME =================================================================
        clock.tick(30)
        
        # EVENT HANDLING =======================================================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                return False, 0
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    player_name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                    screen.blit(background, (0, 0))
                elif event.key == pygame.K_RETURN:
                    survivors_file.write(str(player_name))
                    keepGoing = False
                
        # REFRESH SCREEN ===========================================================
        text = survivor_font.render(player_name, 1, (255, 255, 255))
        screen.blit(text, text_rect)
        pygame.display.flip()
        
    survivors_file.close()
    
def main():
    
    pygame.display.set_caption("Minotaur Labyrinth")
    screen = pygame.display.set_mode((800, 800))
    
    status = game_instructions(screen)
    
    if status:
        game_ended, user_survived = game(screen)
        
    if user_survived:
        save_user_name(screen)
    
    pygame.quit()

    main()
