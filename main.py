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
    class_0 = []
    class_1 = []
    images = spliting('Test2.png')
    img_width, img_height = images[0].size

    for i in range(4):
        polygon_numb = random.randint(1, 10)
        # polygon_numb = 2
        # print(f'Это участок под номером {i}')
        # print("количество полигонов", polygon_numb)
        for j in range(polygon_numb):
            corner_numb = random.randint(3, 7)
            # corner_numb = 3
            # print('Количество вершин - ', corner_numb)
            corner_coordinates = tuple(random.randint(0, 512) for i in range(corner_numb*2))
            # corner_coordinates = (j*10, (j*10+1), j, 0, 1, j*20)

            if corner_numb % 2 == 0:
                """Добавление полигона в класс зданий"""
                class_0.append(corner_coordinates)
            else:
                """Добавление полигона в класс деревьев"""
                class_1.append(corner_coordinates)
            # print('Координаты - ', corner_coordinates)
            img0 = ImageDraw.Draw(images[i])
            img0.polygon(corner_coordinates)
            # images[i].show()

    print('Препятствия 0:', *class_0)
    print('Препятствия 1:', *class_1)

    new_img = Image.new('RGB', (img_width*2, img_height*2), (255, 255, 255))
    new_img.paste(images[0], (0, img_width))
    new_img.paste(images[1], (0, 0))
    new_img.paste(images[2], (img_width, 0))
    new_img.paste(images[3], (img_width, img_height))
    new_img.save(f'MergeredImg{i}.png')
    new_img.show()

    return class_0, class_1


def obstacle_data(coordinates, coors):
    """Получение данных о препятствиях"""

    coordinates = tuple(int(x) for x in coordinates.split(","))
    if coordinates in coors:
        print('ok')
        img0 = Image.open('Test2.png')
        image0 = ImageDraw.Draw(img0)
        image0.polygon(coordinates)
        img0.show()
    else:
        print('not ok')


c = initializing()
print('это', c[0])
obstacle_data(input(), c[0])
