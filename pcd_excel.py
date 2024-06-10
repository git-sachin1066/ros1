import rosbag
from sensor_msgs.msg import PointCloud2
import csv
import struct

def read_point_cloud2(data):
    fmt = 'fff'  # format for x, y, z floats
    point_step = 12  # size of one point in bytes
    for i in range(0, len(data), point_step):
        yield struct.unpack_from(fmt, data, offset=i)

def extract_pointcloud2_data(input_bag_file, output_csv_file, pointcloud_topic):
    with rosbag.Bag(input_bag_file, 'r') as bag:
        with open(output_csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['x', 'y', 'z'])  # CSV header
            for _, msg, _ in bag.read_messages(topics=[pointcloud_topic]):
                for point in read_point_cloud2(msg.data):
                    writer.writerow(point)

if __name__ == '__main__':
    extract_pointcloud2_data('2024-02-09-13-11-54.bag', 'point.csv', '/ouster/points')
