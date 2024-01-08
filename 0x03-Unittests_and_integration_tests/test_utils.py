from typing import Any, Dict, List, Union

def access_nested_map(nested_map: Dict[str, Any], path: Tuple[str]) -> Union[Any, Dict[str, Any]]:
    """
    Accesses nested values in a map based on a path.
    """
    current = nested_map
    for key in path:
        if key in current:
            current = current[key]
        else:
            raise KeyError(f"Key '{key}' not found in map")
    return current

# Other functions in utils.py (if any)
