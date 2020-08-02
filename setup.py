import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="boxprint",
    version="0.0.5",
    author="James Kao",
    author_email="james.l.kao@example.com",
    description="A small package for printing boxes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuzuquats/pyboxprint",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
