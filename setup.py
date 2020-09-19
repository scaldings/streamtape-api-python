import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamtape-api-python-scaldings", 
    version="1.0",
    author="scaldings",
    author_email="lukedahlia@gmail.com",
    description="A Streamtape API written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scaldings/streamtape-api-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
