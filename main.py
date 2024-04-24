import json
import random
# import numpy as np
# import matplotlib.image as img
from PIL import Image, ImageDraw, ImageColor
# import json


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
    images = spliting('black_1.png')
    img_width, img_height = images[0].size

    for i in range(4):
        polygon_numb = random.randint(1, 10)

        for j in range(polygon_numb):
            corner_numb = random.randint(3, 7)
            corner_coordinates = tuple(random.randint(0, 512) for i in range(corner_numb*2))
            # corner_coordinates = (j*10, (j*10+1), j, 0, 1, j*20)

            if corner_numb % 2 == 0:
                """Добавление полигона в класс зданий"""
                class_0.append(corner_coordinates)
            else:
                """Добавление полигона в класс деревьев"""
                class_1.append(corner_coordinates)

            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            img0 = ImageDraw.Draw(images[i])
            img0.polygon(corner_coordinates, color)
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

    return class_0, class_1, new_img


def obstacle_data_1(coordinates, coors):
    """Получение данных о препятствиях - первый вариант"""

    coordinates = tuple(int(x) for x in coordinates.split(","))


def line_trow_polygon(x1, y1, x2, y2, x3, y3, x4, y4):
    dot = []

    if ((y2-y1)*(x4-x3) - (y4-y3)*(x2-x1)) != 0:  # cчитаем определитель матрицы чтобы понять пересекаются линии или нет
        print((y2-y1)*(x4-x3) - (y4-y3)*(x2-x1))
        if (y2 - y1) != 0:  # Чтобы не было деления на ноль
            q = (x2 - x1)/(y1-y2)
            sn = (x3 - x4) + (y3 - y4)*q
            if not sn:
                return 0
            fn = (x3 - x1) + (y3 - y1) * q
            n = fn/sn
        else:
            if not (y3 - y4):
                return 0  # b(y)
            n = (y3 - y1)/(y3 - y4)  # c(y) / b(y)

        dot.append(x3 + (x4 - x3) * n)
        dot.append(y3 + (y4 - y3) * n)
        new_img1 = Image.new('RGB', (1024, 1024), (0, 0, 0))
        fig1 = ImageDraw.Draw(new_img1)
        fig2 = ImageDraw.Draw(new_img1)
        fig2.polygon((x3, y3, x4, y4), (100, 100, 100))
        fig1.polygon((x1, y1, x2, y2), (255, 255, 255))
        new_img1.save('Polygon_line.png')
        new_img1.show()
        print(1)
        print(dot[0], dot[1])
        return dot[0], dot[1]

def obstacle_data_2(inp_coordinates, test_coordinates):
    """Получение данных о препятствиях - второй вариант"""

    info = {
    'corner_numb': None,
    'existence'  : None,
    'coordinates': None
    }

    if type(inp_coordinates) == "<class 'tuple'>":
        print('все сходится')
    else:
        ds = type(inp_coordinates)
        print('тип', ds)
        inp_coordinates = tuple(int(x) for x in inp_coordinates.split(","))
        if inp_coordinates in test_coordinates:
            info['corner_numb'] = len(inp_coordinates)
            info['existence'] = 'Yes'
            info['coordinates'] = inp_coordinates
        else:
            info['corner_numb'] = len(inp_coordinates)
            info['coordinates'] = inp_coordinates
    with open('json_file.txt', 'w') as f:
        f.write(json.dumps(info))
    with open('json_file.txt') as f:
        print(f.read())


def new_metgod(coordinates):
    coordinates_polygon = []
    print(len(coordinates))
    x1, y1 = 30, 20
    x2, y2 = 1000, 1000
    new_img1 = Image.new('RGB', (1024, 1024), (0, 0, 0))
    fig1 = ImageDraw.Draw(new_img1)
    fig2 = ImageDraw.Draw(new_img1)
    for i in range(0, len(coordinates)+2, 2):
        print(i)
        if (i + 3) < (len(coordinates)):
            x3, y3 = coordinates[i], coordinates[i+1]
            x4, y4 = coordinates[i+2], coordinates[i+3]
            denominator = (y4 - y3) * (x1 - x2) - (x4 - x3) * (y1 - y2)
            if denominator == 0:
                if ((x1 * y2 - x2 * y1) * (x4 - x3) - (x3 * y4 - x4 * y3) * (x2 - x1) == 0) and ((x1 * y2 - x2 * y1) * (y4 - y3) - (x3 * y4 - x4 * y3) * (y2 - y1) == 0):
                    print("Отрезки пересекаются(совпадают)")
                    # return False
                else:
                    print('Отрезки не пересекаются(параллельны)')
                    # return False
            else:
                numerator_a = (x4 - x2) * (y4 - y3) - (x4 - x3) * (y4 - y2)
                numerator_b = (x1 - x2) * (y4 - y2) - (x4 - x2) * (y1 - y2)
                Ua = numerator_a / denominator
                Ub = numerator_b / denominator
                if Ua >= 0 and Ua <= 1 and Ub >= 0 and Ub <= 1:
                    x = x1 * Ua + x2 * (1 - Ua)
                    y = y1 * Ua + y2 * (1 - Ua)
                    print(x, "\n", y)
                else:
                    print('Не пересекаются')
                    # return False
        else:
            x3, y3 = coordinates[i], coordinates[i+1]
            x4, y4 = coordinates[0], coordinates[1]
            # return 0

        """Отрисовка полигона с линией"""
        fig2.polygon((x3, y3, x4, y4), (255, 255, 255))
        fig1.polygon((x1, y1, x2, y2), (255, 255, 255))
        new_img1.save('Polygon_line1.png')
        new_img1.show()

"""def trajectory(x1,y1,x2,y2):
    res = new_metgod(x1, y1, x2, y2)
    T = [0,1]
    Проверка на пересечение
    if res:
        pass
    Проверка на совпадение
    if res == 'Отрезки пересекаются(совпадают)':
        return False

"""
c = initializing()

# line_trow_polygon(60,1,17, 14,11,7,12,13)

new_metgod(c[1][0])
# print('это', c[0])
# obstacle_data_1(input(), c[0])
# obstacle_data_2(input(), c[0])

