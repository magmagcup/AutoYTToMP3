import os


def return_path(folder: str) -> str:
    original_path = os.getcwd()
    path = original_path + r"\music\\"[:-1] + folder + r"\\"
    return path


