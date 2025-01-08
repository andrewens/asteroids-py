import pygame
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)

    player = Player(PLAYER_SPAWN_X, PLAYER_SPAWN_Y)

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick() * 1e-3
        for game_object in updatable_group:
            game_object.update(dt)

        screen.fill(BACKGROUND_COLOR)
        for game_object in drawable_group:
            game_object.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
