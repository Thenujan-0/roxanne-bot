import pystray

icon = pystray.Icon('test name')

from PIL import Image, ImageDraw

def create_image():
    width =100
    height=100
    color2='blue'
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height),'red' )
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image

icon.icon = create_image()


icon.run()