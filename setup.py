# coding: utf-8
import os
import sys

from setuptools import setup


__version__ = '1.6.0'
__author__ = 'CHIDA <iam.yeongbin.jo@gmail.com>'
__token__ = 'yeongbin_jo'


with open('README.md') as readme_file:
    long_description = readme_file.read()


# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()
elif sys.argv[-1] == 'clean':
    import shutil
    if os.path.isdir('build'):
        shutil.rmtree('build')
    if os.path.isdir('dist'):
        shutil.rmtree('dist')
    if os.path.isdir('pylab_sdk.egg-info'):
        shutil.rmtree('pylab_sdk.egg-info')


setup(
    name="pylab-sdk",
    version=__version__,
    author="CHIDA",
    author_email="iam.yeongbin.jo@gmail.com",
    description="A development kit that collects simple utilities.",
    license="MIT",
    keywords="python",
    url="https://github.com/PyLabCo/pylab-sdk",
    packages=['pylab_sdk'],
    long_description_content_type='text/markdown',
    long_description=long_description,
    python_requires='>=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Installation/Setup',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    install_requires=[
        'requests',
    ]
)
