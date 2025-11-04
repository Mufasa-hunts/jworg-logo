from graphics import Canvas

CANVAS_WIDTH = 250
CANVAS_HEIGHT = 200

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_jw_logo(canvas)

def draw_jw_logo(canvas):
    # Background color (JW.org blue)
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "#4A6DA7")

    # JW text (centered visually)
    canvas.create_text(60, 40, 
    "JW", 
    color = "white", 
    font_size = 90)

     # .ORG text (centered visually)
    canvas.create_text(50, 120, 
    ".ORG", 
    color = "white", 
    font_size = 55)




if __name__ == '__main__':
    main()
