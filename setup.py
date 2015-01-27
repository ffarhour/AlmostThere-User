import os
from setuptools import setup, find_packages

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

setup(

		name = "User",
		packages=find_packages(),
		include_package_data=True,
		install_requires =['Django']
		)
