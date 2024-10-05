from PIL import ImageGrab
import numpy as np

image = ImageGrab.grab()

def locate_pixel(color: list[int] | None, x1: int = 0, y1: int = 0, x2: int = image.size[0], y2: int = image.size[1]):
    image_array = np.array(image)
    
    # Check and store all pixels that are equal to the color
    y, x = np.where(np.all(image_array == color, -1))

    coordinates = []

    # Allows for correct coordinates if the desired area is different from screen resolution
    for i in list(zip(x, y)):
        # Ignore any pixel outside the desired area
        if ((i[0] > x1) and (i[1] > y1)) and ((i[0] < x2) and (i[1] < y2)):
            coordinates.append(i)

    pixel_count = len(coordinates)

    return pixel_count, coordinates