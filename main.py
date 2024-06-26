import json
import random
from PIL import Image, ImageDraw


# import matplotlib as plt
# import math


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
    i = i + 1
    class_0 = []
    class_1 = []
    images = spliting('black_1.png')
    img_width, img_height = images[0].size

    for i in range(4):
        polygon_numb = random.randint(1, 3)

        for j in range(polygon_numb):
            corner_numb = random.randint(3, 7)
            corner_coordinates = tuple(random.randint(0, 512) for i in range(corner_numb * 2))
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

    print('Препятствия 0:', *class_0)
    print('Препятствия 1:', *class_1)

    new_img = Image.new('RGB', (img_width * 2, img_height * 2), (255, 255, 255))
    new_img.paste(images[0], (0, img_width))
    new_img.paste(images[1], (0, 0))
    new_img.paste(images[2], (img_width, 0))
    new_img.paste(images[3], (img_width, img_height))
    new_img.save(f'MergeredImg{i}.png')
    # new_img.show()
    return class_0, class_1, new_img


def convex_polygon(coordinates):
    """Построение выпуклого многоугольника"""

    """Расчет опорных точек"""
    ref_points = (coordinates[0]-2, coordinates[1]-2, coordinates[2]+2, coordinates[3]-2, coordinates[2]+2,
                  coordinates[1]+2, coordinates[0]-2, coordinates[3]+2)
    print(ref_points)
    """Построение прямоугольника"""
    image = Image.new('RGB', (1024, 1024), 'white')
    draw = ImageDraw.Draw(image)
    draw.rectangle(coordinates[0:4], 'red')
    draw.point((ref_points[0], ref_points[1]), 'black')
    image.show()
    draw.point((ref_points[2], ref_points[3]), 'black')
    image.show()
    draw.point((ref_points[4], ref_points[5]), 'black')
    image.show()
    draw.point((ref_points[6], ref_points[7]), 'black')
    image.show()
    # draw.point(ref_points, 'black')
    image.save('Rectangle.png')
    image.show()
    return image, ref_points


def line_trow_polygon(x1, y1, x2, y2, x3, y3, x4, y4):
    dot = []

    if ((y2 - y1) * (x4 - x3) - (y4 - y3) * (
            x2 - x1)) != 0:  # cчитаем определитель матрицы чтобы понять пересекаются линии или нет
        print((y2 - y1) * (x4 - x3) - (y4 - y3) * (x2 - x1))
        if (y2 - y1) != 0:  # Чтобы не было деления на ноль
            q = (x2 - x1) / (y1 - y2)
            sn = (x3 - x4) + (y3 - y4) * q
            if not sn:
                return 0
            fn = (x3 - x1) + (y3 - y1) * q
            n = fn / sn
        else:
            if not (y3 - y4):
                return 0  # b(y)
            n = (y3 - y1) / (y3 - y4)  # c(y) / b(y)

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
        'existence': None,
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


def lines_intersection(start, finish, coordinates):
    """Проверка на пересечение полигона линией"""

    # 0 - отсутствует связь между точками
    # 1 - есть связь между точками
    # 2 - отрезки совпадают
    # 3 - отрезки параллельны
    # 4 - отрезки пересекаются
    # 5 - отрезки не пересекаются

    """Инициализация координат линии и создание объектов для отрисовки"""
    x1, y1 = start[0], start[1]
    x2, y2 = finish[0], finish[1]
    points = []
    new_img1 = convex_polygon(coordinates[0:8])[0]
    fig1 = ImageDraw.Draw(new_img1)
    fig2 = ImageDraw.Draw(new_img1)
    """Подготовка массива для более удобного перебора"""
    coordinates = list(map(tuple, zip(coordinates[::2], coordinates[1::2])))

    """Создание  и инициализация матрицы смежности"""
    matrix = [0] * len(coordinates)
    print('Матрица смежности')
    for i in range(len(coordinates)):
        matrix[i] = [0] * len(coordinates)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = 0
            elif i == (len(matrix) - 1):
                matrix[len(matrix) - 1][0] = 1
                matrix[len(matrix) - 1][len(matrix) - 2] = 1
            else:
                matrix[i][i + 1] = 1
                matrix[i][i - 1] = 1
        print(matrix[i])
    print('Матрица инцидентности')

    """Проверка на пересечение, совпадение, параллельность"""
    for i in range(1, len(coordinates) + 1):
        for j in range(1, len(coordinates) + 1):
            if i != j:
                if i < len(coordinates):
                    x3, y3 = coordinates[i - 1][0], coordinates[i - 1][1]
                    x4, y4 = coordinates[i][0], coordinates[i][1]
                else:
                    x3, y3 = coordinates[i - 1][0], coordinates[i - 1][1]
                    x4, y4 = coordinates[0][0], coordinates[0][1]
                    # return 0

                denominator = (y4 - y3) * (x1 - x2) - (x4 - x3) * (y1 - y2)
                if denominator == 0:
                    if (((x1 * y2 - x2 * y1) * (x4 - x3) - (x3 * y4 - x4 * y3) * (x2 - x1) == 0) and
                            ((x1 * y2 - x2 * y1) * (y4 - y3) - (x3 * y4 - x4 * y3) * (y2 - y1) == 0)):
                        # print("Отрезки пересекаются(совпадают)")
                        matrix[i - 1][j - 1] = 2 * matrix[i - 1][j - 1]
                        # return False
                    else:
                        # print('Отрезки не пересекаются(параллельны)')
                        # return False
                        matrix[i - 1][j - 1] = 3 * matrix[i - 1][j - 1]
                else:
                    numerator_a = (x4 - x2) * (y4 - y3) - (x4 - x3) * (y4 - y2)
                    numerator_b = (x1 - x2) * (y4 - y2) - (x4 - x2) * (y1 - y2)
                    Ua = numerator_a / denominator
                    Ub = numerator_b / denominator
                    if Ua >= 0 and Ua <= 1 and Ub >= 0 and Ub <= 1:
                        x = x1 * Ua + x2 * (1 - Ua)
                        y = y1 * Ua + y2 * (1 - Ua)
                        print(x)
                        print(y)
                        points.append([x, y])
                        matrix[i - 1][j - 1] = 4 * matrix[i - 1][j - 1]
                    else:
                        # print('Не пересекаются')
                        matrix[i - 1][j - 1] = 5 * matrix[i - 1][j - 1]
                        # return False
            else:
                matrix[i - 1][j - 1] = 0

        # print(f'x{i - 1}:', x3, f'y{i - 1}:', y3)
        # print(f'x{i}:', x4, f'y{i}:', y4)

        """Отрисовка полигона с линией"""
        fig1.polygon((x1, y1, x2, y2), (255, 255, 255))
        fig2.polygon((x3, y3, x4, y4), (255, 255, 255))
        new_img1.save('Polygon_line1.png')
        print(matrix[i - 1])
    new_img1.show()
    # можно использовать yeild
    return matrix, points


