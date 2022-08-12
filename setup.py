from setuptools import setup

# This package is a fork from,
#
# Original repo: http://github.com/oxfordcontrol/miosqp
# Original owner: bartolomeo.stellato@gmail.com


setup(
    name='miosqp',
    version='0.0.1.1',
    author='Muhammad Yasirroni',
    author_email='muhammadyasirroni@gmail.com',
    packages=['miosqp'],
    package_dir={'miosqp': 'miosqp'},
    url='https://github.com/UGM-EPSLab/miosqp',
    license='Apache v2.0',
    description='An MIQP solver based on OSQP',
    install_requires=["osqp",
                      "numpy >= 1.9",
                      "scipy >= 0.15"]
)
