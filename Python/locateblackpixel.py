from PIL import ImageGrab
import numpy as np

def locate_black_pixel():
    image = ImageGrab.grab()
    array = np.array(image)
    y, x = np.where(np.all(array == [0, 0, 0], -1))

    coordinates = []
    for i in list(zip(x, y)):
        print(i)
        if ((i[0] > 485) and (i[1] > 261)) and ((i[0] < 879) and (i[1] < 593)):
            coordinates.append(i)

    print(coordinates)
    print(f"There are {len(coordinates)} black pixels")

locate_black_pixel()