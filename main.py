import numpy as np
import matplotlib.image as img


def initialaising_array(path_img):
    """Инициализация массива пикселями"""
    # можно сразу менять разрешение изображения при его считывании (.resize(1024, 1024))
    img_to_matrice = img.imread(path_img)
    print(img_to_matrice.shape)
    # Определение цвета изображения
    if img_to_matrice.shape[2] == 3:
        img_mat_reshape = img_to_matrice.reshape(img_to_matrice.shape[0], -1)
        print("Reshaping to 2D array:",
              img_mat_reshape.shape)
    else:
        # remain as it is
        img_mat_reshape = img_to_matrice
    df_matrice = pd.Data
