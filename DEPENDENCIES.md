# Dependencies and Development Environment

## Target environment

- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- TurtleBot3 Burger
- Gazebo Sim 8 (verify ROS integration)
- Nav2
- SLAM Toolbox
- RViz2
- Python 3 and colcon

## Project requirements

1. Gazebo maze simulation and TurtleBot3 model.
2. ROS 2 communication between Gazebo and the robot.
3. SLAM mapping and saved map files.
4. Nav2 path planning and goal execution.
5. Clicked-goal selection using an appropriate ROS 2 interface.
6. Deep Q-learning implementation and evaluation.

## Current environment status

Verified:
- Ubuntu 24.04.4 LTS
- ROS 2 Jazzy
- Gazebo Sim 8.11.0
- Nav2 packages
- SLAM Toolbox
- TurtleBot3 core packages

Still to verify:
- Gazebo ROS integration packages
- TurtleBot3 Gazebo-compatible simulation setup
- Python machine-learning dependencies
- End-to-end simulation and navigation

## Installation policy

Check the installed ROS 2 packages before installing anything.
Follow the project's README and package.xml files once the
implementation is available. Do not install arbitrary package
versions without checking compatibility with Ubuntu 24.04 and
ROS 2 Jazzy.
