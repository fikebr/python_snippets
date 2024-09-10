import toml
from typing import Union, Any, IO, Dict


def load_file(toml_filename: str) -> Union[Dict[str, Any], None]:
    """Loads a TOML file and returns its parsed data as a dictionary.

    Args:
        toml_filename: The path to the TOML file.

    Returns:
        A dictionary containing the parsed TOML data, or None if an error occurred.
    """

    try:
        with open(toml_filename, "rb") as f:
            # Try UTF-8 first
            try:
                return toml.loads(f.read().decode("utf-8"))
            except UnicodeDecodeError:
                pass

            # Attempt with other encodings
            encodings = ["latin-1", "cp1252"]
            for encoding in encodings:
                try:
                    f.seek(0)  # Reset the file pointer
                    return toml.loads(f.read().decode(encoding))
                except UnicodeDecodeError:
                    pass

        print(
            f"Error: Could not decode file '{toml_filename}' with any supported encoding."
        )
        return None

    except FileNotFoundError:
        print(f"Error: File '{toml_filename}' not found.")
        return None


def save_file(toml_filename: str, data: Dict[str, Any]) -> None:
    """Saves Python data as a TOML file.

    Args:
        toml_filename: The path to the output TOML file.
        data: The Python data to be saved in TOML format.
    """

    with open(toml_filename, "w") as f:
        toml.dump(data, f)


def to_toml(obj: Any) -> str:
    """Converts a Python object to a TOML string.

    Args:
        obj: The Python object to be converted.

    Returns:
        A TOML string representation of the Python object.
    """

    return toml.dumps(obj)


def toml_parse(toml_str: str) -> Dict[str, Any]:
    """Parses a TOML string into a Python dictionary.

    Args:
        toml_str: The TOML string to be parsed.

    Returns:
        A dictionary containing the parsed TOML data.
    """

    return toml.loads(toml_str)
