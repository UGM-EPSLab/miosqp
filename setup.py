import os
import re

from setuptools import setup

PACKAGE_NAME = 'miosqp'
current_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_path, PACKAGE_NAME, '__init__.py'), "r") as f:
    version_line = f.read()

m = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_line, re.M)
__version__ = m.group(1)

setup(
    name=PACKAGE_NAME,
    version=__version__,
    author='Bartolomeo Stellato, Vihangkumar V. Naik',
    author_email='bartolomeo.stellato@gmail.com, vihangkumar.naik@imtlucca.it',
    packages=['miosqp'],
    package_dir={'miosqp': 'miosqp'},
    url='http://github.com/oxfordcontrol/miosqp',
    license='Apache v2.0',
    description='An MIQP solver based on OSQP',
    install_requires=["osqp",
                      "numpy >= 1.9",
                      "scipy >= 0.15"]
)
