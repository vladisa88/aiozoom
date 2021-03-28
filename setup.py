from os import path
from setuptools import setup, find_packages

directory = path.abspath(path.dirname(__file__))
with open(path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

VERSION = '0.0.9'
DESCRIPTION = 'Async library for interaction with Zoom API'
LONG_DESCRIPTION = 'Async library for interaction with Zoom API.\n' \
                    'It allows you to create, get, stop meetings ' \
                    'and you can get statistics of past meeting'

# Setting up
setup(
        name="aiozoom",
        version=VERSION,
        author="Vladislav Isakov",
        author_email="vladisa88@gmail.com",
        url="https://github.com/vladisa88/aiozoom",
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=['aiohttp'],
        keywords=['python', 'zoom', 'async'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Operating System :: OS Independent",
            "Topic :: Internet",
            "Topic :: Office/Business",
            "Topic :: Software Development :: Libraries",
        ]
)
