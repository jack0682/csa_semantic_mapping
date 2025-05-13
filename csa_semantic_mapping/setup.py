from setuptools import setup
import os
from glob import glob

package_name = 'csa_semantic_mapping'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'msg'), glob('msg/*.msg')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'resource'), glob('resource/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Oh JaeHong',
    maintainer_email='jack0682@soongsil.ac.kr',
    description='CSA Semantic Mapping System',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'yolo_tracker_node = csa_semantic_mapping.yolo_tracker_node:main',
            'slam_pose_node = csa_semantic_mapping.slam_pose_node:main',
            'semantic_mapper = csa_semantic_mapping.semantic_mapper:main',
            'rviz_visualizer = csa_semantic_mapping.rviz_visualizer:main',
        ],
    },
)
