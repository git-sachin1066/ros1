import rosbag
import argparse

def extract_h264_data(input_bag_file, output_h264_file, h264_topic, timestamp_file):
    with rosbag.Bag(input_bag_file, 'r') as bag:
        with open(output_h264_file, 'ab') as h264_f, open(timestamp_file, 'w+') as ts_f:
            for topic, msg, t in bag.read_messages(topics=[h264_topic]):
                h264_f.write(msg.data)
                ts_f.write(f"{t.to_sec()}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract H264 data and timestamps from a ROS bag file.')
    parser.add_argument('input_bag_file', type=str,default = '2024-02-09-13-11-54.bag', help='Path to the input ROS bag file')
    parser.add_argument('output_h264_file', default = 'test.h264', type=str, help='Path to the output H264 file')
    parser.add_argument('h264_topic', default = '/interfacea/link0/image/h264', type=str, help='H264 topic to extract data from')
    parser.add_argument('timestamp_file', type=str,default = 'time.txt', help='Path to the output timestamp file')

    args = parser.parse_args()

    extract_h264_data(args.input_bag_file, args.output_h264_file, args.h264_topic, args.timestamp_file)
