"""A small greeting package."""


def greet(name: str) -> str:
    """Return a greeting for the trimmed name."""
    return f"Hello, {name.strip() or 'world'}!"
