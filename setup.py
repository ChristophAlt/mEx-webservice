import os
from package_settings import NAME, VERSION, PACKAGES, DESCRIPTION
from setuptools import setup
from pathlib import Path
import json
import urllib.request
from functools import lru_cache


@lru_cache(maxsize=50)
def _get_github_sha(github_install_url: str):
    """From the github_install_url get the hash of the latest commit"""
    repository = Path(github_install_url).stem.split('#egg', 1)[0]
    organisation = Path(github_install_url).parent.stem
    github_access_token = os.getenv('GITHUB_ACCESS_TOKEN')
    with urllib.request.urlopen(f'https://api.github.com/repos/{organisation}/{repository}/commits/master?access_token={github_access_token}') as response:
        return json.loads(response.read())['sha']


setup(
    name=NAME,
    version=VERSION,
    long_description=DESCRIPTION,
    author='Christoph Alt',
    author_email='christoph.alt@posteo.de',
    packages=PACKAGES,
    include_package_data=True,
    install_requires=[
        'sanic==0.8.3',
        'pytest==3.8.1',
        'macss-medical-ie==' + _get_github_sha(
            'git+ssh://git@github.com/ChristophAlt/macss-medical-ie.git#egg=macss-medical-ie')
    ],
    dependency_links=[
        'git+ssh://git@github.com/ChristophAlt/macss-medical-ie.git#egg=macss-medical-ie-' + _get_github_sha(
            'git+ssh://git@github.com/ChristophAlt/macss-medical-ie.git#egg=macss-medical-ie')
    ],
    package_data={
        '': ['*.*'],
    },
)
