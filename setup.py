from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyadcsensors',
    version='0.0.1',
    description='Python based ADC Sensor library.',
    long_description=long_description,
    url='https://github.com/macornwell/pyadcsensors.git',
    author='Mike Cornwell',
    author_email='michael.a.cornwell@gmail.com',
    license='License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 3',
    ],

    keywords='Embedded programming',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['Adafruit_ADS1x15'],
)
