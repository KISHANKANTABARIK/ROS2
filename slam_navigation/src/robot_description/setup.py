from setuptools import setup
import os
from glob import glob

package_name = 'robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Install launch files
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')),
        # Install urdf files
        (os.path.join('share', package_name, 'urdf'),
            glob('urdf/*')),
        # Install rviz files
        (os.path.join('share', package_name, 'rviz'),
            glob('rviz/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adem-vishal',
    maintainer_email='ademvishal50@gmail.com',
    description='Robot description package containing URDF/xacro and RViz config',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
