# Responsible for building apps as a package, so anybody can install it and use it
from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function will return list of requirements
    """
    DASH_E_DOT='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements  = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if DASH_E_DOT in requirements:
            requirements.remove(DASH_E_DOT)

    return requirements

# when installing req.txt we add -e . at the end of the file to automatically trigger the setup.py for packaging
setup(
    name='mlproject',
    version= '0.0.1',
    author='Marouane',
    author_email='marouanemasters@outlook.com',
    #to find src code and use it as a package, __init__.py is added to treat src as a package
    packages=find_packages(), 
    install_requires= get_requirements('requirements.txt')
)