def line_intersection(start, finish, point1, point2):
    """Проверка на пересечение отрезка линией"""

    # 0 - отсутствует связь между точками
    # 1 - есть связь между точками
    # 2 - отрезки совпадают
    # 3 - отрезки параллельны
    # 4 - отрезки пересекаются
    # 5 - отрезки не пересекаются

    """Инициализация координат линии и создание объектов для отрисовки"""
    x1, y1 = start[0], start[1]
    x2, y2 = finish[0], finish[1]
    points = []
    new_img1 = Image.new('RGB', (1024, 1024), (0, 0, 0))
    fig1 = ImageDraw.Draw(new_img1)
    fig2 = ImageDraw.Draw(new_img1)

    """Подготовка массива для более удобного перебора"""
    # coordinates = list(map(tuple, zip(coordinates[::2], coordinates[1::2])))
    x3, y3 = point1[0], point1[1]
    x4, y4 = point2[0], point2[1]
    denominator = (y4 - y3) * (x1 - x2) - (x4 - x3) * (y1 - y2)
    if denominator == 0:
        if (((x1 * y2 - x2 * y1) * (x4 - x3) - (x3 * y4 - x4 * y3) * (x2 - x1) == 0) and
                ((x1 * y2 - x2 * y1) * (y4 - y3) - (x3 * y4 - x4 * y3) * (y2 - y1) == 0)):
            print("Отрезки пересекаются(совпадают)")
        else:
            print('Отрезки не пересекаются(параллельны)')
    else:
        numerator_a = (x4 - x2) * (y4 - y3) - (x4 - x3) * (y4 - y2)
        numerator_b = (x1 - x2) * (y4 - y2) - (x4 - x2) * (y1 - y2)
        Ua = numerator_a / denominator
        Ub = numerator_b / denominator
        if Ua >= 0 and Ua <= 1 and Ub >= 0 and Ub <= 1:
            x = x1 * Ua + x2 * (1 - Ua)
            y = y1 * Ua + y2 * (1 - Ua)
            print('ТП1', x)
            print('ТП1', y)
            x4, y4 = x, y
            points.append(x3)
            points.append(y3)
            points.append(x4)
            points.append(y4)
        else:
            print('Не пересекаются')
    print(f'x3:', x3, f'y3:', y3)
    print(f'x4:', x4, f'y4:', y4)
    new_img1 = Image.new('RGB', (1024, 1024), (0, 0, 0))
    fig1 = ImageDraw.Draw(new_img1)
    fig2 = ImageDraw.Draw(new_img1)
    fig2.ellipse(points, (100, 100, 100))
    fig1.polygon((x1, y1, x2, y2), (255, 255, 255))
    new_img1.save('Polygon_line1.png')
    new_img1.show()
    return points


def broot_force(start, finish, coordinates):
    """Построение тракетории полета с помощью метода грубой силы(полный перебор)"""

    # for i in range(len(coordinates)):
    #     line_intersection(coordinates[i], coordinates[i+1], coordinates[i+2], coordinates[i+3])
    """Перевод координат в пиксели"""
    coordinates = initializing()
    coordinates = coordinates[1][0]
    start, finish = start * 256, finish * 256
    coordinates_px = [[coordinates[i - 1] * 256 + 1, coordinates[i] * 256 + 1] for i in
                      range(1, (len(coordinates) + 1), 2)]
    print('Переведенные в пиксели координаты:')
    for i in coordinates_px:
        print(i, '\n')

    """Инициализация графа"""
    graph = lines_intersection(start, finish, coordinates)
    for i in graph[1]:
        print(i)
    """Работа с параметром T"""
    for i in range(len(graph)):
        for j in range(len(graph)):
            # заменить на конструкцию match-case(python 3.10+)
            if graph[i][j] == 0:
                continue
            elif graph[i][j] == 1:
                continue
            elif graph[i][j] == 2:
                # отрезки совпадают
                coordinates_px[i][j] += 1 * 256
                print(coordinates_px[i][j])
            elif graph[i][j] == 3:
                # отрезки параллельны
                coordinates_px[i][j] += 0 * 256
            elif graph[i][j] == 4:
                # отрезки не пересекаются
                pass


c = initializing()
# print('проверка1:', c[1][0][0:2])
# print('проверка2:', c[1][0][2:4])
convex_polygon(c[0][0])
# line_intersection((0, 0), (1024, 1024), c[0][0][0:2], c[0][0][2:4])
# lines_intersection((0, 0), (1024, 1024), c[0][0][0:8])
# broot_force((0, 300), (500, 1000))
