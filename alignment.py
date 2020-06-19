from PIL import Image, ImageDraw, ImageFont
import sys

try:
    test = sys.argv[1]
    arg = sys.argv
except IndexError:
    from choose_opposites import list
    arg = list

grid = [
    [arg[1], 'neutral', arg[2]],
    [arg[3], 'neutral', arg[4]]
]

size = 600
section = size/3
unit = section/6

img = Image.new('RGB', (size, size), color = 'white')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font="arial.ttf", size=16)
for x in range(3):
    for y in range(3):
        draw.rectangle(
            [(section*x + unit, section*y + 3*unit/2), 
            (section*(x+1) - unit, section*(y+1) - unit/2)], 
            outline='black'
        )
                
        if x == y == 1: 
            text = "true neutral"
        else:
            text = str(grid[0][x] + " " + grid[1][y])
        draw.text(
            (section*x + unit, section*y + unit/2),
            text,
            fill = 'black',
            font=font
        )

img.save('test.png')
