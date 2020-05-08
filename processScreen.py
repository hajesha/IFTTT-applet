import time
import numpy as np
import skimage
from skimage import io
from skimage.transform import resize
from colorthief import ColorThief


def get_colors_using_colorthief():
    color_thief = ColorThief("temp.png")
    return color_thief.get_color(quality=1)


def create_mask_rectangle():
    image_big = skimage.io.imread("test.png")
    image = resize(image_big, (240, 300), anti_aliasing=True)
    mask = np.ones(shape=image.shape[0:2], dtype="bool")
    height, width, _ = image.shape
    start_x = int(width * 0.1)
    end_x = int(width * 0.9)
    start_y = int(height * 0.1)
    end_y = int(height-1)
    rr, cc = skimage.draw.rectangle(start=(start_y, start_x), end=(end_y, end_x))
    mask[rr, cc] = False
    mask = ~mask
    image[mask] = 0

    io.imsave('./temp.png', image)


start = time.perf_counter()
create_mask_rectangle()
print(get_colors_using_colorthief())
end = time.perf_counter()

print(f"Time: {end - start:0.4f}")