# make the modular program into a package
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    

setup(
    name="aitravelplanner",
    version="0.1.0",
    packages=find_packages(),
    install_requires= requirements
)