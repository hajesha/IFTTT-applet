import time
from colorthief import ColorThief


def get_colors_using_colorthief():
    color_thief = ColorThief('test.png')
    return color_thief.get_color(quality=1)


start = time.perf_counter()
print(get_colors_using_colorthief())
end = time.perf_counter()