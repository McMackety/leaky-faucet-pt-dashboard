import cairosvg

WIDTH = 1600
HEIGHT = 900

png = cairosvg.svg2png(url='resources/pid.svg', parent_width=WIDTH, parent_height=HEIGHT)
print(png)