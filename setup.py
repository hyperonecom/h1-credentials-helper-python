import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRES = ["PyJWT>=1.7.1", "cryptography >= 3.1.1"]

setuptools.setup(
    name="credentials-hyperonecom",
    version="0.0.1",
    author="HyperOne",
    description="Library for handling authorization to HyperOne services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kuskoman/h1-credentials-helper",
    install_requires=REQUIRES,
    packages=setuptools.find_packages(exclude=["test", "tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
