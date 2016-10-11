import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="nmap-utils",
    version="0.0.1",
    author="Sachin S Kamath",
    author_email="sskamath96@gmail.com",
    description=("Utility to automate pen-tests using nmap output files"),
    license="BSD",
    packages = find_packages(),
    install_requires = ['python-libnmap'],
    keywords="python nmap security xml pen-test",
    url="http://github.com/sachinkamath/nmap-utils",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
