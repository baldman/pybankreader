# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='pybankreader',
    version='0.2.3',
    url='http://github.com/baldman/pybankreader',
    license='BSD',
    author=u'Tomáš Plešek',
    author_email='tomas@plesek.cz',
    description='A library & micro-framework for reading data files exported '
                'from various internet banking solutions. Currently supports '
                'BBF and GPC files (just subsets of those for the time being)',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=[
        "six==1.8.0"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
