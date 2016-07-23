#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='liqpay-python3',
    version='1.1',
    description='LiqPay Python3 SDK',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests']
)
