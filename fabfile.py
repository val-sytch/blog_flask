from fabric.api import local


def run_test():
    local('cd blog/tests/')
    local('python -m unittest discover')
    local('cd ../../')


def make_targz():
    local('python setup.py sdist')
