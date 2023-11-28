from setuptools import setup
import os

VERSION = "0.3"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-pretty-json",
    description="Datasette plugin that pretty-prints any column values that are valid JSON objects or arrays",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-pretty-json",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_pretty_json"],
    entry_points={"datasette": ["pretty_json = datasette_pretty_json"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest"]},
)
