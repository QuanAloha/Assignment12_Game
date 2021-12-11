"""
Assignment12_Game Level One

Description of Game:
It's Finals week, and you have a ton of stuff to take care of. Stay on the path and avoid all the obstacles so
you can make it to the end.

General Description of Code:
This code is divided up into 3 main parts.
1. All the functions required to run the program are at the top.
2. Below all the functions is a main function  for each level that is separated into 3 subsections.
    1. Load all the game assets into variable that the code can work with.
    2. Start the Pregame Section where the player can mover around and examine the map until they press the start
        button.
    3. After the start_button is pressed, the game begins and the payer has to make it ot he end of the maze to make it
        to the next level.
3. The Commands that call the code in order.

The code in this file is written by Nathaniel Atwood and Megan Hays.This is a test.
Any distribution of this code without written consent is strictly prohibited.
"""

import sys
import pygame

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


def level_one_opener():
    # Load Level Assets
    game_map = pygame.image.load("project_assets/opener_1.png")
    # Store window width and height in different forms for easy access
    map_size = game_map.get_size()
    map_rect = game_map.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(map_size)
    game_map = game_map.convert_alpha()

    # Variable to Check if player is ready
    player_is_ready = False

    # Check events by looping over the list of events
    while not player_is_ready:
        for event in pygame.event.get():
            # Check if start_button was pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_is_ready = True

        # Draw the background
        screen.fill((250, 250, 250))
        screen.blit(game_map, map_rect)

        # Bring drawn changes to the front
        pygame.display.update()


def level_one():
    # Load Level Assets
    game_map = pygame.image.load("project_assets/map_1.png")
    # Store window width and height in different forms for easy access
    map_size = game_map.get_size()
    map_rect = game_map.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(map_size)
    game_map = game_map.convert_alpha()
    game_map.set_colorkey((255, 255, 255))
    map_mask = pygame.mask.from_surface(game_map)

    # Create the player data
    player = pygame.image.load("project_assets/mario_running.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (25, 25))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    # Create the Start Button data
    start_button = pygame.image.load("project_assets/start_button.png").convert_alpha()
    start_button = pygame.transform.smoothscale(start_button, (150, 150))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (100, 600)
    start_button_mask = pygame.mask.from_surface(start_button)

    # Create Marriot Library data
    marriot_library = pygame.image.load("project_assets/marriot_library.png").convert_alpha()
    marriot_library = pygame.transform.smoothscale(marriot_library, (187.5, 125))
    marriot_library_rect = marriot_library.get_rect()
    marriot_library_rect.center = (975, 150)
    marriot_library_mask = pygame.mask.from_surface(marriot_library)

    # Create ucard data
    ucard = pygame.image.load("project_assets/ucard.png").convert_alpha()
    ucard = pygame.transform.smoothscale(ucard, (300 / 4, 188 / 4))
    ucard_rect = ucard.get_rect()
    ucard_rect.center = (665, 136)
    ucard_mask = pygame.mask.from_surface(ucard)

    # Create blockade data
    blockade = pygame.image.load("project_assets/black_rectangle_vertical.png").convert_alpha()
    blockade = pygame.transform.smoothscale(blockade, (985 / 4, 492 / 6))
    blockade_rect = blockade.get_rect()
    blockade_rect.center = (1100, 260)
    blockade_mask = pygame.mask.from_surface(blockade)

    # The frame tells which sprite frame to draw
    frame_count = 0

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # The started variable records if the start color has been clicked and the level started
    started = False

    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = False

    # # This state variable shows whether the uID Card is found yet or not
    found_ucard = False

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
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, start_button_mask,
                                                                        start_button_rect):
                is_alive = True
                started = True

            # Position the player to the mouse location
            pos = pygame.mouse.get_pos()
            player_rect.center = pos

            # Draw the background
            screen.fill((250, 250, 250))
            screen.blit(game_map, map_rect)

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
    while is_alive and started:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            # Check if Player made it to the library.
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, marriot_library_mask,
                                                                        marriot_library_rect) and found_ucard:
                is_alive = True
                started = False
            # Check if the ucard is Collected
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, ucard_mask,
                                                                        ucard_rect):
                found_ucard = True

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos

        # See if we touch the maze walls
        if not found_ucard:
            if pixel_collision(player_mask, player_rect, map_mask, map_rect) or \
                    pixel_collision(player_mask, player_rect, blockade_mask, blockade_rect):
                # is_alive = False
                print('Colliding')
            elif pixel_collision(player_mask, player_rect, map_mask, map_rect):
                # is_alive = False
                print('Colliding')
        # Draw the background
        screen.fill((250, 250, 250))
        screen.blit(game_map, map_rect)

        # Only draw the start_button and door if the key is not collected
        if not found_ucard:
            screen.blit(ucard, ucard_rect)
            screen.blit(blockade, blockade_rect)

        # Draw the player character
        screen.blit(player, player_rect)

        # Draw the Library in the top right corner of the screen
        screen.blit(marriot_library, marriot_library_rect)

        # Every time through the loop, increase the frame count.
        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 30 fps
        clock.tick(30)


