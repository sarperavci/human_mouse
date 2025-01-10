from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="human_mouse",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pyautogui>=0.9.53",
        "scipy>=1.7.0"
    ],
    extras_require={
        'linux': ['python-xlib>=0.27'],
    },
    author="Sarper AVCI",
    author_email="sarperavci20@gmail.com",
    description="A package that simulates realistic human-like mouse movements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarperavci/human_mouse",
    project_urls={
        "Bug Tracker": "https://github.com/sarperavci/human_mouse/issues",
        "Documentation": "https://github.com/sarperavci/human_mouse#readme",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
    ],
    keywords="mouse, automation, human-like, movement, simulation, testing",
    python_requires=">=3.10",
) 
