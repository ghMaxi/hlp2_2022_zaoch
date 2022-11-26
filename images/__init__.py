from PIL import Image
image_size = 426


def _cut_in_squares(save_tests=False):
    atlas_path = "images/2560px-Chess_Pieces_Sprite.png"
    if save_tests:
        from os.path import isdir
        from os import mkdir
        if not isdir('test'):
            mkdir('test')

    atlas = Image.open(atlas_path).convert('RGBA')
    raw_images = []
    high_y = 0
    for _ in range(2):
        low_y = high_y
        high_y = low_y + image_size
        high_x = 0
        for _ in range(6):
            low_x = high_x
            high_x = low_x + image_size
            figure = atlas.crop((low_x, low_y, high_x, high_y))
            if save_tests:
                figure.save(f"test\\img{low_x}_{low_y}.png")
            raw_images.append(figure)
    return raw_images


images = dict(zip(('wK', 'wQ', 'wB', 'wH', 'wR', 'wp',
                   'bK', 'bQ', 'bB', 'bH', 'bR', 'bp',),
              _cut_in_squares()))
from pprint import pprint
pprint(images)

if __name__ == "__main__":
    _cut_in_squares(save_tests=True)
