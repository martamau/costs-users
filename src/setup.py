import setuptools
import os

setuptools.setup(
    name="cost-functions",
    version="0.1.0",
    author="Marta Mauri",
    author_email="marta.mauri@zapatacomputing.com",
    description="Cost function package",
    url="https://github.com/martamau/costs-users",
    packages=setuptools.find_namespace_packages(),
    package_dir={"": "python"},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
