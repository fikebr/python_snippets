import os
import shutil
from typing import List, Union, bool


def subfolders(parent_folder: Union[str, os.PathLike]) -> List[str]:
    """Returns a list of subfolders within the specified parent folder.

    Args:
        parent_folder: The path to the parent folder.

    Returns:
        A list of subfolder names within the parent folder.
    """

    contents: List[str] = []

    if os.path.exists(parent_folder):
        contents = os.listdir(parent_folder)
        contents = list(
            filter(lambda x: os.path.isdir(os.path.join(parent_folder, x)), contents)
        )

    return contents


def isdir(dir: Union[str, os.PathLike]) -> bool:
    """Checks if the given path is a directory.

    Args:
        dir: The path to be checked.

    Returns:
        True if the path is a directory, False otherwise.
    """
    return os.path.isdir(dir)


def create_folder(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            # print(f"Folder '{folder_path}' created successfully.")
    except OSError as e:
        print(f"Error creating folder: {e}")


def delete_folder(folder_path):
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        else:
            raise ValueError("Folder DNE: {}".format(folder_path))
    except OSError as e:
        print(f"Error deleting folder: {e}")


