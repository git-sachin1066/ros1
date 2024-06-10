import rosbag

def extract_h264_data(input_bag_file, output_h264_file, h264_topic):
    with rosbag.Bag(input_bag_file, 'r') as bag:
        for _, msg, _ in bag.read_messages(topics=[h264_topic]):
            with open(output_h264_file, 'ab') as f:
                f.write(msg.data)

if __name__ == '__main__':
    input_bag_file = "2024-02-09-13-11-54.bag"
    output_h264_file = 'output.h264'
    bag_topic = '/interfacea/link0/image/h264'
    
    extract_h264_data(input_bag_file, output_h264_file, bag_topic)
