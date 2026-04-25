import time
from roslibpy import Ros, Topic, Message

# 1. Connect to the ROS 2 machine
# Replace '192.168.1.' with your robot's actual IP
client = Ros(host='172.29.37.194',port=9090)

def run_example():
    client.run()
    print(f"Is connected: {client.is_connected}")

    # --- PUBLISHING EXAMPLE ---
    # Define the topic, name, and message type
    talker = Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/Twist')
    
    def send_data():
        msg = Message({
            'linear': {'x': 0.5, 'y': 0.0, 'z': 0.0},
            'angular': {'z': 0.1}
        })
        talker.publish(msg)
        print("Published movement command.")

    # --- SUBSCRIBING EXAMPLE ---
    listener = Topic(client, '/temperature_data', 'sensor_msgs/Temperature')
    
    def callback(message):
        print(f"Received Temp: {message['temperature']}°C")

    listener.subscribe(callback)

    try:
        while True:
            send_data()
            time.sleep(1)
    except KeyboardInterrupt:
        client.terminate()

if __name__ == '__main__':
    run_example()


