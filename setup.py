from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='steganosort',
    license='GPLv3',
    url='https://github.com/sz3/steganosort',
    version='0.1.0',

    entry_points={
        'console_scripts': [
            'steganosort = steganosort:main',
        ],
    },
    packages=find_packages(exclude=('tests',)),

    python_requires='>=3.6',
    install_requires=[
        'bitstring>=3.1',
    ],

    description='Embed messages in the sort order of lists/dicts/JSON/tar.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author="Stephen Zimmerman",
    author_email="sz@recv.cc",

    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
