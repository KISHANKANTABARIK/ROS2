# ROS2 Publisher-Subscriber Workspace

## Introduction
This repository contains a foundational ROS2 workspace demonstrating core node-to-node communication. It features a custom package with two primary nodes: a **Publisher** and a **Subscriber**. 

The publisher node generates and broadcasts data over a specific ROS2 topic, while the subscriber node listens to that exact topic and processes the incoming messages. This setup serves as a practical blueprint for handling real-time data streams and telemetry in larger robotics projects.


---
## Running the Nodes
### Step 1: Navigate to the Workspace

Open a terminal and move to the root of the ROS2 workspace:

```bash
cd ~/your_worksapce
```

Verify that you are in the correct workspace directory by checking for the `src`, `build`, `install`, and `log` folders.

### Step 2: Source the Workspace

Source the workspace setup file:

```bash
source install/setup.bash
```

This makes the custom ROS2 packages available in the current terminal session.

### Step 3: Open a Second Terminal

Open another terminal window with "ctrl + shift + i" and source the worksapce

```bash
source install/setup.bash
```

Both terminals must have the workspace sourced before running the nodes.

### Step 4: Run the Publisher and Subscriber

In the first terminal, start the publisher node:

```bash
ros2 run one_publisher one_publisher
```

In the second terminal, start the subscriber node:

```bash
ros2 run one_subscriber one_subscriber
```
<img width="1237" height="501" alt="image" src="https://github.com/user-attachments/assets/e6f2802f-d881-4e41-a917-9d37941de363" />

The publisher will begin sending messages over the topic, and the subscriber will receive and display them in real time.
<img width="1237" height="501" alt="image" src="https://github.com/user-attachments/assets/428e1758-a155-43ee-aa46-28803aefe5ce" />
