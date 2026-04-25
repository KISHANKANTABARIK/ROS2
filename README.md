# ROS2 Humble - Projects & Basics

Welcome to the **ROS2 Humble** repository! This is a comprehensive collection of ROS2 projects, examples, and practical implementations covering core concepts and advanced applications.

## 📋 Repository Overview

This repository contains all projects and basics of ROS2 (Humble distribution), including:
- Publisher/Subscriber patterns
- Server/Client architecture
- Advanced robotics control
- Simulation with Gazebo and URDF
- Navigation and SLAM
- Smart home applications
- Motor control systems
- Sensor fusion
- MicroROS with ESP32

---

## 📁 Project Structure

### **1. Core Communication Patterns**
- **`one_publisher_one_subscriber_ws/`** - Basic pub/sub implementation to understand ROS2 communication
- **`server_client_ws/`** - Service-based communication using ROS2 services

### **2. Control & Motor Systems**
- **`ros2_control_ws/`** - Integration with ros2_control framework for hardware control
- **`motor_status_ws/`** - Motor status monitoring and control

### **3. Simulation & Visualization**
- **`ros_gazebo_urdf/`** - Gazebo simulation with URDF robot models
- **`turtlesim_catch_them_all_ws/`** - Interactive turtlesim game example

### **4. Navigation & Mapping**
- **`slam_navigation/`** - SLAM (Simultaneous Localization and Mapping) and navigation stack

### **5. Embedded Systems**
- **`micro_ros_esp_ws/`** - MicroROS integration with ESP32 microcontroller

### **6. Sensor Integration**
- **`ros_fusion/`** - Sensor fusion implementations

### **7. IoT Applications**
- **`smart_home_ros/`** - Smart home automation using ROS2

### **8. Learning Resources**
- **`python_practice/`** - Python programming exercises and practice

---

## 🚀 Quick Start Guide

### Prerequisites
- ROS2 Humble installed
- Python 3.10+
- Colcon build system

### Essential ROS2 Commands

#### Creating and Building Packages
```bash
# Create a new ROS2 package
ros2 pkg create --build-type ament_python <package_name>

# Build all packages
colcon build

# Build specific package
colcon build --packages-select <package_name>

# Source the installation
source install/setup.bash
```

#### Running Nodes
```bash
# Run a node
ros2 run <package_name> <executable_name>

# List all running nodes
ros2 node list
```

#### Topic Communication
```bash
# Publish to a topic
ros2 topic pub "<topic_name>" <topic_type> "{<data>: \"<value>\"}"

# Subscribe to a topic
ros2 topic echo "<topic_name>"

# List all topics
ros2 topic list
```

#### Service Communication
```bash
# Call a service
ros2 service call <service_name> <service_type> "{<args>}" 

# List all services
ros2 service list
```

#### Interface Management
```bash
# List all available interfaces
ros2 interface list

# Search for specific interface
ros2 interface list | grep <interface_name>

# Show interface details
ros2 interface show <interface_name>
```

#### Domain ID Configuration
```bash
# Set ROS domain ID (for network isolation)
export ROS_DOMAIN_ID=<ID_number>

# Make it permanent - add to ~/.bashrc
echo \"export ROS_DOMAIN_ID=<ID_number>\" >> ~/.bashrc
```

#### System Debugging
```bash
# List all processes
ps aux

# List ROS-related processes
ps aux | grep ros

# Kill a process
kill -9 <PID>

# Auto-complete topic names
ros2 topic echo <TAB><TAB>
```

---

## 📚 Project Details

Each workspace is self-contained and demonstrates different ROS2 concepts:

| Project | Purpose | Key Concepts |
|---------|---------|--------------|
| `one_publisher_one_subscriber_ws` | Basic communication | Pub/Sub, Topics |
| `server_client_ws` | Service-based communication | Services, Requests/Responses |
| `ros2_control_ws` | Hardware control framework | Controllers, Actuators |
| `motor_status_ws` | Motor monitoring | Sensor feedback, Status publishing |
| `ros_gazebo_urdf` | Robot simulation | URDF, Gazebo, Physics |
| `turtlesim_catch_them_all_ws` | Interactive game | Turtlesim, Animation |
| `slam_navigation` | Robot navigation | SLAM, Nav2 stack |
| `micro_ros_esp_ws` | Embedded systems | MicroROS, ESP32 |
| `ros_fusion` | Multi-sensor fusion | Sensor integration |
| `smart_home_ros` | IoT automation | ROS2 in real-world apps |

---

## 🛠️ Development Workflow

1. **Navigate to project workspace**
   ```bash
   cd <project_name>_ws
   ```

2. **Build the workspace**
   ```bash
   colcon build
   ```

3. **Source the environment**
   ```bash
   source install/setup.bash
   ```

4. **Run the nodes**
   ```bash
   ros2 run <package_name> <executable_name>
   ```

5. **Monitor with ROS2 CLI tools**
   ```bash
   ros2 topic list
   ros2 topic echo /topic_name
   ```

---

## 📖 Learning Path

1. Start with **`one_publisher_one_subscriber_ws`** to understand basic pub/sub
2. Move to **`server_client_ws`** for service-based communication
3. Explore **`ros_gazebo_urdf`** for simulation
4. Study **`ros2_control_ws`** for hardware integration
5. Advance to **`slam_navigation`** for autonomous navigation

---

## 🔗 Useful Resources

- [ROS2 Official Documentation](https://docs.ros.org/en/humble/)
- [ROS2 Control Framework](https://control.ros.org/)
- [Gazebo Simulator](http://gazebosim.org/)
- [Nav2 Navigation Stack](https://navigation.ros.org/)

---

## 📝 Command Reference File

See **`ros_command.txt`** for a comprehensive list of ROS2 commands and usage examples.

---

## 📄 License

This repository is for educational and learning purposes.

---

## 🤝 Contributing

Feel free to fork, modify, and improve these examples. Share your improvements!

---

**Last Updated:** 2026-04-25 14:20:32  
**ROS2 Distribution:** Humble  
**Language:** Python

---

*Happy ROS2 Learning!* 🤖