import rosbag
from sensor_msgs.msg import Imu
import csv

def extract_imu_data(input_bag_file, output_csv_file, imu_topic):
    with rosbag.Bag(input_bag_file, 'r') as bag:
        # with open(output_csv_file, 'w', newline='') as csvfile:
        #     fieldnames = ['timestamp', 'linear_acceleration_x', 'linear_acceleration_y', 'linear_acceleration_z',
        #                   'angular_velocity_x', 'angular_velocity_y', 'angular_velocity_z']
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            for _, msg, t in bag.read_messages(topics=[imu_topic]):
                # print(msg, '\n', t)
                print(msg.header.seq, '\n', t)
                print(msg.header.stamp, '\n', t)

                break



                # writer.writerow({
                #     'timestamp': t.to_nsec(),
                #     'linear_acceleration_x': msg.linear_acceleration.x,
                #     'linear_acceleration_y': msg.linear_acceleration.y,
                #     'linear_acceleration_z': msg.linear_acceleration.z,
                #     'angular_velocity_x': msg.angular_velocity.x,
                #     'angular_velocity_y': msg.angular_velocity.y,
                #     'angular_velocity_z': msg.angular_velocity.z
                # })



if __name__ == '__main__':
    extract_imu_data('2024-02-09-13-11-54.bag', 'imu.csv', '/ouster/imu')
