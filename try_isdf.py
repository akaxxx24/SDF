import numpy as np
import cv2 
from matplotlib import pyplot as plt

# 替换 'file_path.npy' 为你的文件路径
isdf_file_path = '00000.npy'
our_file_path = './COLMAP_TO_ISDF/depth_colmap/00000.npy'
asd = './depth/00000.npy'

our_data = np.load(our_file_path)
isdf_data = np.load(isdf_file_path)

asd_data = np.load(asd)
print(asd_data)
## read depth image from our data
# our_data = cv2.resize(our_data, (1280, 720), interpolation=cv2.INTER_NEAREST)

# save isdf_data to csv with no scientific notation
np.savetxt('isdf_data.csv', isdf_data, fmt='%f', delimiter=',')

print(np.unique(our_data))
print(np.min(our_data))
print(np.max(our_data))

print("our data shape: ", our_data.shape)
# print("isdf data shape: ", isdf_data.shape)  # (720, 1280)

print("our data: ", our_data)
print("isdf data: ", isdf_data)
# print("our data type: ", our_data.dtype) # uint16
# print("isdf data type: ", isdf_data.dtype) # float32
