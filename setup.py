# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

tests_require = ['six', 'pytest>=3.6.0', 'pytest-cov', 'python-coveralls', 'nose', 'django>=1.11.21']

setup(
    name='pysnap',
    version='1.0.1',  # PEP 440 "local version identifier"
    description='Snapshot Testing utils for Python',
    long_description=readme,
    author='Conner Swann',
    author_email='me@connerswann.me',
    url='https://github.com/yourbuddyconner/pysnap',
    # custom PyPI classifier for pytest plugins
    entry_points={
        'pytest11': [
            'pysnap = pysnap.pytest',
        ],
        'nose.plugins.0.10':
        ['pysnap = pysnap.nose:SnapshotTestPlugin']
    },
    install_requires=['six>=1.10.0', 'termcolor'],
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'pytest': [
            'pytest',
        ],
        'nose': [
            'nose',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
    ],
    license='MIT',
    packages=find_packages(exclude=('tests', )))
