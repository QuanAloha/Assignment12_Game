"""
Assignment12_Game Level One

Description of Level:
As a student, your first task of the day is to get to get your books from the Campus store. Watch out for the
food trucks because you can spend your book money on food.

The code in this file is written by Nathaniel Atwood and Megan Hays.This is a test.
Any distribution of this code without written consent is strictly prohibited.
"""

import sys, pygame, math

# Starter code for an avoider game. Written by David Johnson for CS 1400 University of Utah.

# Finished game authors:
# Megan Hays
# Nathaniel Atwood

def pixel_collision(mask1, rect1, mask2, rect2):
    """
    Check if the non-transparent pixels of one contacts the other.
    """

    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]
    # See if the two masks at the offset are overlapping.
    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap

def main():

    # Initialize pygame
    pygame.init()

    map = pygame.image.load("project_assets/map_1.png")
    # Store window width and height in different forms for easy access
    map_size = map.get_size()
    map_rect = map.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(map_size)
    map = map.convert_alpha()
    map.set_colorkey((255, 255, 255))
    map_mask = pygame.mask.from_surface(map)

    # Create the player data
    player = pygame.image.load("project_assets/mario_running.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (25, 25))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)


    # key = pygame.image.load("project_assets/start_button.png").convert_alpha()
    # key = pygame.transform.smoothscale(key, (25, 25))
    # key_rect = key.get_rect()
    # key_rect.center = (350, 400)
    # key_mask = pygame.mask.from_surface(key)

    start_button = pygame.image.load("project_assets/start_button.png").convert_alpha()
    start_button = pygame.transform.smoothscale(start_button, (150, 150))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (100, 600)
    start_button_mask = pygame.mask.from_surface(start_button)



    # door = pygame.image.load("project_assets/door.png").convert_alpha()
    # door = pygame.transform.smoothscale(door, (200, 200))
    # door_rect = door.get_rect()
    # door_rect.center = (550, 200)
    # door_mask = pygame.mask.from_surface(door)

    # The frame tells which sprite frame to draw
    frame_count = 0

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # Get a font - there is some problem on my Mac that makes this pause for 10s of seconds sometimes.
    # I will see if I can find a fix.
    myfont = pygame.font.SysFont('monospace', 24)

    # The started variable records if the start color has been clicked and the level started
    started = False

    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = False

    # # This state variable shows whether the key is found yet or not
    # found_key = False

    # Hide the arrow cursor and replace it with a sprite.
    pygame.mouse.set_visible(False)

    # This is the before game loop. In it we must:
    # - check for events
    # - update the scene
    # - draw the scene
    while not started:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            # Check if start_button was pressed
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, start_button_mask, start_button_rect):
                is_alive = True
                started = True

            # Position the player to the mouse location
            pos = pygame.mouse.get_pos()
            player_rect.center = pos
            print(pos)

            # Draw the background
            screen.fill((250, 250, 250))
            screen.blit(map, map_rect)

            # Only draw the start_button and door if the key is not collected
            screen.blit(start_button, start_button_rect)

            # Draw the player character
            screen.blit(player, player_rect)

            # Every time through the loop, increase the frame count.
            frame_count += 1

            # Bring drawn changes to the front
            pygame.display.update()

            # This tries to force the loop to run at 30 fps
            clock.tick(30)



    # This is the main game loop. In it we must:
    # - check for events
    # - update the scene
    # - draw the scene
    while is_alive:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos
        print(pos)

        # See if we touch the maze walls
        if pixel_collision(player_mask, player_rect, map_mask, map_rect):
            is_alive = False
            print("colliding", frame_count) # Don't leave this in the game



        # # Check if we contact the key
        # if not found_key and pixel_collision(player_mask, player_rect, start_button_mask, start_button_rect):
        #     found_key = True

        # Draw the background
        screen.fill((250,250,250))
        screen.blit(map, map_rect)

        # # Only draw the start_button and door if the key is not collected
        # if not found_key:
        #     pass
        #  screen.blit(door, door_rect)

        # Draw the player character
        screen.blit(player, player_rect)


        # Write some text to the screen. You can do something like this to show some hints or whatever you want.
        # label = myfont.render("By David!", True, (255,255,0))
        # screen.blit(label, (20,20))

        # Every time through the loop, increase the frame count.
        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 30 fps
        clock.tick(30)

    pygame.quit()
    sys.exit()


# Start the program
main()