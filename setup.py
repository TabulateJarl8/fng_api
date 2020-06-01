import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fng_api",
    version="0.0.3",
    author="Tabulate",
    author_email="tabulatejarl8@gmail.com",
    description="API for fakenamegenerator.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TabulateJarl8/fng_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
	install_requires=[
		"requests",
		"bs4"
	],
)
