from setuptools import setup, find_packages

setup(
    name="visualize_categorical",
    version="0.1",
    packages=find_packages(),  
    install_requires=[
        "pandas>=2.0",
        "matplotlib>=3.7",
    ],
    python_requires=">=3.10",
)