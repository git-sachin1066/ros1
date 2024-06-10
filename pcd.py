import rosbag
from sensor_msgs.msg import PointCloud2
import open3d as o3d
import numpy as np
import struct

def read_point_cloud2(data, width, height):
    fmt = 'fff'  # format for x, y, z floats
    point_step = 12  # size of one point in bytes
    points = []
    for i in range(0, len(data), point_step):
        points.append(struct.unpack_from(fmt, data, offset=i))
    return points

def extract_pointcloud2_data_to_pcd(input_bag_file, output_pcd_file, pointcloud_topic):
    with rosbag.Bag(input_bag_file, 'r') as bag:
        for _, msg, _ in bag.read_messages(topics=[pointcloud_topic]):
            points = read_point_cloud2(msg.data, msg.width, msg.height)
            np_points = np.array(points, dtype=np.float32)
            # Create an Open3D point cloud object
            point_cloud = o3d.geometry.PointCloud()
            point_cloud.points = o3d.utility.Vector3dVector(np_points)
            # Save to PCD file
            o3d.io.write_point_cloud(output_pcd_file, point_cloud)
            # break  # Assuming one message is enough for demonstration

if __name__ == '__main__':
    extract_pointcloud2_data_to_pcd('2024-02-09-13-11-54.bag', 'outputfull.pcd', '/ouster/points')
    print('done')
