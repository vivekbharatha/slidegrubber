from setuptools import setup

setup(name='slidegrubber',
    version='2.4',
    description='Back up your SlideShare presentations to PDF.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: Free for non-commercial use',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    keywords='funniest joke comedy flying circus',
    url='https://github.com/cballenar/slidegrubber',
    author='Carlos Ballena',
    author_email='cballenar@gmail.com',
    license='MIT',
    packages=['slidegrubber'],
    install_requires=[
        'Wand',
        'requests',
        'beautifulsoup4'
    ],
    zip_safe=False)