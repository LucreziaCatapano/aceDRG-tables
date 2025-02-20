from setuptools import setup, find_packages

setup(
    name="aceDRG-tables",
    version="1",
    packages=find_packages(),
    include_package_data=True,  # Ensures data files are included
    package_data={
        "tables": ["**/*"],  # Recursively include all files in the tables package
    },
    install_requires=[],
)
