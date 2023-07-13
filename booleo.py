import pygame
import sys
import random

class CardSprite:
    def __init__(self, img, rect):
        self.img = img
        self.rect = rect
        self.selected = False


class Gameplay:
    
    def __init__(self):
        self.setup()
        self.main()
        
    def setup(self):
        self.start_bools = Start_Bools()
        self.start_deck =[]
        self.player1_hand =[]
        self.player2_hand =[]

        for i in range (6) :
            self.start_deck.append(Start_Bools())
        self.current_player=1
        for i in range(4):
            self.player1_hand.append(Cards())
            self.player2_hand.append(Cards())
        print("P1 cards", [card.get_tup() for card in self.player1_hand])
        print("P2 cards", [card.get_tup() for card in self.player2_hand])
        self.player1_cards=[]
        self.player2_cards=[]
        for card in self.player1_hand:
            img = pygame.transform.scale(pygame.image.load(card.get_img()), (100,150))
            rect = img.get_rect()
            self.player1_cards.append(CardSprite(img, rect))
        for card in self.player2_hand:
            img = pygame.transform.scale(pygame.image.load(card.get_img()), (100,150))
            rect = img.get_rect()
            self.player2_cards.append(CardSprite(img, rect))

                
    
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
        images=[]
        #image= pygame.image.load('0.png')
        for card in self.start_deck:
            images.append(pygame.transform.scale(pygame.image.load(card.get_img()), (100,150)))



        # Main game loop
        game_active = True
        while game_active:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_active = False
                # Add other event types here
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for card in self.player1_cards:
                        if card.rect.collidepoint(event.pos):
                            card.selected = not card.selected  # Toggle selection

                    for card in self.player2_cards:
                        if card.rect.collidepoint(event.pos):
                            card.selected = not card.selected  # Toggle selection

            # Update game state
            # This could involve moving pieces, checking for a win, etc.
            # For now, we'll just leave it empty.

            # Draw everything
            window.fill((255, 255, 255))  # Fill the screen with white
            #window.blit(game_board, (0, 0))  # Draw the game board

            # Draw the images in the middle of the game board
        # Define the space between images
            space_between_images = 40  # adjust this value as needed

            #images = [image, image, image, image, image, image]
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
                
            space_between_cards = 40  # adjust this value as needed
            card_width = self.player1_cards[0].img.get_width() + space_between_cards

            for i, card in enumerate(self.player1_cards):
                x = space_between_cards + i * card_width
                y = space_between_cards  # Adjust this as needed
                card.rect.topleft = (x, y)
                window.blit(card.img, card.rect.topleft)
                if card.selected:
                    pygame.draw.rect(window, (255, 0, 0), card.rect, 2)

            for i, card in enumerate(self.player2_cards):
                x = space_between_cards + i * card_width
                y = WINDOW_SIZE[1] - card.img.get_height() - space_between_cards  # Adjust this as needed
                card.rect.topleft = (x, y)
                window.blit(card.img, card.rect.topleft)
                if card.selected:
                    pygame.draw.rect(window, (255, 0, 0), card.rect, 2)

            # Flip the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        sys.exit()
        



class Start_Bools:


    def get_img(self):
        if self.start_bit==0:
            self.image = '0.png'
        else:
            self.image= '1.png'
        return self.image
    
    def get_starting_bit(self):
        return random.randint(0,1)
    
    def __init__(self):
        self.start_bit=self.get_starting_bit() 
        
        

class Cards:
    
    
    def __init__(self):
        if random.randint(0,100) <=17:
            self.type = "NOT"
            self.value = ''
        else:
            self.type = random.choice(["AND", "OR", "XOR", "NAND", "NOR"])
            self.value = random.randint(0,1)
    
    def get_type(self):
        return self.type
    
    def get_value(self):
        return self.value
    
    def get_tup(self):
        return self.type, self.value
 
    def get_img(self):
        if self.value ==0:
            if self.type =="OR":
                return "or0.png"
            else:
                return "and0.png"
        else:
            if self.type =="OR":
                return "or1.png"
            else:
                return "and1.png"



if __name__ == "__main__":
    game = Gameplay()

   