def level_two_opener():
    # Load Level Assets
    game_map = pygame.image.load("project_assets/opener_2.png")
    # Store window width and height in different forms for easy access
    map_size = game_map.get_size()
    map_rect = game_map.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(map_size)
    game_map = game_map.convert_alpha()

    # Variable to Check if player is ready
    player_is_ready = False

    # Check events by looping over the list of events
    while not player_is_ready:
        for event in pygame.event.get():
            # Check if start_button was pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_is_ready = True

        # Draw the background
        screen.fill((250, 250, 250))
        screen.blit(game_map, map_rect)

        # Bring drawn changes to the front
        pygame.display.update()


def level_two():
    game_map = pygame.image.load("project_assets/map_2.png")
    # Store window width and height in different forms for easy access
    map_size = game_map.get_size()
    map_rect = game_map.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(map_size)
    game_map = game_map.convert_alpha()
    game_map.set_colorkey((255, 255, 255))
    map_mask = pygame.mask.from_surface(game_map)

    # Create the player data
    player = pygame.image.load("project_assets/mario_running.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (25, 25))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    # Create the Start Button data
    start_button = pygame.image.load("project_assets/start_button.png").convert_alpha()
    start_button = pygame.transform.smoothscale(start_button, (150, 150))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (100, 600)
    start_button_mask = pygame.mask.from_surface(start_button)

    # Create Marriot Library data
    marriot_library = pygame.image.load("project_assets/marriot_library.png").convert_alpha()
    marriot_library = pygame.transform.smoothscale(marriot_library, (187.5, 125))
    marriot_library_rect = marriot_library.get_rect()
    marriot_library_rect.center = (975, 150)
    marriot_library_mask = pygame.mask.from_surface(marriot_library)

    # Create ucard data
    ucard = pygame.image.load("project_assets/ucard.png").convert_alpha()
    ucard = pygame.transform.smoothscale(ucard, (300 / 4, 188 / 4))
    ucard_rect = ucard.get_rect()
    ucard_rect.center = (665, 136)
    ucard_mask = pygame.mask.from_surface(ucard)

    # Create blockade data
    blockade = pygame.image.load("project_assets/black_rectangle_vertical.png").convert_alpha()
    blockade = pygame.transform.smoothscale(blockade, (985 / 4, 492 / 6))
    blockade_rect = blockade.get_rect()
    blockade_rect.center = (1100, 260)
    blockade_mask = pygame.mask.from_surface(blockade)

    # The frame tells which sprite frame to draw
    frame_count = 0

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # The started variable records if the start color has been clicked and the level started
    started = False

    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = False

    # # This state variable shows whether the uID Card is found yet or not
    found_ucard = False

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
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, start_button_mask,
                                                                        start_button_rect):
                is_alive = True
                started = True

            # Position the player to the mouse location
            pos = pygame.mouse.get_pos()
            player_rect.center = pos

            # Draw the background
            screen.fill((250, 250, 250))
            screen.blit(game_map, map_rect)

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
    while is_alive and started:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            # Check if Player made it to the library.
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, marriot_library_mask,
                                                                        marriot_library_rect) and found_ucard:
                is_alive = True
                started = False
            # Check if the ucard is Collected
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, ucard_mask,
                                                                        ucard_rect):
                found_ucard = True

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos

        # See if we touch the maze walls
        if not found_ucard:
            if pixel_collision(player_mask, player_rect, map_mask, map_rect) or \
                    pixel_collision(player_mask, player_rect, blockade_mask, blockade_rect):
                # is_alive = False
                print('Colliding')
            elif pixel_collision(player_mask, player_rect, map_mask, map_rect):
                # is_alive = False
                print('Colliding')

        # Draw the background
        screen.fill((250, 250, 250))
        screen.blit(game_map, map_rect)

        # Only draw the start_button and door if the key is not collected
        if not found_ucard:
            screen.blit(ucard, ucard_rect)
            screen.blit(blockade, blockade_rect)

        # Draw the player character
        screen.blit(player, player_rect)

        # Draw the Library in the top right corner of the screen
        screen.blit(marriot_library, marriot_library_rect)

        # Every time through the loop, increase the frame count.
        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 30 fps
        clock.tick(30)


