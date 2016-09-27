from fabric.api import local


def run_tests():
    """
    Launch all tests. To use this function firstly launch tests_package_requir()
    """
    local('nosetests')


def run_test_coverage():
    """
    print coverage report to console
    """
    local('nosetests blog/tests/ --with-coverage --cover-package="blog"')


def make_targz():
    """
    make tar.gz for distribution. It could be easily installed at other PC or server with pip
    """
    local('python setup.py sdist')


def tests_package_requir():
    """
    Package required for testing application
    """
    local('pip install nose')
    local('pip install --upgrade setuptools')
    local('pip install mock')


def review_package_requir():
    """
    Package required for launching coverage and pylint report
    """
    local('pip install coverage')
    local('pip install pylint')


def run_pylint_to_files():
    """
    Make a pylint report. Report about each file will be writen to the separate .txt file
    and saved to project root
    """
    local('pylint --files-output=y --disable=line-too-long blog/')


def run_pylint_to_console():
    """
    Write a pylint report to console
    """
    local('pylint --disable=line-too-long blog/')
