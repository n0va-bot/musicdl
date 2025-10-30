from setuptools import setup, find_packages

setup(
    name='musicdl',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'musicdl = musicdl.__main__:main',
        ],
    },
)
