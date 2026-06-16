# ROS2 Server-Client Workspace

## Introduction
This repository contains a foundational ROS2 workspace demonstrating core node-to-node communication. It features a custom package with two primary nodes: a **Server** and a **Client**. 
The server provide a service only when it recieve a request from a client and sent a recognition after completting the task. Here we can have a one server multiple client combination.


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

### Step 4: Run the Server and Client.

In the first terminal, start the Server node:
NOTE: the server has to go first anyhow.
```bash
ros2 run server server
```

In the second terminal, start the client node:

```bash
ros2 run client client
```
<img width="1237" height="501" alt="image" src="https://github.com/user-attachments/assets/247ce75a-cbc1-455a-8360-f5e694ce7622" />


The server will create a service and wait for client request. Once the client runs the server will accept the request and then return a approval feedback.
<img width="1237" height="501" alt="image" src="https://github.com/user-attachments/assets/1718a062-945a-4eca-b3ce-d1f45adc300e" />
