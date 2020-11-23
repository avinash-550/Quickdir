import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Quickdir", 
    version="0.0.1",
    author="Avinash",
    author_email="avinashwc2011@gmail.com",
    description="A package to create complex directories in single step using JSON objects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Viwarrior/Quickdir",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)