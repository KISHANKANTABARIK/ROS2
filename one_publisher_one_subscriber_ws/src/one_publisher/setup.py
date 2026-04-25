from setuptools import find_packages, setup

package_name = 'one_publisher'

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
    maintainer_email='kishan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "one_publisher = one_publisher.one_publisher:main"
            # executable = Package_name . Python_file_name:  main_function_inside_of_that_python_file
        ],
    },
)
