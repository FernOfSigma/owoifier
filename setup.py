import setuptools
import owoifier


setuptools.setup(
    name="owoifier",
    author=owoifier.__author__,
    version=owoifier.__version__,
    description=owoifier.__description__,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "owoifier = owoifier._cli:main"
        ]
    },
    python_requires=">=3.6"
)
