from setuptools import setup


README = open('README.rst').read()

setup(
    name='aiofilecache',
    version='0.0.1',
    author='Alexander Schepanovski',
    author_email='suor.web@gmail.com',

    description='File backend for aiocache',
    long_description=README,
    url='http://github.com/Suor/aioscrape',
    license='BSD',

    install_requires=[
        'aiocache',
        'aiofiles',
    ],
    py_modules=['aiofilecache'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ]
)
