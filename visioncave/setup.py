from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in visioncave/__init__.py
from visioncave import __version__ as version

setup(
    name="visioncave",
    version=version,
    description="A Frappe app for Computer Vision tasks.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
