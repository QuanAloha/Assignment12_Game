"""
Assignment12_Game

Description of Game:
It's Finals week, and you have a ton of stuff to take care of. Stay on the path and avoid all the obstacles so
you can make it to the end.

General Description of Code:
This code is divided up into 3 main parts.
1. All the functions required to run the program are at the top.
2. Below all the functions is a main function for each level that is separated into 3 subsections.
    1. Load all the game assets into variable that the code can work with.
    2. Start the Pregame Section where the player can mover around and examine the map until they press the start
        button.
    3. After the start_button is pressed, the game begins and the payer has to make it ot he end of the maze to make it
        to the next level.
3. The Commands that call the code in order.

The code in this file is written by Nathaniel Atwood and Megan Hays.
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

def end_game_level1():
    # Load end game
    game_map = pygame.image.load("project_assets/end_screen.png")

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
        level_one()


def end_game_level2():
    # Load end game
    game_map = pygame.image.load("project_assets/end_screen.png")
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
        level_two()


def end_game_level3():
    # Load end game
    game_map = pygame.image.load("project_assets/end_screen.png")
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
        level_three()

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

    # Hide the arrow cursor
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

            # draw start_button
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
                is_alive = False
                print('Colliding')
                end_game_level1()

        # See if we touch maze walls after getting Ucard
        if pixel_collision(player_mask, player_rect, map_mask, map_rect):
            is_alive = False
            print('Colliding')
            end_game_level1()

        # Draw the background
        screen.fill((250, 250, 250))
        screen.blit(game_map, map_rect)

        # draw the start_button and door
        if not found_ucard:
            screen.blit(ucard, ucard_rect)
            screen.blit(blockade, blockade_rect)

        # Draw the player character
        screen.blit(player, player_rect)

        # Draw the Library
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
    start_button_rect.center = (1050, 63)
    start_button_mask = pygame.mask.from_surface(start_button)

    # Create Cade Lab data
    cade_lab = pygame.image.load("project_assets/cade_lab.png").convert_alpha()
    cade_lab = pygame.transform.smoothscale(cade_lab, (187.5, 125))
    cade_lab_rect = cade_lab.get_rect()
    cade_lab_rect.center = (1050, 350)
    cade_lab_mask = pygame.mask.from_surface(cade_lab)

    # Create ucard data
    ucard = pygame.image.load("project_assets/ucard.png").convert_alpha()
    ucard = pygame.transform.smoothscale(ucard, (300 / 4, 188 / 4))
    ucard_rect = ucard.get_rect()
    ucard_rect.center = (98, 587)
    ucard_mask = pygame.mask.from_surface(ucard)

    # Create coffee data
    coffee = pygame.image.load("project_assets/coffee.png").convert_alpha()
    coffee = pygame.transform.smoothscale(coffee, (1685 / 20, 2503 / 20))
    coffee_rect = coffee.get_rect()
    coffee_rect.center = (1080, 580)
    coffee_mask = pygame.mask.from_surface(coffee)

    # Create blockade data
    blockade = pygame.image.load("project_assets/black_rectangle_vertical.png").convert_alpha()
    blockade = pygame.transform.smoothscale(blockade, (985 / 4, 492 / 6))
    blockade_rect = blockade.get_rect()
    blockade_rect.center = (1048, 209)
    blockade_mask = pygame.mask.from_surface(blockade)

    # The frame tells which sprite frame to draw
    frame_count = 0

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # The started variable records if the start color has been clicked and the level started
    started = False

    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = True

    # This state variable shows whether the uID Card is found yet or not
    found_ucard = False

    # This state variable shows whether the coffee is found yet or not
    found_coffee = False

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
            # Check if Player made it to the cade lab
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, cade_lab_mask,
                                                                        cade_lab_rect) and found_ucard and found_coffee:
                is_alive = True
                started = False
            # Check if the ucard is Collected
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, ucard_mask,
                                                                        ucard_rect):
                found_ucard = True
            # Check if coffee is collected
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, coffee_mask,
                                                                        coffee_rect):
                found_coffee = True

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos

        # See if we touch the maze walls
        if not found_ucard:
            if pixel_collision(player_mask, player_rect, map_mask, map_rect) or \
                    pixel_collision(player_mask, player_rect, blockade_mask, blockade_rect):
                is_alive = False
                end_game_level2()
            elif pixel_collision(player_mask, player_rect, map_mask, map_rect):
                is_alive = False

        if pixel_collision(player_mask, player_rect, map_mask, map_rect):
            is_alive = False
            end_game_level2()

        # Draw the background
        screen.fill((250, 250, 250))
        screen.blit(game_map, map_rect)

        # Checking if ucard is not found
        if not found_ucard:
            screen.blit(ucard, ucard_rect)
            screen.blit(blockade, blockade_rect)

        # Checking if coffee is not found
        if not found_coffee:
            screen.blit(coffee, coffee_rect)

        # Draw the player character
        screen.blit(player, player_rect)

        # Draw the cade lab in the top right corner of the screen
        screen.blit(cade_lab, cade_lab_rect)

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
    start_button_rect.center = (75, 61)
    start_button_mask = pygame.mask.from_surface(start_button)

    # Create car data
    car = pygame.image.load("project_assets/car.png").convert_alpha()
    car = pygame.transform.smoothscale(car, (187.5, 125))
    car_rect = car.get_rect()
    car_rect.center = (429, 460)
    car_mask = pygame.mask.from_surface(car)

    # Create snail data
    snail = pygame.image.load("project_assets/snail.png").convert_alpha()
    snail = pygame.transform.smoothscale(snail, (300 / 4, 188 / 4))
    snail_rect = snail.get_rect()
    snail_rect.center = (150, 510)
    snail_mask = pygame.mask.from_surface(snail)

    # boss data aka david
    david = pygame.image.load("project_assets/david_johnson.png").convert_alpha()
    david = pygame.transform.smoothscale(david, (250 / 5, 250 / 5))
    david_rect = david.get_rect()
    david_rect.center = (200, 200)
    david_mask = pygame.mask.from_surface(david)
    david_right = True

    # fast david/boss
    fast_david = pygame.image.load("project_assets/fast_david.png").convert_alpha()
    fast_david = pygame.transform.smoothscale(david, (250 / 5, 250 / 5))
    fast_david_rect = david.get_rect()
    fast_david_rect.center = (950, 180)
    fast_david_mask = pygame.mask.from_surface(david)
    fast_david_right = True

    # The frame tells which sprite frame to draw
    frame_count = 0

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # The started variable records if the start color has been clicked and the level started
    started = False

    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = False

    # # This state variable shows whether the snail is found yet or not
    found_snail = False

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

            # draw the start_button and door
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
            # Check if Player made it to the car
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, car_mask,
                                                                        car_rect):
                is_alive = True
                started = False
            # Check if the snail is Collected
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, snail_mask,
                                                                        snail_rect):
                found_snail = True

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos

        # See if we touch the maze walls
        if pixel_collision(player_mask, player_rect, david_mask, david_rect):
            is_alive = False
            end_game_level3()

        if pixel_collision(player_mask, player_rect, fast_david_mask, fast_david_rect):
            is_alive = False
            end_game_level3()

        if pixel_collision(player_mask, player_rect, map_mask, map_rect):
            is_alive = False
            end_game_level3()

        # making david move
        if frame_count % 200 == 0:
            if david_right == True:
                david_right = False
            elif david_right == False:
                david_right = True
        if david_right == True:
            david_rect.move_ip((2, 0))
        if david_right == False:
            david_rect.move_ip((-2, 0))

        # making fast david move and get slow
        if found_snail == False:
            if frame_count % 18 == 0:
                if fast_david_right == True:
                    fast_david_right = False
                elif fast_david_right == False:
                    fast_david_right = True
            if fast_david_right == True:
                fast_david_rect.move_ip((12, 0))
            if fast_david_right == False:
                fast_david_rect.move_ip((-12, 0))
        elif found_snail == True:
            if frame_count % 200 == 0:
                if fast_david_right == True:
                    fast_david_right = False
                elif fast_david_right == False:
                    fast_david_right = True
            if fast_david_right == True:
                fast_david_rect.move_ip((2, 0))
            if fast_david_right == False:
                fast_david_rect.move_ip((-2, 0))

        # Draw the background
        screen.fill((250, 250, 250))
        screen.blit(game_map, map_rect)

        # Draw the player character
        screen.blit(player, player_rect)

        # Draw the car
        screen.blit(car, car_rect)

        # Draw david
        screen.blit(david, david_rect)

        # Draw fast david
        screen.blit(fast_david, fast_david_rect)

        # Draw snail
        screen.blit(snail, snail_rect)

        # Every time through the loop, increase the frame count.
        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 30 fps
        clock.tick(30)

def main():
    # Initialize pygame
    pygame.init()
    level_one_opener()
    level_one()
    level_two_opener()
    level_two()
    level_three_opener()
    level_three()
    pygame.quit()
    sys.exit()

# Start the program
main()
