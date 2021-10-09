from setuptools import find_packages, setup

setup(
    name='example',
    version='0.0.0',
    packages=find_packages(where="src"),
    url='',
    license='',
    author='bn',
    author_email='bjrnfrdnnd@gmail.com',
    description='',
    install_requires=['pandas'],
    extras_require=dict(tests=['pytest']),
    package_dir={"": "src"},
    package_data={
        'example': ['../../data/*', '../../config/*'],
    },
)
