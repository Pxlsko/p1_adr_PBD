from setuptools import find_packages, setup

package_name = 'drone_position'

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
    maintainer='student',
    maintainer_email='pablolusb@gmail.com',
    description='Publicador y suscriptor de posición GPS para un dron',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'uav_publisher = drone_position.uav_publisher:main',  
            'uav_subscriber = drone_position.uav_subscriber:main',
        ],
    },
)
