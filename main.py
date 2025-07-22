import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from bullet import Bullet
import random

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock() 
    dt = 0.0

    # Create sprite groups for updating and drawing and asteroids
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Bullet.containers = shots, updatables, drawables
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

        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                running = False
            for bullet in shots:
                if bullet.collide(asteroid):
                    bullet.kill()
                    asteroid.split()


                
    pygame.quit()




if __name__ == "__main__":
    main()
