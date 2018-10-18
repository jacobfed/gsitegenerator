"""Docstring."""
from setuptools import setup

setup(
    name='sitegenerator',
    version='0.1.1',
    packages=['sitegenerator'],
    include_package_data=True,
    install_requires=[
        "click==6.7",
        "jinja2==2.9.6",
        "sh==1.12.14"
    ],
    entry_points={
        'console_scripts': [
            'sitegenerator = sitegenerator.__main__:main'
        ]
    },
)