import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import pathlib


print(os.getcwd())
# 设置文件夹路径
# folder_path = '../COLMAP_TO_ISDF/new_depth_by_10/'
# d_path = '../COLMAP_TO_ISDF/new_depth_normalize/'
# using pathlib to get the current path


files = sorted([f for f in os.listdir(folder_path) if f.endswith('.npy')])

# 初始化用于存储全局最小和最大值的变量
global_min = np.inf
global_max = -np.inf

# 第一次遍历：寻找全局最小和最大值
for filename in files:
    file_path = os.path.join(folder_path, filename)
    # 加载NumPy数组
    array = np.load(file_path)
    
    # 更新全局最小和最大值
    global_min = min(global_min, np.min(array))
    global_max = max(global_max, np.max(array))

# 第二次遍历：标准化所有数组
for filename in files:
    file_path = os.path.join(folder_path, filename)
    # 加载NumPy数组
    array = np.load(file_path)
    
    # 数据标准化
    normalized_array = (array - global_min) / (global_max - global_min)
    
    # 可选：保存标准化后的数组
    np.save(os.path.join(d_path, filename), normalized_array)

