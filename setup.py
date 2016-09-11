from setuptools import setup, find_packages

setup(
    name='blogFlask',
    version='1.0',
    packages=find_packages(),
    install_requires=['Flask', 'Pillow'],
    url='https://github.com/val-sytch/blog_flask',
    license='MIT',
    author='val.sytch',
    description='Blog on flask'
)