import os
from setuptools import find_packages, setup

# Load README file for long description.
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path.
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Main setup and configuration.
setup(
    name='python-webcrawler',
    version='0.5.1',
    packages=find_packages(),
    include_package_data=True,
    license='Apache License Version 2.0',
    description='Crawls HTML pages for prices and other pieces of data.',
    long_description=README,
    url='https://github.com/marcbperez/python-webcrawler',
    author='marcbperez',
    author_email='marcbperez@users.noreply.github.com',
    install_requires=[
        'requests',
        'lxml',
        'beautifulsoup4',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest-cov',
        'pytest', # Keep at the end to avoid conflicts.
    ],
)
