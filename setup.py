import os
from importlib import import_module
from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init = import_module(f'{package}.__init__')
    version = getattr(init, '__version__')
    return f'{version[0]}.{version[1]}.{version[2]}'


def get_long_description():
    """
    Return the README.
    """
    with open("README.rst", "r", encoding="utf8") as f:
        return f.read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]


setup(
    name="hamstr",
    version=get_version("hamstr"),
    license="MIT",
    description="Framework for gathering and aggregating data from decentralized streams.",
    long_description=get_long_description(),
    long_description_content_type="text/rst",
    author="Twan Walpot",
    author_email="twanwalpot@gmail.com",
    packages=get_packages("hamstr"),
    install_requires=[],
    include_package_data=True,
    entry_points="""
    [console_scripts]
    hamstr=hamstr.cli:main
    """,
)