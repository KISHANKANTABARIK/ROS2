# Catch Them All - ROS2 Turtlesim Project

## Introduction

**Catch Them All** is a ROS2-based project built using the Turtlesim simulator. The objective is to control a hunter turtle that automatically chases and catches randomly spawned turtles within the simulation environment.

The project demonstrates fundamental ROS2 concepts including:

* Publisher and Subscriber communication
* Custom ROS2 Services
* Client-Server architecture
* Coordinate tracking and motion control
* Multi-node interaction by launch files.

As new turtles appear in the simulation, the hunter turtle calculates their position, navigates toward them, and removes them from the environment once caught.

---

## Project Structure

The project consists of multiple ROS2 nodes working together:

* **Turtle Controller Node** – Controls the movement of the hunter turtle to track the spawned turtle and finally reuest to kill the spawned turtle.
* **Spawner Node** – Generates turtles at random positions
* **Turtlesim Node** – Provides the simulation environment, also provide a kill service to remove a turtle once the hunter catches it.
* **Turtle bringup** - A launch file to run all three nodes at once.

---

## Running the Project

### Step 1: Navigate to the Workspace

Open a terminal and move to the ROS2 workspace:

```bash
cd ~/your_workspace
```

---

### Step 2: Build the Workspace

```bash
colcon build
```

---

### Step 3: Source the Workspace

```bash
source install/setup.bash
```

---

### RUN BY NODE

Repeat the steps for two more terminals 

Now in the first terminal we will run the turtlesim_node example from ROS2.
<img width="954" height="497" alt="Screenshot from 2026-06-18 19-48-40" src="https://github.com/user-attachments/assets/c194815e-de3d-4b80-8be5-51a862dc0c60" />

In the second terminal we will run the spawner node
<img width="959" height="506" alt="image" src="https://github.com/user-attachments/assets/c313c301-fd49-479a-bb15-13cc8068cc05" />

The third terminal run the controller node
<img width="1120" height="505" alt="image" src="https://github.com/user-attachments/assets/f6cfd7f4-aa0d-4ab7-859c-6a27c61ce9a2" />

note: Follw the order mentioned as the files can only work properly in that order as they depend on services that were created by other.

### RUN BY LAUNCH

Instead of having tu run three different nodes we can just launch a single bringup file that will internally run the three nodes in the correct order.

To launch the bringup file first follow through step one to step three.

Then use the cli for launch file.
<img width="1120" height="505" alt="image" src="https://github.com/user-attachments/assets/c3025870-5ba0-4d75-aedd-3cf518696f0a" />

