from fabric.api import local


def run_test_coverage():
    local('nosetests blog/tests/ --with-coverage --cover-package="blog"')


def make_targz():
    local('python setup.py sdist')


def tests_package_requir():
    local('pip install nose')
    local('pip install --upgrade setuptools')
    local('pip install mock')


def review_package_requir():
    local('pip install coverage')
    local('pip install pylint')


def run_pylint_to_files():
    local('pylint --files-output=y --disable=line-too-long blog/')


def run_pylint_to_console():
    local('pylint --disable=line-too-long blog/')
