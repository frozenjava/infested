#
# Infested.py
# Josh Artuso
# 06/02/2015
#
# This is my first attempt at creating a game with PyGame
#

import pygame
import Player

# VARIABLES
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


def main():
    """
    The Main function
    :return:
    """

    # Initialize pygame
    pygame.init()

    # Create a surface object
    game_display = pygame.display.set_mode((800, 600))

    # Set the title of the window
    pygame.display.set_caption("Infested")

    # Create a pygame clock object
    clock = pygame.time.Clock()

    # Set the initial environment
    game_display.fill(white)
    player = Player.Player()
    player.draw_player(pygame, game_display)
    pygame.display.update()

    # Exit the game boolean
    game_exit = False

    # Loop until we should exit
    while not game_exit:
        # Handle each event
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                game_exit = True

            # Key press events
            if event.type == pygame.KEYDOWN:
                # Move the player to the left
                if event.key == pygame.K_LEFT:
                    player.request_update_x(-5)
                # Move the player to the right
                elif event.key == pygame.K_RIGHT:
                    player.request_update_x(5)
                # Move the player up
                elif event.key == pygame.K_UP:
                    player.request_update_y(-5)
                # Move the player down
                elif event.key == pygame.K_DOWN:
                    player.request_update_y(5)

            # Key up events
            if event.type == pygame.KEYUP:
                # Stop left and right movement
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.request_update_x(0)
                # Stop up and down movement
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.request_update_y(0)

        player.preform_update(pygame, game_display, white)

        clock.tick(20)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
