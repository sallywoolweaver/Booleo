import pygame
import sys
import random


class Gameplay:
    
    def __init__(self):
        self.setup()
        self.main()
        
    def setup(self):
        start_bools = Start_Bools() 
        for i in range (6) :
            print(start_bools.get_starting_bit())
    
    def main(self):

        # Initialize Pygame
        pygame.init()

        # Set up display
        WINDOW_SIZE = (1400, 800)
        window = pygame.display.set_mode(WINDOW_SIZE)

        # Load images
        # For now, we'll just create placeholders. Replace these with your own code.
        #game_board = pygame.image.load('game_board.png')

        # Load the images for the game board
        image= pygame.image.load('0.png')
        self.setup()
        # Resize the image
        image = pygame.transform.scale(image, (100, 150))


        # Set up game variables
        # Again, just placeholders for now.
        current_player = 1

        # Main game loop
        game_active = True
        while game_active:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_active = False
                # Add other event types here

            # Update game state
            # This could involve moving pieces, checking for a win, etc.
            # For now, we'll just leave it empty.

            # Draw everything
            window.fill((255, 255, 255))  # Fill the screen with white
            #window.blit(game_board, (0, 0))  # Draw the game board

            # Draw the images in the middle of the game board
        # Define the space between images
            space_between_images = 40  # adjust this value as needed

            images = [image, image, image, image, image, image]
            for i, img in enumerate(images):
                # Calculate the total width of one image plus the space
                total_width = img.get_width() + space_between_images

                # Calculate the starting x-coordinate for the first image
                start_x = WINDOW_SIZE[0] / 2 - (total_width * len(images)) / 2

                # Calculate the x-coordinate for this image
                x = start_x + total_width * i

                # Calculate the y-coordinate for the images
                y = WINDOW_SIZE[1] / 2 - img.get_height() / 2

                window.blit(img, (x, y))


            # Flip the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        sys.exit()
        



class Start_Bools:
    def __init__(self):
        self.image = '0.png'

    def get_img(self):
        return self.image
    
    def get_starting_bit(self):
        return random.randint(0,1)
    
 
 
if __name__ == "__main__":
    game = Gameplay()

   

