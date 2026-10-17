"""Launch Gazebo with the maze world and a TurtleBot3."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    world = PathJoinSubstitution(
        [FindPackageShare("turtlebot3_maze_navigation"), "worlds", "maze.world"]
    )
    return LaunchDescription(
        [
            DeclareLaunchArgument("world", default_value=world),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    PathJoinSubstitution(
                        [FindPackageShare("gazebo_ros"), "launch", "gazebo.launch.py"]
                    )
                ),
                launch_arguments={"world": LaunchConfiguration("world")}.items(),
            ),
        ]
    )
