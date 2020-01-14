from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="waveshare_rpi",
    version="0.1.0",
    author="Eli Barnett",
    author_email="emichaelbarnett@gmail.com",
    description=("A quick-and-dirty library wrapping the native API of the "
                 "waveshare GPS hat."),
    license="MIT",
    keywords="waveshare rpi gps",
    url="http://packages.python.org/waveshare_rpi",
    packages=['waveshare'],
    long_description=long_description,
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "pynmea2",
        "pyserial"
    ]
)
