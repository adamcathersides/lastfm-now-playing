from setuptools import setup, find_packages

setup(
    name = "lastfm-now",
    version = "0.0.1",
    author = "Adam Cathersides",
    author_email = "adamcathersides@gmail.com",
    description = ("Display now playing from lastfm"),
    url='https://github.com/adamcathersides/lastfm-now-playing/',
    packages = ['lastfm_now'],
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
