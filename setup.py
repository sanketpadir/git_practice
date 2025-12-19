from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []

    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Sanket",
    author_email="sanketpadir2000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
