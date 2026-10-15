# TurtleBot3 Autonomous Navigation

This package is a starter layout for a ROS 2 TurtleBot3 maze-navigation project.

## Layout

- `worlds/maze.world` - Gazebo maze world.
- `launch/simulation.launch.py` - Starts Gazebo with the maze.
- `launch/slam.launch.py` - Starts SLAM Toolbox.
- `launch/navigation.launch.py` - Starts Nav2 with the saved map.
- `config/nav2_params.yaml` - Nav2 parameters.
- `maps/` - Map metadata and image.
- `dqn/` - DQN training and evaluation entry points.

## Usage

After placing this directory in a ROS 2 workspace and adding the package metadata:

```bash
ros2 launch turtlebot3_maze_navigation simulation.launch.py
ros2 launch turtlebot3_maze_navigation slam.launch.py
ros2 launch turtlebot3_maze_navigation navigation.launch.py
```

The DQN scripts are intentionally scaffolds until a Gymnasium environment and
policy implementation are selected.
