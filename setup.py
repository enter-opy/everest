from setuptools import setup, find_packages

with open('README.md') as f:
    description = f.read()

setup(
    name="everest",
    version='0.0.1',
    packages=find_packages(),
    install_requires=['numpy', 'tensorflow'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)