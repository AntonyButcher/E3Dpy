import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="E3Dpy",
    version="0.0.1",
    author="Antony Butcher",
    author_email="",
    description="E3Dpy - A package for creating E3D parameter files in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AntonyButcher/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
