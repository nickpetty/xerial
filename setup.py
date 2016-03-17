from setuptools import setup

setup(
    name='xerial',
    version='1.0.2b1',
    author='Nicholas Petty',
    author_email='nick@ihackeverything.com',
    packages=['app'],
    package_data={'':['docs/README.md']},
    url='http://github.com/nickpetty/xerial',
    license='GPL licence, see LICENCE.txt',
    description='Terminal Based Serial Client',
    long_description=open('app/docs/README.md').read(),
    install_requires=['pyserial'],
    scripts=['bin/xerial']
)



