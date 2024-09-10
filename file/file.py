import os
import glob
import shutil
from datetime import datetime
from typing import List, Union, bool, Optional


def get_file_size(file_full: Union[str, os.PathLike]) -> Optional[int]:
    """Gets the size of a file in bytes.

    Args:
        file_full: The full path to the file.

    Returns:
        The size of the file in bytes, or None if an error occurs.
    """

    try:
        stat_info = os.stat(file_full)
        return stat_info.st_size
    except OSError as e:
        raise OSError(f"Error getting file size for {file_full}: {e}")


def get_file_createdt(file_full):
    try:
        stat_info = os.stat(file_full)
        creation_time = (
            stat_info.st_ctime
        )  # Creation time on Windows, change time on Linux

        # Convert timestamps to readable dates
        creation_date = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d")

        return creation_date
    except OSError as e:
        print(f"Error: {e}")
        return None


def get_file_moddt(file_full):
    try:
        stat_info = os.stat(file_full)
        modification_time = stat_info.st_mtime

        # Convert timestamps to readable dates
        modification_date = datetime.fromtimestamp(modification_time).strftime(
            "%Y-%m-%d"
        )

        return modification_date
    except OSError as e:
        print(f"Error: {e}")
        return None


def scandir(dir_name: str, patterns=[]) -> list:
    # https://www.geeksforgeeks.org/python-os-scandir-method/
    # https://docs.python.org/3/library/os.html#os.scandir
    # https://docs.python.org/3/library/os.html#os.DirEntry

    if not patterns:
        patterns = ["*.*"]

    # print(f"scandir: {dir_name}")
    if isdir(dir_name):
        files = []
        for pattern in patterns:
            files = files + glob.glob(os.path.join(dir_name, pattern))

        files = list(map(lambda x: os.path.basename(x), files))
        return sorted(files)
    else:
        return None


def write_file(file, text):
    f = open(file, "w", encoding="utf-8")
    f.write(text)
    f.close()


def write_file_append(file, text):
    f = open(file, "a", encoding="utf-8")
    f.write(text)
    f.close()


def copy_file(source, dest):
    try:
        shutil.copyfile(source, dest)
    except OSError as e:
        raise (e)


def move_file(source, dest):
    try:
        shutil.move(source, dest)
    except OSError as e:
        raise (e)


def read_file(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                contents = f.read()
            return contents
        except FileNotFoundError:
            # Handle the case where the file is not found
            print(f"Error: File '{filename}' not found.")
            return None
    else:
        print(f"Error: File '{filename}' does not exist.")
        return None


def delete(filename):
    os.remove(filename)

