from PIL import ImageGrab
import numpy as np

image = ImageGrab.grab()

def locate_pixel(color: list[int] | None, x1: int = 0, y1: int = 0, x2: int = image.size[0], y2: int = image.size[1]):
    image_array = np.array(image)
    y, x = np.where(np.all(image_array == color, -1))

    coordinates = []
    for i in list(zip(x, y)):
        if ((i[0] > x1) and (i[1] > y1)) and ((i[0] < x2) and (i[1] < y2)):
            coordinates.append(i)

    print(coordinates)
    print(f"There are {len(coordinates)} black pixels")

locate_pixel([0, 0, 0], 485, 261, 879, 593)