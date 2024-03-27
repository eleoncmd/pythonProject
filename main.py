import random
# import numpy as np
# import matplotlib.image as img
from PIL import Image, ImageDraw


def spliting(img_path):
    """Разделение квадратного изображения на 4 равные части"""
    im = Image.open(img_path, 'r')
    # slicewidth, sliceheight = im.size

    im_sliced1 = im.crop((0, 512, 512, 1024))
    im_sliced1 = im_sliced1.save("Test3.png")
    im_open1 = Image.open("Test3.png")

    im_sliced2 = im.crop((0, 0, 512, 512))
    im_sliced2 = im_sliced2.save("Test4.png")
    im_open2 = Image.open("Test4.png")

    im_sliced3 = im.crop((512, 0, 1024, 512))
    im_sliced3 = im_sliced3.save("Test5.png")
    im_open3 = Image.open("Test5.png")

    im_sliced4 = im.crop((512, 512, 1024, 1024))
    im_sliced4 = im_sliced4.save("Test6.png")
    im_open4 = Image.open("Test6.png")
    # im_open1.show()
    # im_open2.show()
    # im_open3.show()
    # im_open4.show()
    return [im_open1, im_open2, im_open3, im_open4]


def initializing(i=0):
    """Инициализация изображения препятствиями (полигонами)"""
    i = i+1
    images = spliting('Test2.png')
    img_width, img_height = images[0].size
    for i in range(4):
        polygon_numb = random.randint(1, 20)
        print(polygon_numb)
        print(f'Это участок под номером {i}')
        for j in range(polygon_numb):
            corner_numb = random.randint(2, 30)
            print('Количество вершин - ', corner_numb)
            corner_coordinates = tuple(random.randint(0, 512) for i in range(corner_numb*2))
            print('Координаты - ', corner_coordinates)
            img0 = ImageDraw.Draw(images[i])
            img0.polygon(corner_coordinates)
            # images[i].show()

    new_img = Image.new('RGB', (img_width*2, img_height*2), (255, 255, 255))
    new_img.paste(images[0], (0, img_width))
    new_img.paste(images[1], (0, 0))
    new_img.paste(images[2], (img_width, 0))
    new_img.paste(images[3], (img_width, img_height))
    new_img.save(f'MergeredImg{i}.png')
    new_img.show()

initializing()
spliting('Testing22.png')
