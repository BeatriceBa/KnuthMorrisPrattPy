from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'A package implementing the Knuth Morris Pratt algorithm for pattern searching.'

setup(
        name="knuthMorrisPratt", 
        url='https://github.com/BeatriceBa/KnuthMorrisPrattPy',
        version=VERSION,
        author="Beatrice Baldassarre",
        author_email="<beatrice.baldassarre@mail.polimi.it>",
        description= DESCRIPTION,
        long_description = open('README.md').read(),
        packages=find_packages(),
)