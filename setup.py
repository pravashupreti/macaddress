from setuptools import setup, find_packages

import macaddress

setup(
    name="macaddress",
    version=macaddress.__version__,
    author="Pravash Upreti",
    packages=find_packages(),
    description="A simple CLI tool to fetch the device info using mac address",
    py_modules=["macaddress"],
    install_requires=["Click==8.1", "requests==2.28.1"],
    entry_points="""
        [console_scripts]
        macaddress=macaddress.cli:cli
    """,
)
