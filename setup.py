from setuptools import setup, find_packages

NAME = "pypixiv"
VERSION = "0.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["requests"]

setup(
    name=NAME,
    version=VERSION,

    description="Python Pixiv API",
    long_description="""\
    Unofficial Python API client based on specification extracted from Pixiv Android App v5.0.61
    """,

    author="Yukarin",
    author_email="",

    url="https://github.com/Yukariin/PyPixiv",

    keywords=["pixiv", "api", "pypixiv"],

    install_requires=REQUIRES,

    packages=find_packages()
)
