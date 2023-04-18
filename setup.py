from setuptools import setup
from setuptools import find_packages

setup(
    name="superpoint",
    version="0.1",
    description="PyTorch pre-trained model for real-time interest point detection, description, and sparse tracking.",
    author="Nurenda Technologies",
    author_email="info@nurenda.com",
    packages=find_packages(include=["superpoint", "superpoint.*"]),
)
