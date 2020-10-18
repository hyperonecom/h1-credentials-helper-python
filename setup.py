import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="credentials-hyperonecom",  # Replace with your own username
    version="0.0.1",
    author="HyperOne",
    description="Library for handling authorization to HyperOne services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kuskoman/h1-credentials-helper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
