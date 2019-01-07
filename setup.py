import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sky_remote",
    version="0.0.1",
    author="James Archer",
    author_email="jamesarcher136@googlemail.com",
    description="A package for sending remote commands to Sky+ HD/Sky Q boxes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/archerjm/sky-remote",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Unlicense",
        "Operating System :: OS Independent",
    ],
)
