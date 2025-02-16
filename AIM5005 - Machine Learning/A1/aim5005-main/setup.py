from setuptools import setup
import os
lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = f"{lib_folder}/requirements.txt"
install_requires = [] # Here we'll add: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setup(name='aim5005',
      version='0.1',
      description='Project for Katz AIM-5005',
      url='http://github.com/mzelenetz/aim5005',
      author='Michael Zelenetz',
      author_email='michael.zelenetz@yu.edu',
      license='MIT',
      packages=['aim5005'],
      install_requires=install_requires,
      zip_safe=False)