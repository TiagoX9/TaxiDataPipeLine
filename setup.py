from setuptools import setup

SHORT_DESCRIPTION = 'A library to analyse Newyork yellow taxi data.'

try:
    with open('README.md', encoding='utf8') as readme:
        LONG_DESCRIPTION = readme.read()

except FileNotFoundError:
    LONG_DESCRIPTION = SHORT_DESCRIPTION


setup(
    name='taxidata',
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    version='1.0.0',
    author="Sushma Goutam",
    author_email="sushma.goutam@gmail.com",
    url="https://github.com/write2sushma/TaxiDataPipeLine.git",
    packages=["taxidata"],
    license='MIT',
    platforms='any',
    install_requires=[
        'numpy==1.18.1',
        'pandas==1.0.0',
        'dask[complete]',
        'requests==2.22.0'
    ],
    classifiers=[
        "Development Status :: 1 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
    ]
)
