import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"
REPO_NAME = "Data-Science-Projects"
AUTHOR_USER_NAME = "SMU"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "smu.akash9@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akashsmu/Data-Science-Projects/tree/main/ML/NLP",
    packages=setuptools.find_packages(where = "ML/NLP/src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"":"src"}
)