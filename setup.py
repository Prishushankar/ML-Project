from setuptools import find_packages, setup
from typing import List

def get_requirement(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='Mlproject',
    version='0.0.1',
    author='Priyanshu',
    author_email='prishushankar@gmail.com',  # Correct the email format
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt'),
)
