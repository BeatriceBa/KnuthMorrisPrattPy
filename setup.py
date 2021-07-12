import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="knuthMorrisPratt",
    version="0.0.1",
    author="Beatrice Baldassarre",
    author_email="beatrice.baldassarre@mail.polimi.it",
    description="A package implementing the Knuth Morris Pratt algorithm for pattern searching.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BeatriceBa/KnuthMorrisPrattPy",
    project_urls={
        "Bug Tracker": "https://github.com/BeatriceBa/KnuthMorrisPrattPy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)