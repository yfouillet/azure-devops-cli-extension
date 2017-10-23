# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# ---------------------------------------------------------

from setuptools import setup, find_packages

NAME = 'vsts-cli-common'
VERSION = '0.1.0-preview+dev'

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    'keyring',
    'knack',
    'python-dateutil',
    'vsts==0.1.0-preview+dev'
]

setup(
    name=NAME,
    version=VERSION,
    description="VSTS Command Line Common",
    author="Ted Chambers",
    author_email="tedchamb@microsoft.com",
    url="https://github.com/Microsoft/vsts-cli",
    keywords=["Microsoft", "VSTS", "Team Services", "SDK", "AzureTfs", "CLI"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)
