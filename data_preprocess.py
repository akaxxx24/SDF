import os
from pathlib import Path
from plyfile import PlyData, PlyElement

# Load .ply files from the "mesh folder"
# save the content of the .ply files in a dictionary
# key: file name, value: content of the .ply file
# e.g. {'Bone': PlyData, 'Facial_Nerver': PlyData, ...}
# The content of the .ply file is a PlyData object

def data_preprocess():

    folder_path = os.path.join(Path.cwd(), "mesh")    
    ply_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.ply'):
                ply_files.append(os.path.join(root, file))
    print(ply_files)

    ply_content = {}
    for index, ply_file in enumerate(ply_files):
        file_name = ply_file.split('/')[-1]
        key = file_name.split('.')[0]
        ply_content[key] = PlyData.read(ply_file)
    print(ply_content.keys())


def main():
    data_preprocess()

if __name__ == "__main__":
    main()