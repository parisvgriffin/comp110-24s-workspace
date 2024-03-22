"""Functions that either mutate a list or don't."""

def remove_first(inp_list: list[str]) -> None:
    """Remove first element of inp_list."""
    inp_list.pop(0)

def get_first(inp_list: list[str]) -> str:
    """Return first element of inp_list without mutating."""
    return inp_list[0]

def get_and_remove_first (inp_list: list[str]) -> str:
    """Return first element and remove it."""
    element: str = inp_list[0]
    inp_list.pop(0)
    return element