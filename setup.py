from setuptools import setup

setup(
    name='xerial',
    version='1.0.6b1',
    author='Nicholas Petty',
    author_email='nick@ihackeverything.com',
    packages=['xerial'],
    package_data={'':['docs/*.md','LICENSE']},
    include_package_data=True,
    url='http://github.com/nickpetty/xerial',
    license='GPL licence, see LICENSE',
    description='Terminal Based Serial Client',
    long_description=open('README.rst').read(),
    install_requires=['pyserial'],
    scripts=['bin/xerial'],
    keywords="xerial serial"
)



