from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Async library for interaction with Zoom API'
LONG_DESCRIPTION = 'Async library for interaction with Zoom API'

# Setting up
setup(
        name="aiozoom", 
        version=VERSION,
        author="Vladislav Isakov",
        author_email="vladisa88@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['aiohttp'],
        keywords=['python', 'zoom', 'async'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
