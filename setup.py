import os
from distutils.core import setup


def read_file_into_string(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file_into_string(name)
    return ''


setup(
    name='pkimber-stock',
    packages=['stock', 'stock.migrations', 'stock.tests', 'stock.management', 'stock.management.commands'],
    package_data={
        'stock': [
            'static/*.*',
            'templates/*.*',
            'templates/stock/*.*',
        ],
    },
    version='0.1.02',
    description='stock',
    author='Patrick Kimber',
    author_email='code@pkimber.net',
    url='git@github.com:pkimber/stock.git',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Office/Business :: Scheduling',
    ],
    long_description=get_readme(),
)