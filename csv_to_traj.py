import pandas as pd
import numpy as np
from scipy.spatial.transform import Rotation as R

# Load the CSV file to check its structure and content
csv_file_path = './csv/01-zedm-zed_node-pose_with_covariance.csv'
zed_data = pd.read_csv(csv_file_path)


# Function to convert quaternion DataFrame to scipy Rotation object
def quaternion_to_rotation(q):
    return R.from_quat([q['.pose.pose.orientation.x'], q['.pose.pose.orientation.y'],
                        q['.pose.pose.orientation.z'], q['.pose.pose.orientation.w']])



# Function to create a 4x4 transformation matrix from pose data
def create_transformation_matrix(row):
    row_rotation = quaternion_to_rotation(row)
    rotation_matrix = row_rotation.as_matrix()
    
    translation_vector = [row['.pose.pose.position.x'] / 100.0, 
                          row['.pose.pose.position.y'] / 100.0, 
                          row['.pose.pose.position.z'] / 100.0]

    # Create a 4x4 transformation matrix
    transformation_matrix = np.eye(4)
    transformation_matrix[:3, :3] = rotation_matrix
    transformation_matrix[:3, 3] = translation_vector
    return transformation_matrix.ravel().tolist()

# Apply transformation to all rows and create the 4x4 matrix
transformation_matrix_data = zed_data.apply(create_transformation_matrix, axis=1)
transformation_matrix_df = pd.DataFrame(transformation_matrix_data.tolist(), 
                                        columns=[f"m{i//4+1}{i%4+1}" for i in range(16)])


formatter = "{:.6f}".format

# Apply this formatter to all elements in the DataFrame except for the 'timestamp' column
for column in transformation_matrix_df.columns[:]:
    transformation_matrix_df[column] = transformation_matrix_df[column].map(formatter)

corrected_output_file_path = './traj_2/traj.txt'
transformation_matrix_df.to_csv(corrected_output_file_path, header=False, index=True, sep=' ', mode='w', float_format="%.6")

print("Transformation matrix data saved to:", corrected_output_file_path)
