from setuptools import find_packages, setup
from typing import List
#testing
HYPEN_E_DOT='-e.'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements
    
setup(
    name='Sensor Fault Detection',
    version='0.0.1',
    author='Mohit',
    author_email='mohitrathod723@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
