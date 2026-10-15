# IE4060 – Autonomous Navigation of TurtleBot3 Burger

## Project Overview

This project develops an autonomous navigation system for a TurtleBot3 Burger robot in a custom maze environment using Gazebo and ROS 2 Jazzy.

## Project Objectives

- Create a custom maze environment in Gazebo based on the assignment requirements.
- Map the maze using SLAM or an appropriate mapping method.
- Implement autonomous path planning and navigation using ROS 2 Nav2.
- Allow users to select navigation goals on the map.
- Develop and evaluate a Deep Q-learning approach.
- Evaluate navigation performance using travel time, path length, goal completion, and obstacle avoidance.

## Technologies

- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- Gazebo Sim
- TurtleBot3 Burger
- SLAM Toolbox
- Nav2
- Python

## Repository Structure

```text
IE4060-TurtleBot3-Autonomous-Navigation/
├── config/           # Navigation and robot configuration
├── deep_q_learning/  # Deep Q-learning implementation
├── docs/             # Project report and documentation
├── launch/           # ROS 2 launch files
├── maze_world/       # Gazebo maze world and map files
│   └── maps/
├── results/          # Screenshots and evaluation results
├── src/              # ROS 2 source packages
├── DEPENDENCIES.md   # Environment and dependency notes
└── README.md
```

## Team Workflow

1. Agree on tasks with the team before modifying shared files.
2. Pull the latest changes before starting work.
3. Test changes in the ROS 2 Jazzy environment.
4. Commit related changes with clear messages.
5. Push changes to GitHub and communicate any issues to the team.

## Project Status

Initial repository structure created. Simulation, mapping, navigation, and Deep Q-learning implementation are in progress.

## Academic Context

IE4060 – Robotics and Intelligent Systems  
BSc (Hons) in Information Technology  
Sri Lanka Institute of Information Technology (SLIIT)
