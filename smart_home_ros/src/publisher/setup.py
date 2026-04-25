from setuptools import find_packages, setup

package_name = 'publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kishan',
    maintainer_email='deusmachina2026@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "temp_sensor = publisher.temp_sensor:main",
            "humidity_sensor = publisher.humidity_sensor:main",
            "motion_sensor = publisher.motion_sensor:main" 
        ],
    },
)
