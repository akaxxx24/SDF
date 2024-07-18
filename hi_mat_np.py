import os
import numpy as np
from scipy.io import loadmat
from matplotlib import pyplot as plt
import cv2
from scipy import ndimage

# 设置.mat文件所在的文件夹路径
mat_folder_path = './mat/'
# 设置.npy文件保存的文件夹路径
npy_folder_path = './depth_without_process/'
if not os.path.exists(npy_folder_path):
    os.makedirs(npy_folder_path)


for file in os.listdir(mat_folder_path):
    if file.endswith(".mat"):
        full_file_path = os.path.join(mat_folder_path, file)
        # 加载.mat文件
        data = loadmat(full_file_path)
        X = data['depth_image']
        tmp_str = os.path.splitext(file)[0]
        tmp_int = int(tmp_str)
        # X = X * 1000
        
        # Replace inf values with NaN for uniform handling
        # depth_data_replaced = np.where(np.isinf(X), np.nan, X)


        # depth_data_cleaned_larger = ndimage.generic_filter(depth_data_replaced, np.nanmedian, size=7)

        # nan_indices = np.argwhere(np.isnan(depth_data_cleaned_larger))
        # depth_data_cleaned_larger[nan_indices[:, 0], nan_indices[:, 1]] = 0.0
        
        # depth_data_cleaned_larger = cv2.medianBlur(depth_data_cleaned_larger, 5)
        
        
        
        npy_file_path = os.path.join(npy_folder_path, f'{tmp_int:05d}.npy')
        # np.save(npy_file_path, depth_data_cleaned_larger)
        np.save(npy_file_path, X)
        print(f"Data from {file} saved to {npy_file_path}")

        # # 假设我们要保存的变量名为'X'
        # variable_name = 'depth_image'
        # if variable_name in data:
        #     # 获取变量
        #     X = data[variable_name]
        #     # 构造.npy文件名
        #     X = X * 1000
            
        #     X[X == 0.0] = 240.0
        #     X = X.astype(np.float32)
        #     # unique value in X
        #     print(np.unique(X))
            
        #     tmp_str = os.path.splitext(file)[0]
        #     tmp_int = int(tmp_str)
        #     tmp_int = tmp_int - 1
            
            
        #     npy_file_path = os.path.join(npy_folder_path, f'{tmp_int:05d}.npy')
        #     # 保存为.npy文件
        #     np.save(npy_file_path, X)
        #     print(f"Data from {file} saved to {npy_file_path}")
        # else:
        #     print(f"Variable '{variable_name}' not found in {file}.")
