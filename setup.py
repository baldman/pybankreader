# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='bankdata_reader',
    version='0.1',
    url='http://github.com/baldman/bankdata_reader',
    license='BSD',
    author=u'Tomáš Plešek',
    author_email='tomas@plesek.cz',
    description='A library & micro-framework for reading data files exported '
                'from various internet banking solutions. Currently supports '
                'BBF and GPC files (just subsets of those)',
    long_description=__doc__,
    packages=['bankdata_reader'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        "six==1.8.0"
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)