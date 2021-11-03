#!/usr/bin/python

import pygame
import pygame.freetype
import com
import signal

WIDTH = 1710
HEIGHT = 1347

# Connect to Serial
serial = com.RocketSerial()
serial.start()

def sig_handler():
    serial.stop()

signal.signal(signal.SIGTERM, sig_handler)

# Prepare PyGame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.get_surface()

# Load the Image
image = pygame.image.load("resources/pid.png")

# Load the font
font = pygame.freetype.Font("resources/Roboto-Regular.ttf", 24)

# The display needs to be flipped.
pygame.display.flip() 

clock = pygame.time.Clock()
while True:
    # Draw Background
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))

    data = serial.read_data()

    if len(data) == 8:
        font.render_to(screen, (399, 60), data[0], (200, 0, 0))
        font.render_to(screen, (311, 338), data[1], (200, 0, 0))
        font.render_to(screen, (536, 276), data[2], (200, 0, 0))
        font.render_to(screen, (491, 704), data[3], (200, 0, 0))
        font.render_to(screen, (983, 293), data[4], (200, 0, 0))
        font.render_to(screen, (792, 432), data[5], (200, 0, 0))
        font.render_to(screen, (564, 852), data[6], (200, 0, 0))
        font.render_to(screen, (776, 851), data[7], (200, 0, 0))

    pygame.display.flip() 

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            serial.stop()
            raise SystemExit