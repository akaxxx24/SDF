from mesh_to_sdf import sample_sdf_near_surface
from mesh_to_sdf import mesh_to_voxels
from pathlib import Path
import os
import glob
import trimesh
import numpy as np

def mesh_to_sdf():
    
    print("hello")
    folder_path = os.path.join(Path.cwd(), "mesh")
    ply_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.ply'):
                ply_files.append(os.path.join(root, file))

    ply_content = {}
    for index, ply_file in enumerate(ply_files):
        file_name = ply_file.split('/')[-1]
        key = file_name.split('.')[0]
        ply_content[key] = ply_file

    #dict_keys(['Bone', 'Facial_Nerve'])
    #{'Bone': '/Users/chenxingyu/SDF/mesh/Bone.ply', 'Facial_Nerve': '/Users/chenxingyu/SDF/mesh/Facial_Nerve.ply'}

    # Load the mesh
    meshes_xyz = {}
    meshes_sdf = {}
    for key, filename in ply_content.items():
        mesh = trimesh.load(os.path.abspath(filename), force='mesh')
        # Sample points near the surface
        xyz, sdf = sample_sdf_near_surface(mesh, number_of_points=100000)
        meshes_xyz[key] = xyz
        meshes_sdf[key] = sdf
    
def main():
    mesh_to_sdf()

if __name__ == "__main__":
    main()