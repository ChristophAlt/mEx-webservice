import os
from package_settings import NAME, VERSION, PACKAGES, DESCRIPTION
from setuptools import setup
from pathlib import Path
import json
import urllib.request
from functools import lru_cache


GITHUB_ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')


@lru_cache(maxsize=50)
def _get_github_sha(github_install_url: str):
    """From the github_install_url get the hash of the latest commit"""
    repository = Path(github_install_url).stem.split('#egg', 1)[0]
    organisation = Path(github_install_url).parent.stem
    with urllib.request.urlopen(f'https://api.github.com/repos/{organisation}/{repository}/commits/master?access_token={GITHUB_ACCESS_TOKEN}') as response:
        return json.loads(response.read())['sha']

MACSS_MEDICAL_IE_URL = 'github.com/ChristophAlt/macss-medical-ie.git#egg=macss-medical-ie'
MACSS_MEDICAL_IE_GIT = f'git+https://{GITHUB_ACCESS_TOKEN}:@{MACSS_MEDICAL_IE_URL}'


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
        'macss-medical-ie==' + _get_github_sha(MACSS_MEDICAL_IE_GIT)
    ],
    dependency_links=[
        MACSS_MEDICAL_IE_GIT + '-' + _get_github_sha(MACSS_MEDICAL_IE_GIT)
    ],
    package_data={
        '': ['*.*'],
    },
)
