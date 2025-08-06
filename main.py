import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\n"
          f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    
    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    AsteroidField.containers = (updateable_group)
    Asteroid.containers = (asteroids, updateable_group, drawable_group)
    Player.containers = (updateable_group, drawable_group)
    Shot.containers = (updateable_group, drawable_group, shots)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        
        for obj in drawable_group:
            obj.draw(screen)
        updateable_group.update(dt)
        
        for obj in asteroids:
            if obj.do_collide(player):
                print("Game over!")
                running = False
        
        for obj in asteroids:
            for bullet in shots:
                if obj.do_collide(bullet):
                    bullet.kill()
                    obj.split(screen)

        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    


if __name__ == "__main__":
    main()
