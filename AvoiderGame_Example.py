import sys, pygame, math

# Starter code for an avoider game. Written by David Johnson for CS 1400 University of Utah.

# Finished game authors:
#
#

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

    map = pygame.image.load("project_assets/map.png")
    # Store window width and height in different forms for easy access
    map_size = map.get_size()
    map_rect = map.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(map_size)
    map = map.convert_alpha()
    map.set_colorkey((255, 255, 255))
    map_mask = pygame.mask.from_surface(map)

    # Create the player data
    player = pygame.image.load("project_assets/alien1.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (25, 25))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    key = pygame.image.load("project_assets/key.png").convert_alpha()
    key = pygame.transform.smoothscale(key, (25, 25))
    key_rect = key.get_rect()
    key_rect.center = (350, 400)
    key_mask = pygame.mask.from_surface(key)


    door = pygame.image.load("project_assets/door.png").convert_alpha()
    door = pygame.transform.smoothscale(door, (200, 200))
    door_rect = door.get_rect()
    door_rect.center = (550, 200)
    door_mask = pygame.mask.from_surface(door)

    # The frame tells which sprite frame to draw
    frame_count = 0;

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # Get a font - there is some problem on my Mac that makes this pause for 10s of seconds sometimes.
    # I will see if I can find a fix.
    myfont = pygame.font.SysFont('monospace', 24)

    # The started variable records if the start color has been clicked and the level started
    started = False

    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = True

    # This state variable shows whether the key is found yet or not
    found_key = False

    # Hide the arrow cursor and replace it with a sprite.
    pygame.mouse.set_visible(False)

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

        # See if we touch the maze walls
        if pixel_collision(player_mask, player_rect, map_mask, map_rect):
            print("colliding", frame_count) # Don't leave this in the game

        # Check if we contact the key
        if not found_key and pixel_collision(player_mask, player_rect, key_mask, key_rect):
            found_key = True

        # Draw the background
        screen.fill((250,250,250))
        screen.blit(map, map_rect)

        # Only draw the key and door if the key is not collected
        if not found_key:
            screen.blit(key, key_rect)
            screen.blit(door, door_rect)

        # Draw the player character
        screen.blit(player, player_rect)

        # Write some text to the screen. You can do something like this to show some hints or whatever you want.
        label = myfont.render("By David!", True, (255,255,0))
        screen.blit(label, (20,20))

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
