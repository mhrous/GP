from os import listdir
from os.path import isfile, join,abspath


def get_file_from_folder(path):

    return [abspath(join(path, f)) for f in listdir(path) if isfile(join(path, f))]


