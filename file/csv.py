import csv
import os
from typing import List, Union


def write_csv(file_full: Union[str, os.PathLike], data: List[any]):
    """Writes a row of data to a CSV file.

    Args:
        file_full: The full path to the CSV file.
        data: A list of values to write to the row.
    """

    [folder, filename_base] = os.path.split(file_full)
    if os.path.exists(folder):
        with open(file_full, "a", newline="") as f:
            csvfile = csv.writer(f)
            csvfile.writerow(data)
    else:
        raise OSError("Folder does not exist: " + folder)


def read_csv(file_full: Union[str, os.PathLike]) -> List[List[any]]:
    """Reads a CSV file and returns its contents as a list of lists.

    Args:
        file_full: The full path to the CSV file.

    Returns:
        A list of lists, where each inner list represents a row of data in the CSV file.
    """

    if os.path.exists(file_full):
        with open(file_full, "r") as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                data.append(row)
            return data
    else:
        raise OSError("CSV file does not exist: " + file_full)
