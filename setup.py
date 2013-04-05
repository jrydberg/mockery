from setuptools import setup, find_packages

setup(
    name='mockery',
    version='1.1',
    description='Simple but fully featured stubs and mocks for unittests',
    author='Patrick Fitzsimmons',
    author_email='devteam+mockingbird@hubspot.com',
    url=' http://hubspot.com/',
    packages=find_packages(),
    install_requires=[
        "nose==1.1.2"
        ],
    platforms=["any"],
)


