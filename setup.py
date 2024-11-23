from setuptools import setup, find_packages

setup(
    name="minotaur-labyrinth",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pygame",
    ],
    entry_points={
        "console_scripts": [
            "minotaur-labyrinth=src.Minotaur_Labyrinth:main",
        ],
    },
)
