'''
This is the setup script for galah.  It contains all of the package information
and dependencies
'''
from setuptools import setup,find_packages
import os

pkg_vars  = {}

with open("src/delma/version.py") as fp:
    exec(fp.read(), pkg_vars)

os.system("conda install geos")
os.system("pip install packaging")

setup(
    #name='delma',
    version=pkg_vars['__version__'],
    license='MPL-2.0',
    author='Amanda Buyan',
    author_email='amanda.buyan@csiro.au',
    description="Package for creating Darwin Core Archives",
    long_description="Package for creating Darwin Core Archives",
    long_description_content_type='text/markdown',
    packages=find_packages('src'),
    package_dir={'':'src'},
    url='https://delma.ala.org.au/Python/',
    keywords='delma',
    install_requires=[
        'pandas',
        'beautifulsoup4',
        'configparser',
        'pytest',
        'requests',
        'shutils',
        'metapype',
        'xmltodict',
        'xmlschema'
    ],

    include_package_data = True,
    package_data = {
    # If any package contains *.ini files or *.csv files, include them
    '': ['config.ini','metadata_template.md'],
    },
)
