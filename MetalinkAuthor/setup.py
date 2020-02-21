import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metalink-author-jakekara",
    version="0.0.1",
    author="Jake Kara",
    author_email="jake@jakekara.com",
    description="A library for authoring Metalink documents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jakekara/metalink-author",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)