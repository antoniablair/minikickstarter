try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Todo: Edit this

config = {
    'description': 'Mini Kickstarter',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'antoniablair@gmail.com',
    'version': '0.1',
    'install_requires': ['nose','painter'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)