def level_three_opener():
    # Load Level Assets
    game_map = pygame.image.load("project_assets/opener_3.png")
    # Store window width and height in different forms for easy access
    map_size = game_map.get_size()
    map_rect = game_map.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(map_size)
    game_map = game_map.convert_alpha()

    # Variable to Check if player is ready
    player_is_ready = False

    # Check events by looping over the list of events
    while not player_is_ready:
        for event in pygame.event.get():
            # Check if start_button was pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_is_ready = True

        # Draw the background
        screen.fill((250, 250, 250))
        screen.blit(game_map, map_rect)

        # Bring drawn changes to the front
        pygame.display.update()


def level_three():
    game_map = pygame.image.load("project_assets/map_3.png")
    # Store window width and height in different forms for easy access
    map_size = game_map.get_size()
    map_rect = game_map.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(map_size)
    game_map = game_map.convert_alpha()
    game_map.set_colorkey((255, 255, 255))
    map_mask = pygame.mask.from_surface(game_map)

    # Create the player data
    player = pygame.image.load("project_assets/mario_running.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (25, 25))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    # Create the Start Button data
    start_button = pygame.image.load("project_assets/start_button.png").convert_alpha()
    start_button = pygame.transform.smoothscale(start_button, (150, 150))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (100, 600)
    start_button_mask = pygame.mask.from_surface(start_button)

    # Create Marriot Library data
    marriot_library = pygame.image.load("project_assets/marriot_library.png").convert_alpha()
    marriot_library = pygame.transform.smoothscale(marriot_library, (187.5, 125))
    marriot_library_rect = marriot_library.get_rect()
    marriot_library_rect.center = (975, 150)
    marriot_library_mask = pygame.mask.from_surface(marriot_library)

    # Create ucard data
    ucard = pygame.image.load("project_assets/ucard.png").convert_alpha()
    ucard = pygame.transform.smoothscale(ucard, (300 / 4, 188 / 4))
    ucard_rect = ucard.get_rect()
    ucard_rect.center = (665, 136)
    ucard_mask = pygame.mask.from_surface(ucard)

    # Create blockade data
    blockade = pygame.image.load("project_assets/black_rectangle_vertical.png").convert_alpha()
    blockade = pygame.transform.smoothscale(blockade, (985 / 4, 492 / 6))
    blockade_rect = blockade.get_rect()
    blockade_rect.center = (1100, 260)
    blockade_mask = pygame.mask.from_surface(blockade)

    # The frame tells which sprite frame to draw
    frame_count = 0

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # The started variable records if the start color has been clicked and the level started
    started = False

    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = False

    # # This state variable shows whether the uID Card is found yet or not
    found_ucard = False

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
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, start_button_mask,
                                                                        start_button_rect):
                is_alive = True
                started = True

            # Position the player to the mouse location
            pos = pygame.mouse.get_pos()
            player_rect.center = pos

            # Draw the background
            screen.fill((250, 250, 250))
            screen.blit(game_map, map_rect)

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
    while is_alive and started:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            # Check if Player made it to the library.
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, marriot_library_mask,
                                                                        marriot_library_rect) and found_ucard:
                is_alive = True
                started = False
            # Check if the ucard is Collected
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, ucard_mask,
                                                                        ucard_rect):
                found_ucard = True

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos

        # See if we touch the maze walls
        if not found_ucard:
            if pixel_collision(player_mask, player_rect, map_mask, map_rect) or \
                    pixel_collision(player_mask, player_rect, blockade_mask, blockade_rect):
                # is_alive = False
                print('Colliding')
            elif pixel_collision(player_mask, player_rect, map_mask, map_rect):
                # is_alive = False
                print('Colliding')

        # Draw the background
        screen.fill((250, 250, 250))
        screen.blit(game_map, map_rect)

        # Only draw the start_button and door if the key is not collected
        if not found_ucard:
            screen.blit(ucard, ucard_rect)
            screen.blit(blockade, blockade_rect)

        # Draw the player character
        screen.blit(player, player_rect)

        # Draw the Library in the top right corner of the screen
        screen.blit(marriot_library, marriot_library_rect)

        # Every time through the loop, increase the frame count.
        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 30 fps
        clock.tick(30)

def game_over():
    pass


def main():
    # Initialize pygame
    pygame.init()
    level_one_opener()
    level_one()
    level_two()
    level_three()
    pygame.quit()
    sys.exit()


# Start the program
main()
