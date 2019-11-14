from setuptools import setup, find_packages
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "lastfm-now",
    version = "0.0.2",
    author = "Adam Cathersides",
    author_email = "adamcathersides@gmail.com",
    description = ("Display now playing from lastfm"),
    url='https://github.com/adamcathersides/lastfm-now-playing/',
    packages = ['lastfm_now'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data = True,
    install_requires = [
        'click',
        'pylast'
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    entry_points={
          'console_scripts': [
              'lastfm-now = lastfm_now.lastfm_now:run'
          ]
      }
)
