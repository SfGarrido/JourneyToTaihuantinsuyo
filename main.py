# Example file showing a circle moving on screen
import pygame
import abilities
import constant
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
time = 0
jumps = 1
jump_time = 0
jumping = False
dy = 0
accel = 14
downward_accel = 1
grounded = 1
gravity = constant.GRAVITY
direc_horizontal = -1  # -1 for left, 1 for right
x = abilities.Dash()
x.func()
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)
    if x.active:
        time += dt
        if time > 0.3:
            time = 0
            x.active = False
        else:
            counter = 0
            while counter < 4:
                player_pos.x += 200 * dt * direc_horizontal
                counter += 1
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and jumps > 0:
            gravity = 0
            jumps -= 1
            jumping = True
            dy = -60
        if jumping:
            counter = 0
            jump_time += dt
            accel -= 0.3
            if jump_time > 0.7:
                accel = 14
                jump_time = 0
                gravity = constant.GRAVITY
                jumping = False
                dy = 0
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            direc_horizontal = -1
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            direc_horizontal = 1
            player_pos.x += 300 * dt
        if keys[pygame.K_1]:
            if x.current == 0:
                x.current = x.cooldown
                x.active = True
    if x.current > 0:
        x.current -= dt
        if x.current < 0:
            x.current = 0
    # flip() the display to put your work on screen
    player_pos.y += gravity * dt + dy * dt * accel
    pygame.display.flip()
    if player_pos.y < 600:
        gravity = constant.GRAVITY * downward_accel
        downward_accel += 0.1
    else:
        gravity = 0
        downward_accel = 1
        player_pos.y = 600
        grounded = True
        jumps = 1
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
