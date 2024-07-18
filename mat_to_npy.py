import os
import numpy as np
from scipy.io import loadmat
from matplotlib import pyplot as plt
import cv2

# 设置.mat文件所在的文件夹路径
mat_folder_path = './mat_colmap/'
# 设置.npy文件保存的文件夹路径
npy_folder_path = './COLMAP_TO_ISDF/change_scale/'
if not os.path.exists(npy_folder_path):
    os.makedirs(npy_folder_path)


for file in os.listdir(mat_folder_path):
    if file.endswith(".mat"):
        full_file_path = os.path.join(mat_folder_path, file)
        # 加载.mat文件
        data = loadmat(full_file_path)
        X = data['depth_map']
        tmp_str = os.path.splitext(file)[0]
        tmp_int = int(tmp_str)
        # plt.imshow(X)

        X = X[:540, :960]
        # np.savetxt('colmapdata.csv', X, fmt='%f', delimiter=',')
        # X = X * 10
          
        indices_too_small = np.argwhere(X < 11)
        X[indices_too_small[:, 0], indices_too_small[:, 1]] = 18
        
        indices_too_big = np.argwhere(X >= 30)
        X[indices_too_big[:, 0], indices_too_big[:, 1]] = 18
        
        
        nan_indices = np.argwhere(np.isnan(X))
        X[nan_indices[:, 0], nan_indices[:, 1]] = 0.0
        
        # need to smooth the depth map to remove the noise

        X = cv2.medianBlur(X, 5)
        X = cv2.medianBlur(X, 5)
        
        X = X * 10
        
        
        
        npy_file_path = os.path.join(npy_folder_path, f'{tmp_int:05d}.npy')
        np.save(npy_file_path, X)
        print(f"Data from {file} saved to {npy_file_path}")
