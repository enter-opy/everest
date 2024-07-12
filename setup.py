from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name="everest",
    version=VERSION,
    packages=find_packages(),
    install_requires=['numpy', 'tensorflow'],
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Production",
        "Intended Audience :: Developers, Researchers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)