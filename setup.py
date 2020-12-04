from setuptools import setup, find_packages
import re


packages = find_packages(where='src')
print(packages)
install_requires= open('requirements.txt').read().splitlines()

setup()
