from os import path
import pathlib


def get_fixture_location(name):
    parent = pathlib.Path(__file__).parent.absolute()
    return path.join(parent, 'fixtures', name)
