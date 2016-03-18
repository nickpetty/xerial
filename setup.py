from setuptools import setup

setup(
    name='xerial',
    version='1.0.2b1',
    author='Nicholas Petty',
    author_email='nick@ihackeverything.com',
    packages=['app'],
    package_data={'':['docs/*.md','LICENCE']},
    include_package_data=True,
    url='http://github.com/nickpetty/xerial',
    license='GPL licence, see LICENCE',
    description='Terminal Based Serial Client',
    long_description=open('README.md').read(),
    install_requires=['pyserial'],
    scripts=['bin/xerial']
)



