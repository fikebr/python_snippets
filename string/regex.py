import re

def regex_pattern(pattern: str):
    pattern = re.compile(r"\d+")  # Matches one or more digits
    return(pattern)

def regex_match(pattern: str, string: str) -> re.match:
    """if pattern matches the ENTIRE string. Returns a `match` object or `None`."""
    p = regex_pattern(pattern)
    m = re.match(p, string)
    return(m)

    # "m" is a match object
    # match.group()  # Access the entire matched substring (phone number)
    # match.start()  # Starting index of the match
    # match.end()  # Ending index of the match
    # match.group(1)  # Assuming a capturing group exists (e.g., (\d{3}))

def regex_search(pattern: str, string: str) -> re.match:
    """Returns the first `match` or `None`."""
    p = regex_pattern(pattern)
    m = re.search(p, string)
    return(m)

def regex_findall(pattern: str, string: str):
    """Finds all non-overlapping matches. Returns a list of matching substrings."""
    p = regex_pattern(pattern)
    m = re.findall(p, string)
    return(m)

def regex_sub(pattern: str, string: str, replace: str, count: int = 0) -> str:
    """Replaces occurrences of `pattern` in `string` with `repl`. count is the num of replacements to make"""
    p = regex_pattern(pattern)
    m = re.sub(p, replace, string, count)
    return(m)

