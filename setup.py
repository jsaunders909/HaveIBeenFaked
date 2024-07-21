from setuptools import setup

setup(
    name="hibf_lib",
    version="0.0.0",
    description="Python package for the have I been faked project",
    url="https://github.com/jsaunders909/HaveIBeenFaked",
    author="Jack Saunders, Isaiah Carrington, Alexandra Fuentes Mercado and Sophia Lin",
    author_email="t-jsaunders@microsoft.com",
    license="BSD 2-clause",
    install_requires=[
        "opencv-python==4.10.0.84",
        "facenet-pytorch==2.6.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
    packages=setuptools.find_packages(),
)
