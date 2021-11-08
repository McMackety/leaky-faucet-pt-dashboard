#!/usr/bin/python

import pygame
import pygame.freetype
from pygame.locals import *
import com
import signal
import cairosvg
import io

WIDTH = 1600
HEIGHT = 900

# Connect to Serial
serial = com.RocketSerial()
serial.start()

def sig_handler():
    serial.stop()

signal.signal(signal.SIGTERM, sig_handler)

png = cairosvg.svg2png(url='resources/pid.svg', output_width=WIDTH, output_height=HEIGHT, dpi=300)

# Prepare PyGame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)
screen = pygame.display.get_surface()

# Load the Image
image = pygame.image.load(io.BytesIO(png))

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

    if len(data) == 9:
        font.render_to(screen, (WIDTH * 0.0, HEIGHT * 0.0), "Time: {}".format(data[0]), (200, 0, 0))
        font.render_to(screen, (WIDTH * 0.3625, HEIGHT * 0.062), data[1], (200, 0, 0))
        font.render_to(screen, (WIDTH * 0.31875, HEIGHT * 0.318), data[2], (200, 0, 0))
        font.render_to(screen, (WIDTH * 0.4325, HEIGHT * 0.2566), data[3], (200, 0, 0))
        font.render_to(screen, (WIDTH * 0.409375, HEIGHT * 0.6566), data[4], (200, 0, 0))
        font.render_to(screen, (WIDTH * 0.6725, HEIGHT * 0.2677), data[5], (200, 0, 0))
        font.render_to(screen, (WIDTH * 0.57125, HEIGHT * 0.40333), data[6], (200, 0, 0))
        font.render_to(screen, (WIDTH * 0.449375, HEIGHT * 0.8), data[7], (200, 0, 0))
        font.render_to(screen, (WIDTH * 0.560625, HEIGHT * 0.8), data[8], (200, 0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse1, mouse2, mouse3 = pygame.mouse.get_pressed()

    if mouse1:
        print("Width: {}, Height: {}".format((mouse_x + 1) / WIDTH, (mouse_y + 1) / HEIGHT))

    pygame.display.flip() 

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            serial.stop()
            raise SystemExit
        elif event.type==VIDEORESIZE:
            WIDTH, HEIGHT = event.dict['size']
            png = cairosvg.svg2png(url='resources/pid.svg', output_width=WIDTH, output_height=HEIGHT, dpi=300)
            image = pygame.image.load(io.BytesIO(png))