import os
import numpy as np
from scipy.io import loadmat
from matplotlib import pyplot as plt
import cv2
from scipy import ndimage


# 替换 'file_path.npy' 为你的文件路径
# isdf_file_path = '00000.npy'

# isdf_data = np.load(isdf_file_path)

# np.savetxt('isdf_data.csv', isdf_data, fmt='%f', delimiter=',')
# print("isdf data: ", isdf_data)


hi_original = 'normalize_hi.npy'
hi_original_data = np.load(hi_original)
# np.savetxt('hi_original_data.csv', hi_original_data, fmt='%f', delimiter=',')
print("hi_original_data: ", hi_original_data)

