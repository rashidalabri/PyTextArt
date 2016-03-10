import sys
import time

# get the text to print
try:
    text = sys.argv[1]
except IndexError:
    print 'Error: Text to print was not specified'
    exit()

# get the font to use
try:
    font = sys.argv[2]
except IndexError:
    font = 'main_font'

# execute the font file
exec(open(font+'.py').read())

# start printing
for word in text.lower().split(' '):
    
    # create an empty canvas
    canvas = []

    # append empty elements to the canvas according to height
    for _ in range(height):
        canvas.append([])    

    # create the canvas
    for char in word:
        char_canvas = eval(replace_hook(char))
        for char_line in range(height):
            canvas[char_line] = canvas[char_line] + [0] + char_canvas[char_line]
    
    # print the canvas
    for line in canvas:
        string = ''
        for block in line:
            if block >= 1:
                string = string + block_black
            elif block <= 0:
                string = string + block_white
        print string
        time.sleep(0.07)
    
    # print an empty line
    print ''

    time.sleep(0.05)
