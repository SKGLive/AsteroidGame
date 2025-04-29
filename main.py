# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()   # Initialize the pygame library
    timeClock = pygame.time.Clock() # Create a clock object to control the frame rate
    dt = 0.0    # Initialize delta time variable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    # Create a player object

    # game prompt
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     # Create a screen with the specified width and height

    # create game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "BLACK")  # Fill the screen with black color
        player.draw(screen)  # Draw the player on the screen
        pygame.display.flip()  # Update the screen with the new content
        
        timeClock.tick(60)  # pauses the game loop until 1/60th of a second has passed
        dt = timeClock.tick(60) / 1000.0  # Calculate delta time in seconds

if __name__ == "__main__":
    main()