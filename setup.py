from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in my_custom_app/__init__.py
from my_custom_app import __version__ as version

setup(
	name="my_custom_app",
	version=version,
	description="A simple custom Frappe app",
	author="Your Name",
	author_email="your.email@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
