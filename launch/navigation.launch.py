"""Start Nav2 with the maze map and local parameter file."""

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    PathJoinSubstitution(
                        [FindPackageShare("nav2_bringup"), "launch", "bringup_launch.py"]
                    )
                ),
                launch_arguments={
                    "map": PathJoinSubstitution(
                        [FindPackageShare("turtlebot3_maze_navigation"), "maps", "maze.yaml"]
                    ),
                    "params_file": PathJoinSubstitution(
                        [
                            FindPackageShare("turtlebot3_maze_navigation"),
                            "config",
                            "nav2_params.yaml",
                        ]
                    ),
                    "use_sim_time": "True",
                }.items(),
            )
        ]
    )
