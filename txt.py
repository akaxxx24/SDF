import os
import numpy as np
import pandas as pd

#read the txt file
txt_folder_path = './camera_base.txt'
txt = pd.read_csv(txt_folder_path, sep=' ', header=None)
# 5th column values / 100
txt[4] = txt[4] / 10
txt[8] = txt[8] / 10
txt[12] = txt[12] / 10

txt.to_csv('./camera_base_10.txt', sep=' ', index=False, header=False)
