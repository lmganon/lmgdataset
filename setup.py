from setuptools import find_packages, setup

setup(
    name="lmgdataset",
    version="0.1",
    author="lmganon",
    description="A tool for automatically creating a dataset using selenium",
    url="https://github.com/lmganon/lmgdataset",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "undetected-chromedriver"
    ],
    extras_require={
        "dev": ["isort>=5.12.0", "black>=23.3.0", "flake8>=6.0.0"],
    },
)
