from setuptools import setup, find_packages

setup(
    name='blog_flask',
    version='1.0',
    packages=find_packages(),
    install_requires=['Flask', 'Pillow'],
    include_package_data=True,
    url='https://github.com/val-sytch/blog_flask',
    license='MIT',
    author='val.sytch',
    description='Blog on flask'
)
