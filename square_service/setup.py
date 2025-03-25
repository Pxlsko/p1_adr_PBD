from setuptools import setup, find_packages

package_name = 'square_service'

setup(
    name=package_name,
    version='0.0.1',
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
    description='Servicio que calcula el cuadrado de un número',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'square_service = square_service.square_service:main',
            'square_client = square_service.square_client:main',
        ],
    },
)
