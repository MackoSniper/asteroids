import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock() 
    dt = 0.0

    # Create sprite groups for updating and drawing and asteroids
    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = updatables, drawables
    Asteroid.containers = asteroids, updatables, drawables
    AsteroidField.containers = updatables

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  
        for sprite in drawables:
            sprite.draw(screen)
        
        updatables.update(dt)
        pygame.display.flip()    
        dt = clock.tick(60) / 1000.0  

    pygame.quit()




if __name__ == "__main__":
    main()
