import random
import numpy as np
import matplotlib.image as img
from PIL import Image, ImageDraw


# def initialaising_array(path_img):
#     """Инициализация массива пикселями"""
#     # можно сразу менять разрешение изображения при его считывании (.resize(1024, 1024))
#     ismg = Image.open(path_img)
#     left, right = ismg.size
#     print(left, right, 'hdjshd')
#     img_to_matrice = img.imread(path_img)
#     print(img_to_matrice.shape)
#     # Определение цвета изображения и преображение его в двумерный массив
#     if img_to_matrice.shape[2] == 3:
#         img_mat_reshape = img_to_matrice.reshape(img_to_matrice.shape[0], -1)
#         print(img_mat_reshape)
#         print("Reshaping to 2D array:", img_mat_reshape.shape)
#     else:
#         # remain as it is
#         img_mat_reshape = img_to_matrice
#     # Разбиение изображения на 4 участка

def spliting(img_path, numb_slice):
    im = Image.open(img_path, 'r')
    #px = np.asarray(im)
    #px_array = Image.fromarray(im, 'RGB')
    #px_array.show()
    slicewidth, sliceheight = im.size

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

    #[im_open1, im_open2, im_open3, im_open4]
    return im_open4


def initializing():
    corner_numb = random.randint(1, 30)
    print(corner_numb)
    corner_coordinates = tuple(random.randint(0, 512) for i in range(corner_numb))
    print(corner_coordinates)
    pa = spliting('Testing22.png', 3)

    img0 = ImageDraw.Draw(pa)
    img0.polygon(corner_coordinates)
    pa.show()


initializing()
spliting('Testing22.png', 3)
