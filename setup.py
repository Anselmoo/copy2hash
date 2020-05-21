try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from pathlib import Path

import copy2hash

__author__ = "Anselm Hahn"
__email__ = "Anselm.Hahn@gmail.com"


def long_description():
    with open(Path("./README.md")) as f_1:
        readme = f_1.read()
    with open(Path("./CHANGES.md")) as f_2:
        changes = f_2.read()
    with open(Path("./TODO.md")) as f_3:
        todo = f_3.read()

    long_description = (
        f"{readme}\n\n"
        "CHANGES\n"
        "-------\n"
        "{changes}\n"
        "TODO\n"
        "----\n"
        "{todo}\n"
    )
    return long_description


def install_requires():
    with open("requirements.txt") as f:
        required = f.read().splitlines()
    return required


setup(
    name="copy2hash",
    version=copy2hash.__version__,
    description="Copy or rename any file(s) to a hash-secured filename via terminal",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    install_requires=install_requires(),
    packages=["copy2hash",],
    py_modules=[path.stem for path in Path(".").glob("copy2hash/*.py")],
    author=__author__,
    author_email=__email__,
    maintainer=__author__,
    maintainer_email=__email__,
    url="https://github.com/Anselmoo/copy2hash",
    license="MIT",
    entry_points={
        "console_scripts": ["copy2hash = copy2hash.copy2hash:command_line_runner"]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: System :: Shells",
        "Topic :: Database",
        "Topic :: Documentation" "Topic :: Utilities",
    ],
    keywords=["sha", "sha256", "hash", "hash-key", "data-science", "database",],
    extras_require={"testing": ["pipenv"]},
)
