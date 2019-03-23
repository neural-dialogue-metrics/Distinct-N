from setuptools import setup

__version__ = '0.2.0'

setup(
    name='Distinct-N',
    version=__version__,
    description='Distinct-N metric that measures degree of diversity of generated response',
    url='https://github.com/neural-dialogue-metrics/Distinct-N.git',
    author='cgsdfc',
    author_email='cgsdfc@126.com',
    keywords=[
        'NL', 'CL', 'MT',
        'natural language processing',
        'computational linguistics',
        'machine translation',
    ],
    packages=['distinct_n'],
    scripts=['distinct_metric.py'],
    # py_modules=['distinct_metric'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache-v2',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Linguistic'
    ],
    license='LICENCE.txt',
    long_description=open('README.md').read(),
    install_requires=['numpy==1.13.1'],
)
