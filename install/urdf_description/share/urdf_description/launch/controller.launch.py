from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    controller_yaml = os.path.join(
        get_package_share_directory('urdf_description'),
        'launch',
        'controller.yaml'
    )

    controllers = [
        'Revolute_4_position_controller',
        'Revolute_5_position_controller',
        'Revolute_6_position_controller',
        'Revolute_7_position_controller',
        'Revolute_8_position_controller',
        'Revolute_9_position_controller',
        'Revolute_10_position_controller',
        'Revolute_11_position_controller',
        'Revolute_12_position_controller',
        'Revolute_13_position_controller',
        'Revolute_14_position_controller',
        'Revolute_15_position_controller',
        'Revolute_1_position_controller',
        'Revolute_17_position_controller',
        'Revolute_18_position_controller',
        'joint_state_broadcaster'
    ]

    controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        namespace='URDF',
        arguments=controllers,
        parameters=[controller_yaml],
        output='screen'
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        remappings=[
            ('/joint_states', '/URDF/joint_states')
        ],
        output='screen'
    )

    return LaunchDescription([
        controller_spawner,
        robot_state_publisher
    ])
